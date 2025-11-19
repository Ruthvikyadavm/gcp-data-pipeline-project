from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# WSL paths (Linux format)
output_path = "/home/ruthvruthvik/week5/output/"
checkpoint_path = "/home/ruthvruthvik/week5/checkpoint/"

taxi_schema = StructType([
    StructField("VendorID", IntegerType()),
    StructField("tpep_pickup_datetime", StringType()),
    StructField("tpep_dropoff_datetime", StringType()),
    StructField("passenger_count", IntegerType()),
    StructField("trip_distance", DoubleType()),
    StructField("RatecodeID", IntegerType()),
    StructField("store_and_fwd_flag", StringType()),
    StructField("PULocationID", IntegerType()),
    StructField("DOLocationID", IntegerType()),
    StructField("payment_type", IntegerType()),
    StructField("fare_amount", DoubleType())
])

spark = SparkSession.builder \
    .appName("KafkaSparkStreamingLocal") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "taxi_trips") \
    .option("startingOffsets", "latest") \
    .load()

json_df = df.select(from_json(col("value").cast("string"), taxi_schema).alias("data"))

final_df = json_df.select("data.*") \
    .withColumn("tpep_pickup_datetime", to_timestamp("tpep_pickup_datetime")) \
    .withColumn("tpep_dropoff_datetime", to_timestamp("tpep_dropoff_datetime"))

# Write to Linux filesystem
query = final_df.writeStream \
    .format("json") \
    .outputMode("append") \
    .option("path", "/home/ruthvruthvik/week5/output/") \
    .option("checkpointLocation", "/home/ruthvruthvik/week5/checkpoint/") \
    .start()


query.awaitTermination()


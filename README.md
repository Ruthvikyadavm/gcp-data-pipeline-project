🚕 End-to-End Data Engineering Pipeline

GCP | PySpark | Kafka | Spark Structured Streaming | Airflow | BigQuery

This project demonstrates a production-grade data engineering pipeline on Google Cloud Platform, supporting batch ETL and real-time streaming use cases.

📊 Records processed: 2.7M+
⚙️ Architecture: Batch + Streaming
🎥 YouTube Demo: https://youtu.be/Cb2BpFoL30g

📈 Dashboard: https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

🏗️ Architecture
Batch ETL

Raw CSV → GCS → PySpark (Dataproc) → GCS Processed → BigQuery → Looker

Streaming

Kafka → Spark Structured Streaming → BigQuery

📁 Project Structure
gcp-data-pipeline-project/
│── dags/
│   └── gcp_etl_dag.py
│── week3/
│   └── pyspark_etl.py
│── week5-streaming/
│   ├── kafka_producer.py
│   └── spark_streaming.py
│── screenshots/
│── README.md

🚀 Batch ETL Pipeline
1️⃣ Upload Raw Data to GCS
gsutil cp big_dataset.csv gs://my-gcp-bucket/raw/big_dataset.csv


2️⃣ PySpark Transformation (Dataproc)

week3/pyspark_etl.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder.appName("TaxiETL").getOrCreate()

input_path = "gs://my-gcp-bucket/raw/big_dataset.csv"
output_path = "gs://my-gcp-bucket/processed/taxi_data"

df = spark.read.option("header", True).csv(input_path)

clean_df = (
    df
    .dropna(subset=["pickup_datetime", "fare_amount"])
    .withColumn("pickup_datetime",
                to_timestamp(col("pickup_datetime"), "yyyy-MM-dd HH:mm:ss"))
    .withColumn("fare_amount", col("fare_amount").cast("double"))
)

clean_df.write.mode("overwrite").parquet(output_path)

spark.stop()





3️⃣ Load into BigQuery (Airflow)

dags/gcp_etl_dag.py

from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="gcp_batch_etl",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    load_to_bq = GCSToBigQueryOperator(
        task_id="load_to_bigquery",
        bucket="my-gcp-bucket",
        source_objects=["processed/taxi_data/*"],
        destination_project_dataset_table="my_project.analytics.taxi_trips",
        source_format="PARQUET",
        write_disposition="WRITE_TRUNCATE",
        autodetect=True
    )


4️⃣ BigQuery Analytics View
CREATE OR REPLACE VIEW analytics.daily_revenue AS
SELECT
  DATE(pickup_datetime) AS trip_date,
  SUM(fare_amount) AS total_revenue
FROM analytics.taxi_trips
GROUP BY trip_date;





⚡ Real-Time Streaming Pipeline
5️⃣ Kafka Producer

week5-streaming/kafka_producer.py

from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    event = {
        "pickup_datetime": time.strftime("%Y-%m-%d %H:%M:%S"),
        "fare_amount": round(random.uniform(5, 50), 2)
    }
    producer.send("taxi_topic", event)
    time.sleep(1)

6️⃣ Spark Structured Streaming Consumer

week5-streaming/spark_streaming.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("KafkaStreaming").getOrCreate()

schema = StructType() \
    .add("pickup_datetime", StringType()) \
    .add("fare_amount", DoubleType())

kafka_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "taxi_topic")
    .load()
)

parsed_df = kafka_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

query = (
    parsed_df.writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()


📊 BI Dashboard (Looker Studio)

Metrics:

Daily revenue

Peak hours

Trip density

Pickup zones

🧰 Tech Stack
Layer	Tools
Cloud	GCP (GCS, Dataproc, BigQuery, Composer)
Processing	PySpark, Spark Structured Streaming
Streaming	Apache Kafka
Orchestration	Airflow
BI	Looker Studio
Language	Python, SQL
📈 Key Outcomes

Built batch + streaming hybrid architecture

Processed 2.7M+ records

Automated pipelines using Airflow

Delivered analytics-ready datasets

Implemented fault-tolerant streaming

📬 Contact

Ruthvik Kumar Yadav Maram
📍 Schaumburg, IL
📧 ruthvikyadav930@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/ruthvikyadav/

🔗 GitHub: https://github.com/Ruthvikyadavm

✅ IMPORTANT

Make sure these files exist:

screenshots/
├── architecture-batch.png
├── architecture-streaming.png
├── gcs-raw.png
├── dataproc-create.png
├── gcs-processed.png
├── bq-table-schema.png
├── bq-views.png
├── airflow-run.png
├── spark-stream.png
├── dashboard.png

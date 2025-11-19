import sys
from pyspark.sql import SparkSession
import argparse

# ------------------------------
# Parse command-line arguments
# ------------------------------
parser = argparse.ArgumentParser(description="Process big data with PySpark")
parser.add_argument("--input", required=True, help="GCS input file path")
parser.add_argument("--output", required=True, help="GCS output path")
args = parser.parse_args()

input_path = args.input
output_path = args.output

# ------------------------------
# Create Spark session
# ------------------------------
spark = SparkSession.builder.appName("Week3DataProcessing").getOrCreate()

# ------------------------------
# Read CSV from GCS
# ------------------------------
df = spark.read.csv(input_path, header=True, inferSchema=True)

# ------------------------------
# Transformations
# Example: lowercase column names and drop rows with nulls
# ------------------------------
df = df.toDF(*[c.lower() for c in df.columns])
df = df.na.drop()

# ------------------------------
# Write output back to GCS
# ------------------------------
df.write.csv(output_path, mode="overwrite", header=True)

spark.stop()
print(f"Data processed successfully! Output saved to: {output_path}")


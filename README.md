🚀 End-to-End Data Engineering Pipeline on Google Cloud Platform (GCP)

This project showcases a production-grade data pipeline built using
Google Cloud Storage, PySpark on Dataproc, BigQuery, Apache Airflow, Looker Studio, and Kafka Streaming.

The pipeline ingests raw NYC Yellow Taxi data → processes it using distributed PySpark → loads it into BigQuery → visualizes insights → and supports real-time streaming via Kafka + Spark Structured Streaming.

-----

⚡ TL;DR — What I Built

🟡 Raw → GCS (Raw Zone)

🔵 Transform → PySpark on Dataproc

🟣 Store → BigQuery Analytics Warehouse

🟢 Visualize → Looker Studio Dashboard

🔴 Orchestrate → Apache Airflow DAG

🟠 Stream → Kafka + Spark Structured Streaming

⚡ Processed 2.7M+ taxi trip records end-to-end

-----

🏗️ Architecture (Batch Pipeline)
Raw CSV 
   → Google Cloud Storage (Raw Zone)
   → Dataproc PySpark Job (Transform & Clean)
   → Google Cloud Storage (Processed Zone)
   → BigQuery (Partitioned Analytics Warehouse)
   → Looker Studio (Visualization)


---


🛠️ Technologies Used
Component	                Technology
Cloud	                        Google Cloud Platform
Storage	                        Google Cloud Storage (GCS)
Compute	                        Dataproc (PySpark)
ETL	                        Python, Spark
Warehouse	                BigQuery
Orchestration	                Apache Airflow
Visualization	                Looker Studio
Streaming	                Kafka + Spark Structured Streaming
Language	                Python, SQL
Version Control	                Git & GitHub

----


📁 Repository Structure
gcp-data-pipeline-project/
│
├── week1/        # Raw ingestion to GCS + BigQuery load
├── week2/        # Data cleaning + automated pipeline
├── week3/        # PySpark on Dataproc + processed outputs
├── week4/        # BigQuery views + Looker dashboard
├── week5/        # Kafka + Spark Structured Streaming
│
├── dags/         # Airflow DAG files
│   └── gcs_to_bigquery_dag.py
│
├── screenshots/  # Architecture, GCS, BQ, Dashboard screenshots
└── README.md

-----

🎯 How to Run the Project (Quick Start)

1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Upload Raw CSV to GCS
gsutil cp nyc_taxi_raw.csv gs://ruthvik-week3-bucket-2/raw/

3️⃣ Run Week 2 Cleanup
python week2/clean_data.py

4️⃣ Submit PySpark Job on Dataproc
gcloud dataproc jobs submit pyspark \
    --cluster=my-spark-cluster \
    --region=us-central1 \
    week3/process_big_data.py

5️⃣ Airflow DAG Loads Processed CSV → BigQuery Automatically

6️⃣ Open Looker Dashboard (Live Link)

🔗 https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

---------

📦 Week 1 – Data Ingestion & Environment Setup

✔ Tasks Completed

Created GCP project, service account, IAM roles

Uploaded raw CSV into GCS (Raw Zone)

Loaded raw data into BigQuery using autodetect

Explored dataset using SQL queries

🧠 Skills Practiced

GCS buckets, BigQuery tables, schema detection, gcloud CLI, Python.

-----

🧹 Week 2 – Data Cleaning & Automated ETL

✔ Tasks Completed

Performed data cleaning using Pandas

Fixed inconsistent types, nulls, outliers

Uploaded the cleaned dataset to GCS (Processed Zone)

Automated ingestion script

🧠 Skills Practiced

Python ETL, Pandas, data quality checks, automation.

---

⚡ Week 3 – Distributed Processing with PySpark (Dataproc)

✔ Tasks Completed

Created Dataproc cluster

Executed PySpark job on 2.7M+ records

Stored processed outputs into GCS as Parquet/CSV

Connected BigQuery to processed data

🧠 Skills Practiced

Spark DataFrames, partitioning, cluster-based ETL, optimization.

---

📊 Week 4 — BigQuery Analytics + Looker Studio Dashboard

✔ SQL Views Created

View	                    Description
trips_by_passenger	     Avg fare vs passenger count
trips_over_time	        Daily trip counts and seasonality
high_fare_trips	        Outlier/high value rides

-----

✔ Dashboard Includes

Daily revenue trend

Avg distance trend

Top pickup zones

Fare distribution

🔗 Live Dashboard:
https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

-------

🌬️ Week 5 – Real-Time Streaming (Kafka + Spark Structured Streaming)

This week adds near real-time micro-batch processing.

🔥 Architecture
Producer → Kafka Topic (`taxi_trips`) 
        → Spark Structured Streaming (JSON processing)
        → GCS / Local JSON Output

✔ Technologies Used

Kafka 3.5.1, Zookeeper, Spark 3.5.1, JSON events, WSL2 Ubuntu.

✔ Real Output Sample
{"VendorID":1,"trip_distance":3.5,"fare_amount":12.5,...}

✔ What I Learned

Kafka topic creation

Producer/Consumer basics

Micro-batch streaming

Checkpointing & fault tolerance

Fixing Spark classpath issues

-------

🌀 Orchestration — Airflow DAG

This DAG automatically:

Lists all processed CSV files in GCS

Loads them into BigQuery

Truncates table and refreshes analytics daily

----

📌 DAG Code Used

from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


with DAG(
    dag_id="gcs_to_bigquery_dag",
    start_date=datetime(2025, 11, 8),
    schedule="0 0 * * *",   # Runs once per day
    catchup=False,
    tags=["gcs", "bigquery"],
):
    
    list_gcs_files = GCSListObjectsOperator(
        task_id="list_gcs_files",
        bucket="ruthvik-week3-bucket-2",
        prefix="",
        gcp_conn_id="google_cloud_default"
    )

    load_to_bigquery = GCSToBigQueryOperator(
        task_id="load_to_bigquery",
        bucket="ruthvik-week3-bucket-2",
        source_objects=["week3/output/part-*.csv"],
        destination_project_dataset_table="ruthvik-week3-dataproc.nyc_taxi_demo.trips",
        write_disposition="WRITE_TRUNCATE",
        source_format="CSV",
        skip_leading_rows=1,
        autodetect=True,
        gcp_conn_id="google_cloud_default",
    )

    list_gcs_files >> load_to_bigquery

-----


Airflow Graph view

Airflow Code view

Successful DAG run

------

📈 Key Insights from the Data

2.8M+ rides analyzed

Avg fare stays stable for 1–4 passengers, spikes at 7+

Trip volume spikes ≠ fare spikes

Pickup hotspots: Manhattan transit, tourist zones

Seasonal patterns in trip count & revenue

----

🎯 Next Steps (Planned Enhancements)

Stream Kafka data directly into BigQuery

Add Kafka Connect + Schema Registry

Add Terraform (IaC for bucket, cluster, BQ)

Add CI/CD using Cloud Build or GitHub Actions

Build a monitoring dashboard (Cloud Logging + Grafana)

----

🔗 Important Links

🔸 Dashboard
https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

🔸 LinkedIn
https://www.linkedin.com/in/ruthvikyadav/

🔸 GitHub Repository
https://github.com/Ruthvikyadavm/gcp-data-pipeline-project



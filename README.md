# 🚀 End-to-End Data Engineering Pipeline on Google Cloud Platform (GCP)

This project showcases a **production-grade data pipeline** built using  
**Google Cloud Storage, PySpark on Dataproc, BigQuery, Apache Airflow, Looker Studio, and Kafka Streaming**.

The pipeline ingests raw **NYC Yellow Taxi** data → processes it using **distributed PySpark** → loads it into **BigQuery** → visualizes insights → and supports **real-time streaming** via Kafka + Spark Structured Streaming.

---

# ⚡ TL;DR — What I Built

- Raw → **GCS (Raw Zone)**
- Transform → **Dataproc (PySpark)**
- Store → **BigQuery**
- Visualize → **Looker Studio**
- Orchestrate → **Apache Airflow DAG**
- Stream → **Kafka + Spark Structured Streaming**
- Processed **2.7M+ records**

---

# 🏗️ Architecture (Batch Pipeline)

```
Raw CSV 
   → Google Cloud Storage (Raw Zone)
   → Dataproc PySpark Job (Transform & Clean)
   → Google Cloud Storage (Processed Zone)
   → BigQuery (Partitioned Analytics Warehouse)
   → Looker Studio (Visualization)
```

![Architecture Diagram](gcp_bold_pipeline_diagram.png)

---

# 🛠️ Technologies Used

| Component | Technology |
|----------|------------|
| Cloud | Google Cloud Platform |
| Storage | Google Cloud Storage (GCS) |
| Compute | Dataproc (PySpark) |
| ETL | Python, Spark |
| Warehouse | BigQuery |
| Orchestration | Apache Airflow |
| Visualization | Looker Studio |
| Streaming | Kafka + Spark Structured Streaming |
| Language | Python, SQL |
| Version Control | Git & GitHub |

---

# 📁 Repository Structure

```
gcp-data-pipeline-project/
│
├── week1/        # Raw ingestion → GCS + BigQuery load
├── week2/        # Data cleaning + automated pipeline
├── week3/        # PySpark on Dataproc + processed outputs
├── week4/        # BigQuery views + Looker dashboard
├── week5/        # Kafka + Spark Structured Streaming
│
├── dags/         # Airflow DAG definitions
│   └── gcs_to_bigquery_dag.py
│
├── screenshots/  # Architecture, GCS, BigQuery, Dashboard screenshots
└── README.md
```

---

# 🎯 Quick Start – How to Run the Pipeline

### **Install Dependencies**
```
pip install -r requirements.txt
```

### **Upload Raw Data to GCS**
```
gsutil cp nyc_taxi_raw.csv gs://ruthvik-week3-bucket-2/raw/
```

### **Run Data Cleaning (Week 2)**
```
python week2/clean_data.py
```

### **Submit PySpark Job on Dataproc (Week 3)**
```
gcloud dataproc jobs submit pyspark \
    --cluster=my-spark-cluster \
    --region=us-central1 \
    week3/process_big_data.py
```

### **Airflow DAG Automatically Loads into BigQuery (Week 4)**
DAG: `gcs_to_bigquery_dag`

### **Live Dashboard**
🔗 https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

---

# 📦 Week 1 — Data Ingestion & Environment Setup

### ✔ Tasks
- Created GCP project + IAM roles  
- Uploaded raw CSV to **GCS (Raw Zone)**  
- Loaded raw data into BigQuery using autodetect  
- Validated schema with SQL  

### Skills: GCS, BQ, IAM, gcloud

---

# 🧹 Week 2 — Data Cleaning & Python ETL

### ✔ Tasks
- Cleaned dataset using Pandas  
- Fixed nulls, types, outliers  
- Uploaded cleaned data to **GCS (Processed Zone)**  
- Automated ETL script  

### Skills: Python, Pandas, DQ checks

---

# ⚡ Week 3 — Distributed PySpark on Dataproc

### ✔ Tasks
- Created Dataproc cluster  
- Processed **2.7M+ rows** using PySpark  
- Saved output to GCS  
- Connected BigQuery to processed dataset  

### Skills: Spark DataFrames, partitioning, optimization

---

# 📊 Week 4 — BigQuery Analytics + Looker Dashboard

### ✔ Views
| View | Description |
|------|-------------|
| `trips_by_passenger` | Avg fare vs passengers |
| `trips_over_time` | Daily trip patterns |
| `high_fare_trips` | Outlier detection |

### ✔ Dashboard Includes
- Daily fare + revenue trends  
- Avg trip distance  
- Top pickup zones  
- Automatic refresh via BigQuery  

🔗 Dashboard:  
https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

---

# 🌬️ Week 5 — Real-Time Streaming (Kafka + Spark Structured Streaming)

### Architecture
```
Kafka Producer 
   → Kafka Topic (`taxi_trips`)
   → Spark Structured Streaming (micro-batch)
   → JSON output / GCS sink
```

### Skills
- Kafka (broker, zookeeper, topics)  
- Streaming ETL  
- Checkpoints + fault tolerance  
- JSON event processing  

### Sample Output
```
{"VendorID":1,"trip_distance":3.5,"fare_amount":12.5,...}
```

---

# 🌀 Airflow Orchestration (Daily Automated Load)

### What This DAG Does
1. Lists processed files in GCS  
2. Loads them into BigQuery  
3. Replaces table daily  

### DAG Code (`gcs_to_bigquery_dag.py`)
```
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
```

---

# 📈 Key Insights

- Analyzed **2.8M+ trips**  
- Avg fare stable for 1–4 passengers, spikes at 7+  
- Pickup hotspots: Manhattan transit hubs  
- Seasonal ride volume patterns  
- Revenue ≠ trip count correlation  

---

# 🔮 Next Enhancements

- Kafka → BigQuery using Kafka Connect  
- Terraform IaC for buckets, cluster, BigQuery  
- CI/CD: GitHub Actions + Cloud Build  
- Monitoring: Cloud Logging + Grafana  
- ML models (fare prediction, demand prediction)

---

# 🔗 Important Links

👉 **Dashboard:**  
https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

👉 **LinkedIn:**  
https://www.linkedin.com/in/ruthvikyadav/

👉 **GitHub:**  
https://github.com/Ruthvikyadavm/gcp-data-pipeline-project


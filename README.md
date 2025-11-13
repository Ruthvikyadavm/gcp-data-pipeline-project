# End-to-End Data Engineering Pipeline on GCP

This project demonstrates a production-grade data pipeline built using **Google Cloud Platform (GCP)**, **PySpark**, and **Apache Airflow**.  
The pipeline ingests raw NYC Taxi trip data, processes it with PySpark on Dataproc, loads it into BigQuery, and visualizes insights in Looker Studio.

The full workflow represents real-world **batch data engineering and analytics**.

---


## 🏗️ Architecture Diagram
Raw CSV → GCS (Raw Zone)
→ PySpark on Dataproc (Transform & Clean)
→ GCS (Processed Zone)
→ BigQuery (Analytics Warehouse)
→ Looker Studio (Visualization)
![Architecture Diagram](gcp_bold_pipeline_diagram.png)


---

## 🚀 Technologies Used

| Component | Tool |
|---------|------|
| Storage | Google Cloud Storage (GCS) |
| Processing | PySpark on Dataproc |
| Data Warehouse | BigQuery |
| Orchestration | Apache Airflow |
| Dashboard | Looker Studio |
| Language | Python & SQL |
| Version Control | Git & GitHub |

---

## 📌 Key Deliverables

- Automated end-to-end ETL pipeline
- PySpark transformation script processing **2.7M+ taxi records**
- Partitioned BigQuery tables for optimized cost & performance
- Looker Studio dashboard showing trip & fare insights

---

## 📊 Dashboard  
🔗 **Live Dashboard:**  
https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

---

## 📁 Repository Folder Structure

gcp-data-pipeline-project/
│
├── week1/ → Raw ingestion to GCS + BigQuery load
├── week2/ → Data cleaning + automated pipeline
├── week3/ → PySpark job on Dataproc + processed outputs
├── week4/ → Analytics & Dashboard
└── dags/ → Airflow workflow definitions


---

## 📝 BigQuery Views (Week 4)

| View | Description |
|------|-------------|
| trips_by_passenger | Avg fare grouped by passenger count |
| trips_over_time | Trips per day + daily averages |
| high_fare_trips | Trips with unusually large fare values |

---

## 🧠 Key Insights

- Avg fare remains stable for most rides, increases for groups of 7+
- More trips **do not necessarily mean higher average fare**
- Seasonal/time-based demand patterns are clearly visible

---


---

## Week 1 – Data Ingestion & Environment Setup

**Tasks Completed**
- Created GCP project and configured IAM authentication
- Uploaded NYC Taxi CSV dataset to **Google Cloud Storage (Raw Zone)**
- Loaded raw data into **BigQuery** using auto-detected schema
- Validated dataset structure using SQL queries

**Key Skills Practiced**
- Cloud Storage buckets
- BigQuery table creation
- Data validation & sanity checks
- Python + gcloud CLI

---

## Week 2 – Data Cleaning & Automated Pipeline

**Tasks Completed**
- Cleaned the raw dataset using **Pandas** (null handling, schema cleanup, type fixes)
- Re-uploaded clean data to **GCS (Processed Zone)**
- Loaded cleaned dataset into **BigQuery**
- Automated the ETL pipeline

**Key Skills Practiced**
- Pandas data wrangling
- ETL job scripting
- Automated workflows
- Data quality checks

---

## Week 3 – Distributed Processing with PySpark (Dataproc)

**Tasks Completed**
- Created a **Dataproc cluster** for scalable distributed processing
- Wrote and executed **PySpark** script to process 2.7M+ records
- Saved processed Parquet/CSV output to **GCS**
- Connected BigQuery to processed zone for analytics

**Key Skills Practiced**
- Spark DataFrames
- Cluster-based data processing
- Partitioning & performance optimization

---

## Week 4 – Analytics & Visualization (Looker Studio)

**Tasks Completed**
- Query optimization & partitioned tables in BigQuery
- Created analytical SQL views:
  - `trips_by_passenger`
  - `trips_over_time`
  - `high_fare_trips`
- Built a **Looker Studio dashboard** connected directly to BigQuery
- Designed visual insights, metrics, trends, and anomaly detection

**Dashboard Link**  
🔗 https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b
(week4_dashboard.png) 
(dashboard_nyc_taxi.png)

**Key Insights**
- Average fare trends remain stable across most passenger counts, rises sharply for large groups
- Demand spikes across certain dates do not correlate directly with fare spikes
- Time-based ride patterns confirm clear seasonal & behavioral fluctuations

---

---

### 📈 Dashboard Visualizations

| Chart | Description |
|------|-------------|
| Daily Revenue Trend | Revenue fluctuation over time |
| Avg Distance Trend | Average trip length by date |
| Top Pickup Locations | Most common pickup areas |
| Data Table | Cleaned dataset preview for validation |

---

### 🔍 Key Insights
- Over **2.8M+ trips** analyzed from NYC Yellow Taxi dataset
- Revenue and trip distance show seasonal trends
- Pickup hotspots are concentrated in key NYC transit + tourist zones
- Data pipeline enables **automatic dashboard refresh** as new data is ingested

---

## 🔗 Project Links

- **Looker Studio Dashboard**: https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b  
- **LinkedIn Post**: *[your post link]*  












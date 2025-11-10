## 🧠 Project Summary

This project demonstrates a complete end-to-end Data Engineering pipeline on Google Cloud:
- Data ingestion to Google Cloud Storage
- Transformation using Pandas & PySpark on Dataproc
- Warehouse loading and analytics in BigQuery
- Dashboard visualization in Looker Studio

This simulates real enterprise ETL workflows and showcases cloud data engineering skills.

------
## 🏗️ Architecture Diagram
![Architecture Diagram](gcp_bold_pipeline_diagram.png)

**Week 1 – Initial Setup & Data Loading**

**Tasks Completed:**

Set up a GCP free-tier project.

Created a Cloud Storage bucket for raw data.

Installed and configured gcloud CLI.

Wrote a Python script to upload CSV files to the bucket.

Loaded the data into BigQuery with auto-detected schema.

Ran a query to validate the data.

**Skills Practiced:**

Python (file handling, scripts)

GCP Authentication & CLI

Google Cloud Storage

BigQuery

SQL & Data Validation

Basic ETL (Extract → Load → Query)

**Files in Week 1:**

upload_to_bucket.py

sample_data.csv

README.md



--------------------------------------------

**Week 2 – Data Cleaning & Automated ETL Pipeline**

**Tasks Completed:**

Cleaned raw CSV data locally using Pandas (clean_data.py).

Uploaded cleaned data to Google Cloud Storage (upload_to_bucket.py).

Loaded cleaned data into BigQuery (cleaned_sample_table).

Automated the entire process using etl_pipeline.py (clean → upload).

**Skills Practiced:**

Python (Pandas, file I/O)

Google Cloud Storage

BigQuery

Data Cleaning & Transformation

ETL Pipeline Design & Automation

**Files in Week 2:**

clean_data.py

etl_pipeline.py

README.md (updated documentation)

--------------------------------------------------------



## Week 3 – Big Data Processing with PySpark on Dataproc

**Tasks Completed:**
- Created a Dataproc cluster to process large datasets using PySpark.
- Ran PySpark job to clean, transform, and aggregate trip data at scale.
- Wrote cleaned output back to Google Cloud Storage (`/week3/output/`).
- Defined schema, validated data types, and ensured no data loss.

**Skills Practiced:**
- PySpark (RDDs & DataFrame API)
- Google Cloud Dataproc (cluster provisioning and distributed jobs)
- Distributed data transformation and optimization
- Cloud Storage (Input / Output data paths)

**Key Script(s):**
- `process_big_data.py`

---


## Week 4 – Data Insights & Visualization 🎨📊

In Week 4, we analyzed and visualized the cleaned trip data loaded into BigQuery.

### ✅ Tasks Completed
- Loaded final PySpark output from GCS into BigQuery (`nyc_taxi_demo.trips_cleaned`)
- Wrote analytical SQL queries to generate aggregated insights
- Built a Looker Studio dashboard connected live to BigQuery
- Enabled auto-refresh based on Airflow pipeline updates

---

### 📊 Dashboard Preview

![NYC Taxi Dashboard](dashboard_nyc_taxi.png)

**Live Dashboard Link:**  
🔗 https://lookerstudio.google.com/reporting/9d456692-cd86-460e-9bbd-58e1bdc4413b

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

### 🗄️ Data Source









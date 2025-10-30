# GCP Data Pipeline Project

## Week 1 – Setup & Raw Data Upload
- Created a GCP project and Cloud Storage bucket
- Uploaded raw CSV files using Python
- Loaded data into BigQuery and validated
- Skills: Python, GCP, BigQuery, ETL, SQL

## Week 2 – Data Cleaning & Automation
- Implemented data cleaning using Pandas (removed missing rows, standardized column names)
- Automated uploading cleaned CSV to GCS
- Loaded cleaned data into BigQuery (`cleaned_sample_table`)
- Combined cleaning + upload in one script (`etl_pipeline.py`) for automation
- Skills: Python, Pandas, ETL, GCP, BigQuery, Automation

**Commands to run Week 2 pipeline:**
```bash
python etl_pipeline.py
# gcp-data-pipeline-project
Data engineering pipeline using Python and GCP (BigQuery + Cloud Storage)

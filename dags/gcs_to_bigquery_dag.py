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
        bucket="ruthvik-week3-bucket-2",   # <-- Change bucket name if needed
        prefix="",                         # "" means list everything
        gcp_conn_id="google_cloud_default"
    )

    load_to_bigquery = GCSToBigQueryOperator(
        task_id="load_to_bigquery",
        bucket="ruthvik-week3-bucket-2",   # <-- Same bucket
        source_objects=["week3/output/part-*.csv"],  # <-- File(s) in bucket
        destination_project_dataset_table="ruthvik-week3-dataproc.nyc_taxi_demo.trips",  
        write_disposition="WRITE_TRUNCATE",
        source_format="CSV",
        skip_leading_rows=1,
        autodetect=True,
        gcp_conn_id="google_cloud_default",
    )

    list_gcs_files >> load_to_bigquery

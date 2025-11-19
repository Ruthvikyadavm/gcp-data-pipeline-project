import pandas as pd
from google.cloud import storage

def clean_data():
    """
    Read raw CSV, clean it, and save as cleaned_data.csv
    """
    df = pd.read_csv("sample_data.csv")
    df = df.dropna()  # remove rows with missing values
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    df.to_csv("cleaned_data.csv", index=False)
    print("✅ Data cleaned and saved as cleaned_data.csv")

def upload_to_gcs(bucket_name, file_name):
    """
    Upload the file to Google Cloud Storage
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"data/{file_name}")
    blob.upload_from_filename(file_name)
    print(f"✅ Uploaded {file_name} to GCS")

if __name__ == "__main__":
    clean_data()
    upload_to_gcs("ruthvik-data-pipeline-bucket", "cleaned_data.csv")

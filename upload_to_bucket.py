from google.cloud import storage

def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(f"✅ File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    bucket_name = "ruthvik-data-pipeline-bucket"  # 👈 Replace this
    source_file_name = "sample_data.csv"
    destination_blob_name = "data/sample_data.csv"

    upload_to_bucket(bucket_name, source_file_name, destination_blob_name)

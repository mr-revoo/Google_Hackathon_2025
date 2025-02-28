import os
from google.cloud import bigquery

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/youssef/Desktop/GDG/startups-452221-a288712043d0.json"

client = bigquery.Client()

dataset_id = "startups-452221.america_dataset"
table_id = f"{dataset_id}.investment"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

with open("cleaned_investments_VC.csv", "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete
print(f"Loaded {job.output_rows} rows into {table_id}.")
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()
query = """
SELECT *
FROM your_project_id.your_dataset.enriched_customer_data
"""
df = client.query(query).to_dataframe()

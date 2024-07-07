batch_prediction_job = aiplatform.BatchPredictionJob.create(
    job_display_name='batch_prediction',
    model_name=model.resource_name,
    instances_format='bigquery',
    bigquery_source=f'bq://{your_project_id}.{your_dataset}.new_data_to_predict',
    predictions_format='bigquery',
    bigquery_destination_prefix=f'bq://{your_project_id}.{your_dataset}.predictions',
)

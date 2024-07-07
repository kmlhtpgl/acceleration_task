from google.cloud import aiplatform

aiplatform.init(project='your_project_id', location='your_region')

job = aiplatform.CustomTrainingJob(
    display_name='propensity_model_training',
    script_path='train_model.py',  # Your training script
    container_uri='gcr.io/cloud-aiplatform/training/tf-cpu.2-3:latest',
)

job.run(
    replica_count=1,
    model_display_name='propensity_model',
    args=['--dataset', 'your_dataset.processed_data', '--model_output', 'gs://your_bucket/models/']
)

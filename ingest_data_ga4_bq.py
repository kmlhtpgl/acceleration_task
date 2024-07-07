import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(
    project='your_project_id',
    temp_location='gs://your_bucket/temp',
    region='your_region'
)

def transform(element):
    # Transformation logic here
    return element

with beam.Pipeline(options=options) as p:
    (p
     | 'Read from GA4' >> beam.io.ReadFromText('path_to_your_google_analytics_data')
     | 'Transform Data' >> beam.Map(transform)
     | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
         'your_project_id:your_dataset.your_table',
         schema='SCHEMA_AUTODETECT'
     ))

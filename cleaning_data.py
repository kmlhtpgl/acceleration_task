def preprocess(element):
    # Preprocessing logic here
    return element

with beam.Pipeline(options=options) as p:
    (p
     | 'Read Raw Data' >> beam.io.ReadFromBigQuery(query='SELECT * FROM your_dataset.raw_data')
     | 'Preprocess Data' >> beam.Map(preprocess)
     | 'Write Processed Data' >> beam.io.WriteToBigQuery(
         'your_project_id:your_dataset.processed_data',
         schema='SCHEMA_AUTODETECT'
     ))

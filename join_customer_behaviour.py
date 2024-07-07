def enrich(element):
    # Enrichment logic here
    return element

with beam.Pipeline(options=options) as p:
    (p
     | 'Read Customer Data' >> beam.io.ReadFromBigQuery(query='SELECT * FROM your_dataset.customer_data')
     | 'Read Behavior Data' >> beam.io.ReadFromBigQuery(query='SELECT * FROM your_dataset.behavior_data')
     | 'Join and Enrich Data' >> beam.Map(enrich)
     | 'Write Enriched Data' >> beam.io.WriteToBigQuery(
         'your_project_id:your_dataset.enriched_data',
         schema='SCHEMA_AUTODETECT'
     ))

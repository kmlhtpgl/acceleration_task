import requests

def transfer_to_crm(element):
    crm_api_url = 'https://your-crm.com/api/endpoint'
    headers = {'Authorization': 'Bearer YOUR_API_TOKEN', 'Content-Type': 'application/json'}
    response = requests.post(crm_api_url, headers=headers, json=element)
    if response.status_code != 200:
        logging.error(f"Failed to send data for user_id {element['user_id']}")
    return element

with beam.Pipeline(options=options) as p:
    (p
     | 'Read Propensity Scores' >> beam.io.ReadFromBigQuery(query='SELECT * FROM your_dataset.propensity_scores')
     | 'Transfer to CRM' >> beam.Map(transfer_to_crm))

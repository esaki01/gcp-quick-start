from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials


credentials = GoogleCredentials.get_application_default()
service = build('dataflow', 'v1b3', credentials=credentials)

# Set the following variables to your values.
JOBNAME = 'myjob'
PROJECT = 'dataflow-reference'
BUCKET = 'dataflow-reference'
TEMPLATE = 'template'

GCSPATH = "gs://dataflow-reference/template".format(bucket=BUCKET, template=TEMPLATE)
BODY = {
    "jobName": "{jobname}".format(jobname=JOBNAME),
    "parameters": {
        "suffix": "?",
    },
    "environment": {
        "tempLocation": "gs://{bucket}/tmp".format(bucket=BUCKET),
        "zone": "us-central1-f"
    }
}

request = service.projects().templates().launch(projectId=PROJECT, gcsPath=GCSPATH, body=BODY)
response = request.execute()

print(response)

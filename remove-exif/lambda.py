import boto3

s3 = boto3.resource('s3')

def handler(event, context):
    print(event)
    key = event['Records'][0]['s3']['object']['key']
    source = {
    'Bucket': 'graveend-terraform-example-input',
    'Key': key
    }
    s3.meta.client.copy(source, "graveend-terraform-example-output", key + "-modified")
    return {
        'statusCode' : 200
    }
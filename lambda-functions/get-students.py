import boto3
from botocore.exceptions import ClientError

import json

def lambda_handler(event, context):
    dynamodb_response, success = get_students()
    if success:
        data = {
            'items': dynamodb_response['Items']
        }
        return data
    else:
        return dynamodb_response

def get_dynamodb_resource():
    return boto3.resource(
        'dynamodb',
        region_name='us-east-2',
    )

def get_students():
    client = get_dynamodb_resource()
    try:
        table = client.Table('student')
        response = table.scan()
        return response, True
    except ClientError as e:
        return bad_request('No se pudo obtener estudiantes'), False
    
def bad_request(message):
    response = {
        'status_code': 400,
        'message': message
    }
    return response
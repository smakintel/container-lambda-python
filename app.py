import awsgi
import json
import os
from pprint import pprint
import boto3
from botocore.vendored import requests
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from flask import (
    Flask,
    jsonify,
)

app = Flask(__name__)
region = os.environ['AWS_REGION']

@app.route('/')
def index():
    return jsonify(status=200, message='OK')


@app.route('/register')
def register():
    ddbClient = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = ddbClient.Table('maiderp_academy_users')

    print(event)
    event_body = json.loads(event["body"])
    
    email=event_body["email"]
    registerDate=event_body["registerDate"]
    name=event_body["name"]
    mobile=event_body["mobile"]
    password=event_body["password"]

    try:

        response = table.put_item(
           Item={
                'registerDate': registerDate,
                'name': name,
                'email': email,
                'mobile': mobile,
                'password': password
         
            }
        )
        

        return {"statusCode": 200,"body": json.dumps(response),"isBase64Encoded":"false","headers": { "Access-Control-Allow-Origin" : "*", "Access-Control-Allow-Credentials" : "true" } }

    except ClientError as e:
        print("Here")
        print(e)
        return {"statusCode": 500,"body": json.dumps("error"),"isBase64Encoded":"false","headers": { "Access-Control-Allow-Origin" : "*", "Access-Control-Allow-Credentials" : "true" } }


@app.route('/kava/test')
def kava():
    return jsonify(status=200, message='Kava test')

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
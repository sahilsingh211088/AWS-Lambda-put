{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
import boto3\
import logging\
\
logger = logging.getLogger()\
logger.setLevel(logging.INFO)\
\
def lambda_handler(event, context):\
    # TODO implement\
    eventJson = json.dumps(event)\
    logging.info("Event variable: " + eventJson)\
   \
    eventPythonObject = json.loads(eventJson)\
    record = eventPythonObject['Records'][0]\
   \
    bucket = record['s3']['bucket']['name']\
    key = record['s3']['object']['key']\
    size = record['s3']['object']['size']\
   \
    s3 = boto3.resource('s3')\
    copy_source = \{\
        'Bucket': bucket,\
        'Key': key\
    \}\
   \
    if size > 50 :\
        s3.meta.client.copy(copy_source, 'freewheel-historical-data-cleaned', key)\
       \
    return \{\
        'statusCode': 200,\
        'body': json.dumps('Hello from Lambda!')\
    \}}
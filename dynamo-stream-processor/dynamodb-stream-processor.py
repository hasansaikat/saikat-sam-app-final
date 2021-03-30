import json
import os
import boto3


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "test hello world",

        }),
    }

import json
import os
import boto3
import uuid
s3 = boto3.client('s3')
client = boto3.client('dynamodb')

bucket_name = "saikats3bucketfinalassignment"


def lambda_handler(event, context):

    data = json.loads(event['body'])

    print(data)
    keys = list(data)
    project_name = keys[0]  # project name
    p_name = data[project_name]
    key = keys[1:]  # input value keys
    print(key)

    DBtable = os.environ['AppTable']


    item_en = {}
    item_fr = {}
    item_cn = {}

    for i in key:
        try:
            if "first_name" == i:
                # id = uuid.uuid4().hex
                item_en['pk'] = {'S': p_name}
                item_en['sk'] = {'S': 'en'}
                item_en['gsipk'] = {'S': p_name}
                item_en['gsisk'] = {'S': p_name + "_en"}
                item_en[i] = {'S': data[i]}
                response = client.put_item(
                    TableName=DBtable,
                    Item=item_en
                )

            if "Prénom" == i:
                # id = uuid.uuid4().hex
                item_fr['pk'] = {'S': p_name}
                item_fr['sk'] = {'S': 'fr'}
                item_fr['gsipk'] = {'S': p_name}
                item_fr['gsisk'] = {'S': p_name + "_fr"}
                item_fr[i] = {'S': data[i]}
                response = client.put_item(
                    TableName=DBtable,
                    Item=item_fr
                )

            if "名" == i:
                # id = uuid.uuid4().hex
                item_cn['pk'] = {'S': p_name}
                item_cn['sk'] = {'S': 'cn'}
                item_cn['gsipk'] = {'S': p_name}
                item_cn['gsisk'] = {'S': p_name + "_cn"}
                item_cn[i] = {'S': data[i]}
                response = client.put_item(
                    TableName=DBtable,
                    Item=item_cn
                )

        except IndexError as e:
            print(e)

    directory_name = p_name  # it's name of your folders
    s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "hello world",

        }),
    }

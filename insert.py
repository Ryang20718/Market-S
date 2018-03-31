from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

def insert():
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if o % 1 > 0:
                    return float(o)
                else:
                    return int(o)
    return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')

table = dynamodb.Table('Swipes') # table 


'''
response = table.put_item(
   Item={
        'Location': "totalCount",
        'totalNum': 1
    }
)
'''



response = table.update_item(
    Key={
        'Location': "totalCount",
    },
    UpdateExpression="set totalNum = totalNum + :val",
    ExpressionAttributeValues={
        ':val': 1
    },
    ReturnValues="UPDATED_NEW"
)

numItems = 0;

response = table.query(
    KeyConditionExpression=Key('Location').eq("totalCount") 
)

for i in response['Items']:
    numItems = (i['totalNum'])

convertedNumItems = str(numItems)   


response = table.put_item(
   Item={
        'Location': "Bplato" + convertedNumItems,
        'info': {
            'price': 5,
            'quantity': 3,
            'timee': "3-4"
        }
    }
)



print("PutItem succeeded:")
#print(json.dumps(response, indent=4, cls=DecimalEncoder))



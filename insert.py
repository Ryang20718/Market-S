from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

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

table = dynamodb.Table('Swipes')

response = table.put_item(
   Item={
        'Location': "location",
        'info': {
            'price': 4,
            'quantity': 3,
            'timee': "3-4"
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))



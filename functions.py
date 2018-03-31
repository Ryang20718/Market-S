from __future__ import print_function # Python 2/3 compatibility
import boto3
from botocore.exceptions import ClientError
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
def eraseItem(m_key):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table = dynamodb.Table('Swipes')
    
    
    print("Attempting a conditional delete...")
    
    try:
        response = table.delete_item(
            Key={
                'Location': m_key
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("DeleteItem succeeded:")
    
    return    
        
        
def insertOrUpdate(m_key, m_price , m_quantity, m_timee , m_location):
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    table = dynamodb.Table('Swipes') # table 
    
    
    #updates totalNumber of items
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
    
    numItems = 0
    #get the current count of items
    response = table.query(
        KeyConditionExpression=Key('Location').eq('totalCount') 
    )
    
    for i in response['Items']:
        numItems = (i['totalNum'])
    
    convertedNumItems = str(numItems)   
    
    #inserting the new item with the new items
    response = table.put_item(
       Item={
            'Location': m_location + convertedNumItems,
            'info': {
                'price': m_price,
                'quantity': m_quantity,
                'timee': m_timee
            }
        }
    )
    
    print("PutItem succeeded:")
    return



def getItem(m_key):
    dynamodb = boto3.resource("dynamodb", region_name='us-west-1')
    
    table = dynamodb.Table('Swipes')
    
    try:
        response = table.get_item(
            Key={
                'Location': m_key
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
    return item #returns json Item



def queryByKey(m_key):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table = dynamodb.Table('Swipes')
    
    
    response = table.query(
       #FilterExpression=Attr('info.timee').contains("3"),  #can use this for filtering strings
        #FilterExpression=Attr('info.price').eq(4),
        KeyConditionExpression=Key('Location').eq(m_key) 
    )
    
    for i in response['Items']:
        print(i['info'])
    return    
        
        
def queryByAttributes(m_key, m_price, m_timee, m_quantity):#query by attributes
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    
    table = dynamodb.Table('Swipes')
    
    
    response = table.query(
       FilterExpression=Attr('info.timee').contains(m_timee),  #can use this for filtering strings
        FilterExpression=Attr('info.price').eq(m_price),
        FilterExpression=Attr('info.quantity').eq(m_quantity),
        KeyConditionExpression=Key('Location').eq(m_key) 
    )
    
    for i in response['Items']:
        print(i['info'])







#MAIN
def main():
    #insertOrUpdate("Bplato",5,1,"3-9","Bplato")
    #eraseItem("Bplato11")
    #getItem("Bplato12")
    #query("Bplato12")

main()
import boto3
import json
import os


def lambda_handler(event, context):
    '''API Gateway Integration Function to perform CRUD operations on DynamoDB table.'''
    print(event)
    dynamodb = boto3.resource("dynamodb")
    table_name = os.environ["TABLE"]
    table = dynamodb.Table(table_name)
    
    # Extract HTTP Method from event
    operation = event["requestContext"]["http"]["method"]
    
    # success and error response
    error_response = {
        "statusCode": 400,
        "body": json.dumps("Invalid Input.")
    }
    success_response = {
        "statusCode": 200,
        "body": json.dumps("")
    }
    
    # interaction with DynamoDB
    response = {}
    if operation == "GET":
        postID = event["pathParameters"]["postID"]
        response = table.get_item(Key = {"postID": postID})
    elif operation in ["POST", "PUT"]:
        item = json.loads(event["body"])
        response = table.put_item(Item = item)
    elif operation == "DELETE":
        postID = event["pathParameters"]["postID"]
        response = table.delete_item(Key = {"postID": postID}, ReturnValues='ALL_OLD')
    else:
        return error_response
    
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        success_response["body"] = json.dumps(response)
        return success_response
    else:
        error_response["body"] = json.dumps("A DynamoDB error occurred.")
        return error_response
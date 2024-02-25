import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd

# low level
client = boto3.client('dynamodb')
table_name = 'Employee'

# item_mariok = {
#     'LoginAlias':{'S':'mariok'},
#     'FirstName':{'S':'Mario'},
#     'LastName':{'S':'Kauer'}
# }
    
# resp = client.put_item(TableName = table_name, Item = item_mariok)

# with open("dynamodbemployees.csv", "r") as file:
#     lines = file.readlines()

# first_column =  []

# for i in lines:
#     parts = i.split(",")
#     loginalias = parts[0]
#     first_column.append(loginalias)
    
# second_column =  []

# for i in lines:
#     parts = i.split(",")
#     firstname = parts[1]
#     second_column.append(firstname)

# third_column =  []

# for i in lines:
#     parts = i.split(",")
#     lastname = parts[2]
#     third_column.append(lastname)

# fourth_column =  []

# for i in lines:
#     parts = i.split(",")
#     managerloginalias = parts[3]
#     fourth_column.append(managerloginalias)

# item_1 = {"LoginAlias":first_column[1],"FirstName":second_column[1],"LastName":third_column[1],"ManagerLoginAlias":fourth_column[1]}
# item_2 = {"LoginAlias":first_column[2],"FirstName":second_column[2],"LastName":third_column[2],"ManagerLoginAlias":fourth_column[2]}
# item_3 = {"LoginAlias":first_column[3],"FirstName":second_column[3],"LastName":third_column[3],"ManagerLoginAlias":fourth_column[3]}

# items_to_add = [item_1, item_2, item_3]

# table = dynamodb.Table('Employee')

# with table.batch_writer() as batch:
#     for item in items_to_add:
#         response = batch.put_item(Item={
#             "LoginAlias": item["LoginAlias"],
#             "FirstName": item["FirstName"],
#             "LastName": item["LastName"],
#             "ManagerLoginAlias": item["ManagerLoginAlias"]
#         })
#_________________________________________________________________

# high level

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee')

# employees = pd.read_csv("dynamodbemployees.csv")

# with table.batch_writer() as batch:
#     for index, row in employees.iterrows():
#         content = {
#             'LoginAlias': row['LoginAlias'],
#             'FirstName': row['FirstName'],
#             'LastName': row['LastName'],
#             'ManagerLoginAlias': row['ManagerLoginAlias']
#         }
#         batch.put_item(Item=content)

# 1. Operation - Lasse dir alle Einträge in der Tabelle mit der Scan Operation anzeigen.

# response = table.scan()
# items = response['Items']
# print(items)

# PartiQL statement
# response_scan = client.execute_statement(Statement='SELECT * FROM Employee')
# print(response_scan)

# 2. Operation - Gib alle Informationen über den Nutzer mit dem LoginAlias “carolinh” aus.

# response = table.get_item(
#     Key = {'LoginAlias': 'carolinh'}
#         )
# print(response)

# PartiQL statement
# response_carolin = client.execute_statement(Statement='SELECT * FROM Employee WHERE LoginAlias = \'carolinh\'')
# print(response_carolin)

# 3. Operation - Lasse dir alle Vornamen der Angestellen zurückgeben, die von “johns” gemanagt werden.

# response = table.query(
#     IndexName='ManagerLoginAlias-index',
#     KeyConditionExpression=Key('ManagerLoginAlias').eq('johns'),
#     ProjectionExpression="FirstName" # ProjectionExpression="FirstName" im query würde eine FOR-Schleife ersetzen!   
#     )

# for item in items:
#     print(item["FirstName"])
# print(response['Items'])
   
# PartiQL statement    
# response_manager = client.execute_statement(Statement='SELECT FirstName FROM Employee WHERE ManagerLoginAlias = \'johns\'')
# print(response_manager)

# 4. Operation - Füge einen neue Mitarbeiterin Sarah Klein hinzu. Sarah’s Login ist sarahk, sie berichtet an Martha Rivera und kennt sich gut mit “software” aus.

# response = table.put_item(
#     Item={'LoginAlias': 'sarahk', 'FirstName': 'Sarah', 'LastName': 'Klein', 'ManagerLoginAlias': 'marthar', 'Skills': '{"software"}'},
#     )

# PartiQL statement
# https://aws-dojo.com/excercises/excercise29/
# sarahk = {
#     "LoginAlias": "sarahk",
#     "FirstName": "Sarah",
#     "LastName": "Klein",
#     "ManagerLoginAlias": "marthar",
#     "Skills": {"software"} # string set
# }

# response_sarah = client.execute_statement(Statement=f'INSERT INTO Employee VALUE {sarahk}'.replace("{'software'}","<<'software'>>"))

# 5. Operation - Passe den Eintrag von Mateo an und füge als Skill nun auch “operations” hinzu.

# https://www.youtube.com/watch?v=9TKOsWiAh8w
# response = table.update_item(
#     Key = {'LoginAlias': 'mateoj'},
#     UpdateExpression='ADD Skills :a',
#     ExpressionAttributeValues={':a': {"operations"}},
#     ReturnValues='UPDATED_NEW'
#     )
# print(response['Attributes'])

# PartiQL statement    
# response_update = client.execute_statement(Statement='UPDATE Employee SET Skills =set_add(Skills, <<\'operations\'>>) WHERE LoginAlias = \'mateoj\'')
# print(response_update) 
# another_update = client.execute_statement(Statement='UPDATE Employee set Skills =set_add(Skills, <<\'sql\'>>) where LoginAlias=\'mateoj\'')
# print(another_update)
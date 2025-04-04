import boto3
import time
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Attr

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserLogins')

# Sample user data
sample_users = [
    {
        'UserID': 'user1',
        'Timestamp': int(time.time()),
        'Name': 'Alice Johnson',
        'Email': 'alice@example.com',
        'LastLogin': datetime.now().isoformat()
    },
    {
        'UserID': 'user2',
        'Timestamp': int((datetime.now() - timedelta(days=3)).timestamp()),
        'Name': 'Bob Smith',
        'Email': 'bob@example.com',
        'LastLogin': (datetime.now() - timedelta(days=3)).isoformat()
    },
    {
        'UserID': 'user3',
        'Timestamp': int((datetime.now() - timedelta(days=10)).timestamp()),
        'Name': 'Carol Lee',
        'Email': 'carol@example.com',
        'LastLogin': (datetime.now() - timedelta(days=10)).isoformat()
    }
]

# Insert data
for user in sample_users:
    table.put_item(Item=user)

print("Sample data inserted.")

# Query: users who logged in within the last 7 days
seven_days_ago = int((datetime.now() - timedelta(days=7)).timestamp())

response = table.scan(
    FilterExpression=Attr('Timestamp').gt(seven_days_ago)
)

print("\nUsers who logged in within the last 7 days:")
for item in response['Items']:
    print(item)


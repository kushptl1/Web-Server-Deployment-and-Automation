import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # use your preferred region

# Create table
table = dynamodb.create_table(
    TableName='UserLogins',
    KeySchema=[
        {'AttributeName': 'UserID', 'KeyType': 'HASH'},  # Partition key
        {'AttributeName': 'Timestamp', 'KeyType': 'RANGE'}  # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'UserID', 'AttributeType': 'S'},
        {'AttributeName': 'Timestamp', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Creating table...")
table.wait_until_exists()
print("Table status:", table.table_status)


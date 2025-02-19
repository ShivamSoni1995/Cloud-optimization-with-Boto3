import boto3
import zipfile

lambda_client = boto3.client('lambda')

# Create ZIP package
with zipfile.ZipFile('lambda_function.zip', 'w') as z:
    z.write('lambda_function.py')

# Upload Lambda function
with open('lambda_function.zip', 'rb') as f:
    response = lambda_client.create_function(
        FunctionName='MyLambdaFunction',
        Runtime='python3.8',
        Role='arn:aws:iam::123456789012:role/lambda-role',  # Replace with your IAM role ARN
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': f.read()}
    )

print("Lambda Function ARN:", response['FunctionArn'])

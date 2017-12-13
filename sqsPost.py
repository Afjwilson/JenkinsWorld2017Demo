#!/usr/bin/python

access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']

aws_message = "{\n The Access Key ID is: " + access_key + ",\n   The Secret Access Key is: " + secret_key + "\n}"
print aws_message

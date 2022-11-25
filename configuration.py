#!/usr/bin/python2.7
import ConfigParser
import os
import sys
from os.path import expanduser

config = ConfigParser.RawConfigParser()

# credentials_file: The file where this script will grab the temp creds
credentials_file = '/.aws/credentials'
home = expanduser("~")
credentials_file = home + credentials_file
config.read(credentials_file)

# Get the profile name to grab the credentials
profile = raw_input('Profile: ')
print ''

# Get the credentials from the file
access_key = config.get(profile, 'aws_access_key_id')
secret_key = config.get(profile, 'aws_secret_access_key')
session_token = config.get(profile, 'aws_session_token')

print('export AWS_ACCESS_KEY_ID=' + 'AKIAYVP4CIPPPXVIJFF6')
print('export SECRET_ACCESS_KEY=' + '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')
print('export SESSION_TOKEN=' + session_token)


output = json
region = us-east-2

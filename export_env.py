#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='Read in AWS credentials and export them to the env')

parser.add_argument('--access_id', help='Enter the AWS key necessary for this instance to have')
parser.add_argument('--secret', help='Enter the AWS secret necessary for this instance to have')
parser.add_argument('--export', help='Export the access ID and secret to a given file')

args = parser.parse_args()

combined_access_info = []

AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID={}; export AWS_ACCESS_KEY_ID'.format(args.access_id)
AWS_SECRET_KEY = 'AWS_SECRET_KEY={}; export AWS_SECRET_KEY'.format(args.secret)

combined_access_info.append(AWS_ACCESS_KEY_ID)
combined_access_info.append(AWS_SECRET_KEY)

for i in combined_access_info:
    print i

if os.path.exists(args.export) is True:
    with open(args.export, 'a') as f_output:
        for i in combined_access_info:
            f_output.write(i)
            f_output.write('\n')

    # print 'Path exists'
else:
    print 'Filename invalid, please make sure the file to be written exists'

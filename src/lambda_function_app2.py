#*******************************************************************************
#lambda_function_app2.py
#*******************************************************************************

#Purpose:
#Basic usage of AWS lambda and s3 storage.
#Authors:
#Cedric H. David, 2018-2024
#Manu Tom, 2023-2024

#*******************************************************************************
#Python libraries
#*******************************************************************************
import boto3


#*******************************************************************************
#lambda handler
#*******************************************************************************
def lambda_handler(event, context):
    S3_BUCKET = event['S3_BUCKET_NAME']
    FILENAME_UPLD = event['FILENAME_UPLOAD']
    FILENAME_DWNLD = event['FILENAME_DOWNLOAD']
	
    #s3 bucket interface
    s3 = boto3.resource('s3')
    
    #sample upload and download 
    s3.Bucket(S3_BUCKET).upload_file(FILENAME_UPLD, FILENAME_UPLD)
    s3.Bucket(S3_BUCKET).download_file(FILENAME_UPLD, FILENAME_DWNLD)

    message  = 'Uploaded the file <{}> to S3 bucket <{}> and downloaded the same as <{}> to </var/task>'.format(event['FILENAME_UPLOAD'], event['S3_BUCKET_NAME'], event['FILENAME_DOWNLOAD'])
    return { 
        'Success' : message
    }


#*******************************************************************************
#End
#*******************************************************************************

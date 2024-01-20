#*******************************************************************************
#lambda_function_app3.py
#*******************************************************************************

#Purpose:
#Basic usage of a python driver (with AWS lambda and s3 storage).
#Authors:
#Cedric H. David, 2018-2024
#Manu Tom, 2023-2024

#*******************************************************************************
#Python libraries
#*******************************************************************************
import mock_drv as drv


#*******************************************************************************
#lambda handler
#*******************************************************************************
def lambda_handler(event, context):
    #***************************************************************************
    #input parameters as events
    #***************************************************************************
    #s3 bucket
    S3_BUCKET = event['S3_BUCKET_NAME']
    
    #for file upload and download ( /var/task <--> s3 )
    FILENAME_UPLD = event['FILENAME_UPLOAD']
    FILENAME_DWNLD = event['FILENAME_DOWNLOAD']
    
    #for file upload to s3 from URL
    FILE_URL = event['FILE_URL']
	
    
    #***************************************************************************
    #invoke drivers
    #*************************************************************************** 
    #driver to upload a file from /var/task to s3 bucket
    drv.drv_upld(S3_BUCKET, FILENAME_UPLD)
    
    #driver to download a file from s3 bucket to /var/task
    drv.drv_dwnld(S3_BUCKET, FILENAME_UPLD, FILENAME_DWNLD)
    
    #driver to upload a file from URL to s3 bucket
    drv.drv_upld_from_url(S3_BUCKET, FILE_URL)

    message  = 'successful'

    return { 
        'Upload and Download' : message
    }


#*******************************************************************************
#End
#*******************************************************************************

#!/usr/bin/env python3
#*******************************************************************************
#mock_drv.py
#*******************************************************************************

#Purpose:
#This program will mock some upload and download (python) drivers.
#Authors:
#Cedric H. David, 2023-2024
#Manu Tom, 2023-2024


#*******************************************************************************
#Import Python modules
#*******************************************************************************
import boto3
import requests


#*******************************************************************************
#AWS s3 bucket interface
#*******************************************************************************
s3_res = boto3.resource('s3')


#*******************************************************************************
#Driver for uploading from/var/task to s3
#*******************************************************************************
def drv_upld(s3_bucket_name, fn_upld):
     print('Driver for uploading to s3 bucket')

     #sample upload 
     s3_res.Bucket(s3_bucket_name).upload_file(fn_upld, fn_upld)


#*******************************************************************************
#Driver for downloading to /var/task from s3
#*******************************************************************************
def drv_dwnld(s3_bucket_name, fn_in_s3, fn_local):
     print('Driver for downloading from s3 bucket')

     #sample download 
     s3_res.Bucket(s3_bucket_name).download_file(fn_in_s3, fn_local)


#*******************************************************************************
#Driver for uploading a file from a URL to s3
#*******************************************************************************
def drv_upld_from_url(s3_bucket_name, url_inp):
     print('Driver for uploading a file from a url to s3 bucket')
     
     #request file from url
     url_req = requests.get(url_inp, stream=True).raw

     #extract filename from url
     url_filename = url_inp.split('/')[-1]

     #upload to s3 bucket
     s3_res.Bucket(s3_bucket_name).upload_fileobj(url_req, url_filename)


#*******************************************************************************
#End
#*******************************************************************************

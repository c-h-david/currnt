#*******************************************************************************
#lambda_function_app2.py
#*******************************************************************************

#Purpose:
#Basic usage of a python driver to print basin ID.
#Authors:
#Manu Tom, Cedric H. David, 2018-2024


#*******************************************************************************
#Example invocation
#*******************************************************************************
#{
#     "basin_id": "74",
#     "lsm_mod": "VIC"
#     "yyyy_mm": "2000-01"
#     "s3_name": "currnt-data"
#}


#*******************************************************************************
#Import libraries
#*******************************************************************************
import drv_all as drv


#*******************************************************************************
#lambda handler
#*******************************************************************************
def lambda_handler(event, context):
    message = event['basin_id']
    
    #***************************************************************************
    #invoke driver
    #*************************************************************************** 
    drv.drv_hel(message)
    
    return { 
        'message' : message
    }


#*******************************************************************************
#End
#*******************************************************************************

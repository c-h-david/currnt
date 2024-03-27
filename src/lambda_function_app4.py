#*******************************************************************************
#lambda_function_app4.py
#*******************************************************************************

#Purpose:
#Basic usage of NSIDC Earthaccess library (with AWS lambda) for LDAS download.
#Authors:
#Manu Tom, Cedric H. David, 2018-2024


#*******************************************************************************
#Example invocation
#*******************************************************************************
#{
#     "LSMexp": "GLDAS",
#     "LSM": "VIC"
#     "LSMres": "3H"
#     "month": "2000-01"


#*******************************************************************************
#Options supported
#*******************************************************************************
#     "LSMexp": "GLDAS", "NLDAS"
#     "LSM": "VIC"
#     "LSMres": "3H" and "M" (GLDAS), "H" and "M" (NLDAS)
#     "month": 2000-01 till 2023-12 (GLDAS, ongoing data production),
#              1979-01 till 2024-03 (NLDAS, ongoing data production)


#*******************************************************************************
#Python libraries
#*******************************************************************************
import os, subprocess, earthaccess


#*******************************************************************************
#lambda handler
#*******************************************************************************
def lambda_handler(event, context):
    #***************************************************************************
    #earth access parameters from input events
    #***************************************************************************
    
    if(event['LSMexp']=="GLDAS"):
        spatial_res = "10"
        boundingBox = (-180,-60,180,90)    
    elif(event['LSMexp']=="NLDAS"):
        spatial_res = "0125"
        boundingBox = (-125,25,-67,53)
    else:
        print("error: invalid LSM")

    date_beg = event['month']+"-01T00:00:00"# eg. "2000-01-01T00:00:00"
    date_end = date_beg.split("-")[0]+"-"+str(int(date_beg.split("-")[1])+1).zfill(2)# eg. "2000-02-01T00:00:00"
    
    #***************************************************************************
    #search for LDAS data
    #***************************************************************************
    results = earthaccess.search_data(
        short_name = event['LSMexp']+"_"+event['LSM']+spatial_res+"_"+event['LSMres'],
        cloud_hosted=True,
        bounding_box=boundingBox,
        temporal=(date_beg, date_end),
        count=10 # parameter to download the first X files in the list
        )
    
    #***************************************************************************
    #make folder, download LDAS files, list files
    #***************************************************************************
    dwnld_fldr = "/tmp"
    if not os.path.exists(dwnld_fldr):
        os.makedirs(dwnld_fldr)
    files = earthaccess.download(results, dwnld_fldr)
    print("Files downloaded: ", files)
    
    #***************************************************************************
    #check downloaded files
    #***************************************************************************
    result_chk_dwnld = subprocess.run(["ls", "-lR", "/tmp"], capture_output=True, text=True)
    print("Checking downloaded folder contents:\n", result_chk_dwnld.stdout)
    
    message  = ' {} {} {} {}'.format(event['LSMexp'], event['LSM'], event['LSMres'], event['month'])    

    return { 
        #'Upload and Download' : message
	'Download from Earthaccess library succesful for ' : message
    }


#*******************************************************************************
#End
#*******************************************************************************

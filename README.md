# CURRNT
The Combined Utilities for River Routing Nested Together (CURRNT) is designed to
simplify the execution of the Routing Application for Parallel computatIon of 
Discharge (RAPID) and the Reproducible Routing Rituals (RRR) on Amazon Web
Services (AWS).

## Local execution
Download CURRNT:

```
git clone https://github.com/c-h-david/currnt
```

Enter the CURRNT directory:

```
cd currnt/
```

Create Docker image:

```
docker build -t chdavid/currnt:app0 -f Dockerfile_app0 .
```

Execute Docker image as a Docker container:

```
docker run --rm -p 9000:8080 chdavid/currnt:app0
docker run -e AWS_ACCESS_KEY_ID="yourKeyID" -e AWS_SECRET_ACCESS_KEY="yourSecretAccessKey" --rm -p 9000:8080 chdavid/currnt:app2
docker run -e EARTHDATA_USERNAME="yourEarthDataUserName" -e EARTHDATA_PASSWORD="yourEarthDataPassword" --rm -p 9000:8080 currnt:app4
```

> The `--rm` option deletes the container after execution. The `-p 9000:8080`
> option maps Transmission Control Protocol (TCP) ports. In this case, the
> `8080` port in the Docker container is mapped to the `9000` port in the Docker
> host.

Try it out:

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"basin_id":"74", "lsm_mod":"VIC", "s3_name":"currnt-data", "yyyy_mm":"2000-01"}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"S3_BUCKET_NAME":"yourBucketName", "FILENAME_UPLOAD":"inputs.txt", "FILENAME_DOWNLOAD":"yourFilename.txt"}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"S3_BUCKET_NAME":"yourBucketName", "FILENAME_UPLOAD":"lambda_function_app3.py", "FILENAME_DOWNLOAD":"yourFilename.py", "FILE_URL":"https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg"}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"LSMexp":"GLDAS", "LSM":"VIC", "LSMres":"3H", "month":"2001-01"}'
```

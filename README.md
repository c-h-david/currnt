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
```

> The `--rm` option deletes the container after execution. The `-p 9000:8080`
> option maps Transmission Control Protocol (TCP) ports. In this case, the
> `8080` port in the Docker container is mapped to the `9000` port in the Docker
> host.

Try it out:

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"LSM":"VIC"}'
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"S3_BUCKET_NAME":"yourBucketName", "FILENAME_UPLOAD":"lambda_function_app2.py", "FILENAME_DOWNLOAD":"yourFilename.py"}'
```

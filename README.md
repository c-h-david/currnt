# CURRNT

[![License (3-Clause BSD)](https://img.shields.io/badge/license-BSD%203--Clause-yellow.svg)](https://github.com/c-h-david/currnt/blob/main/LICENSE)

[![Docker Images](https://img.shields.io/badge/docker-images-blue?logo=docker)](https://hub.docker.com/r/chdavid/currnt/tags)

The Combined Utilities for River Routing Nested Together (CURRNT) is designed to
simplify the execution of the Routing Application for Parallel computatIon of
Discharge (RAPID) and the Reproducible Routing Rituals (RRR) on Amazon Web
Services (AWS).

## Local execution

Download CURRNT:

```bash
git clone https://github.com/c-h-david/currnt
```

Enter the CURRNT directory:

```bash
cd currnt/
```

Create Docker image:

```bash
docker build -t chdavid/currnt:app0-latest -f Dockerfile_app0 .
```

Execute Docker image as a Docker container:

```bash
docker run --rm -p 9000:8080 chdavid/currnt:app0-latest
docker run -e EARTHDATA_USERNAME="yourEarthDataUserName" \
           -e EARTHDATA_PASSWORD="yourEarthDataPassword" \
           --rm -p 9000:8080 chdavid/currnt:app3-latest
docker run -e EARTHDATA_USERNAME="yourEarthDataUserName" \
           -e EARTHDATA_PASSWORD="yourEarthDataPassword" \
           -e AWS_ACCESS_KEY_ID="yourKeyID" \
           -e AWS_SECRET_ACCESS_KEY="yourSecretAccessKey" \
           --rm -p 9000:8080 chdavid/currnt:app4-latest
```

> The `--rm` option deletes the container after execution. The `-p 9000:8080`
> option maps Transmission Control Protocol (TCP) ports. In this case, the
> `8080` port in the Docker container is mapped to the `9000` port in the Docker
> host. Also, if one of your environmental variables has a special character,
> consider using the `\` escape character before the special character.

Try it out:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" \
     --data-raw '{"basin_id":"74", "lsm_mod":"VIC",
                  "s3_name":"currnt-data", "yyyy_mm":"2000-01"}'
```

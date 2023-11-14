# Docker Knowledge
## Building
#### Building for aarch:  
https://www.docker.com/blog/multi-arch-images/

#### Any cpu
```--platform linux/amd64,linux/arm64,linux/arm/v7```

#### ARM64 only (Raspi 4)
```--platform linux/arm64```

#### Save Docker image to file
```docker save image:latest > <path>/dockerimage.tar```

## Dockerfile
#### Run container for ever
```CMD ["sleep", "infinity"]```

## Container Management
#### Show all env vars of a container
```docker exec <container id> printenv```

## Registry
#### Own local registry
##### HTTP
https://docs.docker.com/registry/deploying  
https://docs.docker.com/engine/reference/commandline/push  
```docker run -d -p 5000:5000 --restart always --name YourRegistryName registry:latest```

##### HTTPS
```docker run -d --restart always --name YourRegistryName -v /PATH_FROM_HOST/certs:/certs -e REGISTRY_HTTP_ADDR=0.0.0.0:5000 -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/YOUR_CERT.crt -e REGISTRY_HTTP_TLS_KEY=/certs/YOUR_KEY.key -p 5000:5000 registry:latest```

#### Push image to registry
##### Rename image first
```docker image tag your-image-name:latest registry-adress:5000/your-image-name:latest```

##### Push to your registry
```docker image push registry-adress:5000/your-image-name:latest```

##### (Optional) Rename the pushed image after you pulled it
```docker image tag registry-adress:5000/your-old-image-name:latest your-new-image-name:latest```

##### List all current images
```docker image ls```

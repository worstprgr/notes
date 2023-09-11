# Docker Knowledge
## Building
#### Building for aarch:  
https://www.docker.com/blog/multi-arch-images/

#### Any cpu
```--platform linux/amd64,linux/arm64,linux/arm/v7```

#### ARM64 only (Raspi 4)
```--platform linux/arm64```

#### Save Docker Image to file
```docker save image:latest > <path>/dockerimage.tar```

## Dockerfile
#### Run container for ever
```CMD ["sleep", "infinity"]```

## Registry
#### Own local registry
https://docs.docker.com/registry/deploying/
```docker run -d -p 5000:5000 --restart always --name YourRegistryName registry:latest```

###Building for aarch:  
https://www.docker.com/blog/multi-arch-images/

####Any cpu
--platform linux/amd64,linux/arm64,linux/arm/v7

####ARM64 only (Raspi 4)
--platform linux/arm64


###Save Docker Image to file
docker save image:latest > <path>/dockerimage.tar

# Notes for renewing a cert
_Primarily for nginx_  

## Pre-requisite
You'll need:  
- certificate file
- private key file

## Steps
1. `cat` the files together with `cat certificate privatekey > new_bundled_file`
2. Check if the bundle is working: `openssl x509 -noout -text -in new_bundled_file`. If the data is correct (e.g. subject: *.yourdomain.com), it's looking good
3. backup the old certificates/keys and replace them with the new ones
4. restart the services (depends on the service)

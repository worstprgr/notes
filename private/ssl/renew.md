# Notes for renewing a cert
_Primarily for nginx and postfix_  

## Pre-requisite
You'll need:  
- certificate file
- private key file

## Steps
1. `cat` the files together with `cat certificate privatekey > new_bundled_file`
2. backup the old certificates/keys and replace them with the new ones
3. restart the services (depends on the service)

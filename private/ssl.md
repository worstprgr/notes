# SSL Knowledge
### Creating own SSL cert
https://dev.to/techschoolguru/how-to-create-sign-ssl-tls-certificates-2aai
https://www.techrepublic.com/article/how-to-deploy-self-hosted-docker-registry-self-signed-certificates

### cnf file example
```
[req]
default_bits  = 2048
distinguished_name = req_distinguished_name
req_extensions = req_ext
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
countryName = DE
stateOrProvinceName = N/A
localityName = N/A
organizationName = YourName Self-Signed
commonName = YourName

[req_ext]
subjectAltName = @alt_names

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = *.domain.com
IP.1 = 192.168.0.1
```

### Creating SSL crt & key
##### 01. Generate private key
```openssl genrsa 1024 > domain.key```

##### 02. Change permissions
```chmod 400 domain.key```

##### 03. Create cnf file and adjust & paste the content mentioned above (cnf file example)
Important things to change:
- countryName
- organizationName
- commonName
- DNS.1
- IP.1

You can have more DNS and IP entries. Just adjust the number behind "DNS." and "IP.".  
You don't need DNS **and** IP, you can leave only one entry and omit the other.  
```nano expand.cnf```

##### 04. Generate certificate
```openssl req -new -x509 -nodes -sha1 -days 365 -key domain.key -out domain.crt -config expand.cnf```  

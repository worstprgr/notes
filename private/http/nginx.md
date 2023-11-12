# Nginx
Redirect all `http` requests to `https`  

1. `cd /etc/nginx/sites-enabled/<your site>`  
2. *Add* this rule:  
```
server {
	listen 80;
	server_name domain.com www.domain.com;

	location / {
		return 301 https://$host$request_uri;
	}
}
```

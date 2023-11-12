# HTACCESS file
Redirect all http requests to https  
```
RewriteEngine On
RewriteCond %{SERVER_PORT} !=443
RewriteRule ^(.*)$ https://example.com/$1 [R=301,L]
```

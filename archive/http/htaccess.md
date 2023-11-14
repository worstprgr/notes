# HTACCESS file
Redirect all http requests to https  

Create a `.htaccess` file in your root dir of the site:  
```
RewriteEngine On
RewriteCond %{SERVER_PORT} !=443
RewriteRule ^(.*)$ https://www.example.com/$1 [R=301,L]
```

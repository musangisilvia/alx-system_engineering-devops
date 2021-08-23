# 0x0F-load_balancer


## 0-custom_http_repsonse_header

Configure web-02 to be identical to web-01 using the bashscript in the [web server project](https://github.com/musangisilvia/alx-system_engineering-devops/tree/master/0x0C-web_server)
* Additional requirements are:
  - confifure Nginx so that its HTTP response contains a custom header:
    * ```X-Served-By``` <hostname>

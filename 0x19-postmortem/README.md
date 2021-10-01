# Postmortem

## Issue Summary
On 30/09/2021 at 7:00pm EAT, 100% of the webserver was down for a total of 15 minutes. Service was restored at 7:15pm EAT. The website architecture consists of two servers.The usage of these servers is regulated by a loadbalancer, one server was down hence the burden of service lay on the second server. The root cause was a syntax error in the ``` /etc/nginx/sites-available/default ``` file of nginx running on one server. The synstax error was in the form of a missing semicolon in the added line, resulting in nginx failing to start.

## Timeline
7:00pm EAT: Issue was detected.
7:05pm EAT: While using curl to check the response headers, the custom header indicating the name of the server that sent the response showed that only one server was responding to the requests
7:08pm EAT: Logged into the server that was not responding.
7:09pm EAT: Ran the command ``` sudo service nginx status ``` to bring up a log of the current status of nginx.
7:11pm EAT: It was discovered that nginx was not running and the cause of failure was outlined in the following snippet:
- ```  nginx[31101]: nginx: [emerg] invalid number of arguments in "rewrite" directive in /etc/nginx/sites-available/default  ```
- ```  nginx[31101]: nginx: configuration file /etc/nginx/nginx.conf test failed ```
7:13pm EAT: Opened the file stated in the first line of the snippet and added a semicolon to the reqrite directive. 
7:14pm EAT: Saved the file and restarted Nginx.
7:15pm EAT: Service was restored.

## Root Cause and Resolution
## Corrective Measures

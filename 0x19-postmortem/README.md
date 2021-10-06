# Postmortem

![fire in the server lol](https://www.meme-arsenal.com/memes/437534c12d20ac33aab23da961731233.jpg)

## Issue Summary
On 30/09/2021 at 7:00pm EAT, 100% of the webserver was down for a total of 15 minutes. Service was restored at 7:15pm EAT. The website architecture consists of two servers.The usage of these servers is regulated by a loadbalancer, one server was down hence the burden of service lay on the second server. The root cause was a syntax error in the ``` /etc/nginx/sites-available/default ``` file of nginx running on one server. The synstax error was in the form of a missing semicolon in the added line, resulting in nginx failing to start.

## Timeline
7:00pm EAT: Issue was detected.
7:05pm EAT: While using curl to check the response headers, the custom header indicating the name of the server that sent the response showed that only one server was responding to the requests
7:08pm EAT: Issue was handled by Silvia, the server administrator who logged into the server that was not responding.
7:09pm EAT: She ran the command ``` sudo service nginx status ``` to bring up a log of the current status of nginx.
7:11pm EAT: It was discovered that nginx was not running and the cause of failure was outlined in the following snippet:
- ```  nginx[31101]: nginx: [emerg] invalid number of arguments in "rewrite" directive in /etc/nginx/sites-available/default  ```
- ```  nginx[31101]: nginx: configuration file /etc/nginx/nginx.conf test failed ```
7:13pm EAT: She then opened the file stated in the first line of the snippet and added a semicolon to the rewrite directive. 
7:14pm EAT: The file was saved and restarted Nginx.
7:15pm EAT: Service was restored.

## Root Cause and Resolution
The root cause was the syntax error in the rewrite directive added to the /etc/nginx/sites-available/default. This was resolved by first checking the status of the nginx service. This outlined the cause of error as a syntax error in the file /etc/nginx/sites-available/default. The file was opened and a semicolon was added at the end of the rewrite directive. Afterwards, the file was saved and nginx was restarted. This restored the service.

## Corrective Measures

- Ensure that status of a service whose configuration file has been altered is checked after restart/reload. 
- Double check that the correct syntax is being used in the configuration files before closing the file and saving it.

![dusting hands off](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fsearch%2Fdust-off-hands-gifs&psig=AOvVaw2MtwCdq2A1Wo7d-BtVBS4R&ust=1633602885323000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCJiZnJLLtfMCFQAAAAAdAAAAABAD)
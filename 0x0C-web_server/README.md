# 0x0C-web_server

A webserver is a computer software and underlying hardware that accepts requests via
[HTTP]() ( the network prootocol created to distribbute web pages) or its secure variant
[HTTPS]()

## 0-transfer_file

A bash script that transfers a file from our client to a server.
- It accepts four parameters:
    * PATH to file to be transfered
    * IP of the server we want to transfer to.
    * USERNAME scp connects with
    * PATH to SSH private key that scp uses.
- Displays ``` Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY ``` if less than 3 parameteres are passed.
- scp transfers the file to the user home directory
- strict hostkey checking must be disabled when using scp


# Web Server Configuration Project

This repository contains scripts and instructions for configuring a web server using Nginx. The project is organized into several tasks, each focusing on a specific aspect of the server setup.

## Task 0: Transfer a file to your server

### Script: `0-transfer_file`

This script transfers a file from the client to the server using scp. It accepts parameters for the file path, server IP, username, and SSH private key.

#### Example Usage:

```bash
./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key

Task 1: Install nginx web server
Script: 1-install_nginx_web_server
This script installs Nginx on the server, configures it to listen on port 80, and sets up a basic "Hello World!" page. The script is designed to be run on the server.

Task 2: Setup a domain name
Configure a domain name (myschool.tech) and point it to the web server's IP address. The DNS records should be set up with an A entry.

Task 3: Redirection
Script: 3-redirection
Configure Nginx to redirect requests from /redirect_me to another page using a "301 Moved Permanently" redirect. The script automates this configuration on a new Ubuntu machine.

Task 4: Not found page 404
Script: 4-not_found_page_404
Configure Nginx to display a custom 404 page with the message "Ceci n'est pas une page" when a resource is not found. The script automates this configuration on a new Ubuntu machine.

These scripts serve as a foundation for setting up a basic web server and handling common configurations.

# Web Stack Redundancy Project

## Overview

In this project, the goal is to enhance the web stack for redundancy by configuring web-02 to be identical to web-01 and installing and configuring HAproxy as a load balancer on lb-01. This will allow for better traffic handling and increased reliability.

## Task 0: Double the Number of Webservers

### Requirements:

- Configure Nginx on web-02 to be identical to web-01.
- Add a custom HTTP response header, "X-Served-By," containing the hostname of the server.
- Write a Bash script, `0-custom_http_response_header`, to automate the configuration.

### How to Run:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-stack-redundancy.git
   cd web-stack-redundancy

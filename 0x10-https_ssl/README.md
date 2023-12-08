This README provides guidance on configuring your domain, implementing SSL termination with HAProxy, and enforcing HTTPS traffic. Follow the steps below to achieve a secure and optimized setup for your website.

# Task 0: World Wide Web Configuration
Domain Zone Configuration
Configure your domain zone to ensure that the subdomain www points to your load balancer IP (lb-01).

Add other subdomains as needed for convenience.

bash
Copy code
./subdomain_info.sh
Ensure that the script provides accurate details about the configured subdomains.

# Task 1: HAProxy SSL Termination
Certificate Creation with Certbot
Generate a certificate using Certbot for your subdomain www.

Follow the Certbot instructions to complete the certificate creation process.

HAProxy Configuration for SSL Termination
Configure HAProxy to handle encrypted traffic for the subdomain www.

Ensure that HAProxy is set up to decrypt the incoming SSL traffic and pass it on to its destination.

# No Loophole in Website Traffic
Advanced Configuration
Implement automatic redirection of HTTP traffic to HTTPS to ensure no unencrypted traffic is possible. Modify your HAProxy configuration to enforce HTTPS.

Usage
After completing the configuration tasks, your website should be accessible securely via the subdomain www. Use the provided Bash script to check subdomain information, and verify that the HAProxy SSL termination and HTTPS enforcement are functioning correctly.

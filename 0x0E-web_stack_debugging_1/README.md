# Nginx Configuration

This set of Bash scripts helps configure an Nginx server to listen on port 80.

## Script 1: Configure Nginx Server

### Purpose
- Removes the default Nginx configuration file.
- Configures Nginx to listen on port 80.
- Restarts Nginx for the changes to take effect.

### Usage
```bash
#!/usr/bin/env bash
# Configures Nginx server to listen to port 80.

# Removes the default Nginx configuration file
rm /etc/nginx/sites-enabled/default

# Configures Nginx to listen on port 80
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# restart nginx
service nginx restart

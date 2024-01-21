# Web Server Configuration

This repository contains scripts to configure a web server to run Nginx as the nginx user listening on port 8080.

## Scripts

### create_nginx_config.sh

This script modifies the configuration of a web server to run Nginx as the nginx user listening on port 8080. The following steps are performed:

1. Replace the '#user' value in the config file with 'nginx'.
2. Replace port 80 with 8080 in the sites-available config.
3. Give owner permissions to read and write to the config file.
4. Kill the apache2 process if it is running.
5. Start the nginx service with the new nginx user.

### run_whoami.sh

This script creates and runs the whoami command as the specified user. The following steps are performed:

1. Use the sudo command to run the command as the specified user.
2. Use the -u option to specify the username of the user to run the command as.
3. Use the $1 variable to pass the username as an argument to the script.

## Usage

To use these scripts, simply download them to your web server and run them using the following commands:

```bash
./create_nginx_config.sh
./run_whoami.sh username

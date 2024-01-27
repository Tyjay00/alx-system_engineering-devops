# AirBnB Clone Deployment

This repository contains a series of tasks related to deploying the AirBnB Clone application on a web server. The tasks involve setting up the development environment, configuring Flask, integrating Gunicorn for production, and using Nginx as a reverse proxy.

## Task 0: Set up development with Python

To serve the AirBnB Clone v2 on web-01, follow these steps:

1. Complete task #3 of your SSH project for web-01.
2. Install the net-tools package: `sudo apt install -y net-tools`
3. Git clone your AirBnB_clone_v2 on your web-01 server.
4. Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
5. Ensure your Flask application object is named `app`.

```bash
python3 -m web_flask.0-hello_route
curl 127.0.0.1:5000/airbnb-onepage/
Task 2: Serve a page with Nginx
Configure Nginx to serve your page from the route /airbnb-onepage/:

Nginx must serve the page both locally and on its public IP on port 80.
Proxy requests to the process listening on port 5000.
Include your Nginx config file as 2-app_server-nginx_config.


Certainly! Here's the consolidated README.md file with the task scripts:

markdown
Copy code
# AirBnB Clone Deployment

This repository contains a series of tasks related to deploying the AirBnB Clone application on a web server. The tasks involve setting up the development environment, configuring Flask, integrating Gunicorn for production, and using Nginx as a reverse proxy.

## Task 0: Set up development with Python

To serve the AirBnB Clone v2 on web-01, follow these steps:

1. Complete task #3 of your SSH project for web-01.
2. Install the net-tools package: `sudo apt install -y net-tools`
3. Git clone your AirBnB_clone_v2 on your web-01 server.
4. Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
5. Ensure your Flask application object is named `app`.

```bash
python3 -m web_flask.0-hello_route
curl 127.0.0.1:5000/airbnb-onepage/
Task 1: Set up production with Gunicorn
To set up the production application server with Gunicorn on web-01:

Install Gunicorn and any other required libraries.
Ensure the Flask application object is named app.
Serve the same content from the same route as in the previous task on port 5000.
Use Gunicorn to bind to localhost on port 5000 with your application object as the entry point.
Ensure nothing is listening on port 6000.
bash
Copy code
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
curl 127.0.0.1:5000/airbnb-onepage/
Task 2: Serve a page with Nginx
Configure Nginx to serve your page from the route /airbnb-onepage/:

Nginx must serve the page both locally and on its public IP on port 80.
Proxy requests to the process listening on port 5000.
Include your Nginx config file as 2-app_server-nginx_config.
bash
Copy code
# On the server:
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

# On local terminal:
curl -sI 35.231.193.217/airbnb-onepage/
curl 35.231.193.217/airbnb-onepage/
Task 3: Add a route with query parameters
Expand the web application by adding another service for Gunicorn:

Proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.
Include your Nginx config file as 3-app_server-nginx_config.

Task 4: Serve your AirBnB clone API
Serve what you built for AirBnB clone v3 - RESTful API on web-01:

Git clone your AirBnB_clone_v3.
Setup Nginx to point to a Gunicorn instance listening on port 5002.
Nginx must serve the page both locally and on its public IP on port 80.
Bind Gunicorn to api/v1/app.py.

Task 5: Serve your AirBnB clone
Serve what you built for AirBnB clone - Web dynamic on web-01:

Git clone your AirBnB_clone_v4.
Gunicorn should serve content from web_dynamic/2-hbnb.py on port 5003.
Setup Nginx to point to your Gunicorn instance.
Ensure Nginx properly serves static assets found in web_dynamic/static/.
Reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP.
Nginx must serve the page both locally and on its public IP on port 5003.

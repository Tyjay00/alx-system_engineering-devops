# Hello Holberton Container

In this project, the goal is to run Apache on a Docker container and make it return a page containing 'Hello Holberton' when querying the root of it.

### Example:

```bash
$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
$ curl 0:8080
curl: (52) Empty reply from server
$ curl 0:8080
Hello Holberton

# Web stack debugging #0

To __debug the issue and ensure that Apache returns a page__ containing "Hello Holberton" when querying the root of the container, you can follow these steps:

* connect to docker container:
docker exec -it <container_id> /bin/bash

* start Apache server
service apache2 start

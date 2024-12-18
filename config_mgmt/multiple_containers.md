```bash

docker run -d --name db --restart always \
    -v db_data:/var/lib/mysql -p 3306 -p 3306 \
    -e MYSQL_ROOT_PASSWORD=somewordpress \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=wordpress \
    -e MYSQL_PASSWORD=wordpress \
    mariadb:10

```

```bash

docker run -d --name wordpress --restart always \
    -v wp_data:/var/www/html -p 80:80 \
    -e WORDPRESS_DB_HOST=db \
    -e WORDPRESS_DB_USER=wordpress \
    -e WORDPRESS_DB_PASSWORD=wordpress \
    -e WORDPRESS_DB_NAME=wordpress \
    wordpress:latest

```

```bash 

docker stop wordpress && docker rm wordpress

docker stop db && docker rm db

```

```bash

docker network create myblog

```

```bash

docker run -d --name db --restart always \
    -v db_data:/var/lib/mysql -p 3306 -p 3306 \
    -e MYSQL_ROOT_PASSWORD=somewordpress \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=wordpress \
    -e MYSQL_PASSWORD=wordpress \
    --network myblog \
    mariadb:10

docker run -d --name wordpress --restart always \
    -v wp_data:/var/www/html -p 80:80 \
    -e WORDPRESS_DB_HOST=db \
    -e WORDPRESS_DB_USER=wordpress \
    -e WORDPRESS_DB_PASSWORD=wordpress \
    -e WORDPRESS_DB_NAME=wordpress \
    --network myblog \
    wordpress:latest

```

```bash

docker run -it debian:latest

ping db.myblog

```
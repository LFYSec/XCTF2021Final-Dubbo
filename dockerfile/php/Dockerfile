FROM php:7.4-fpm-alpine

COPY _files /tmp/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add --update --no-cache nginx \
    && mkdir /run/nginx \
    # configure file
    && mv /tmp/docker-php-entrypoint /usr/local/bin/docker-php-entrypoint \
    && mv /tmp/nginx.conf /etc/nginx/nginx.conf \
    && echo '<?php phpinfo();' > /var/www/html/index.php \
    && chown -R www-data:www-data /var/www/html \
    && chmod +x /usr/local/bin/docker-php-entrypoint \
    # clear
    && rm -rf /tmp/*
    
WORKDIR /var/www/html

EXPOSE 80

VOLUME ["/var/log/nginx"]

CMD ["/bin/bash", "-c", "docker-php-entrypoint"]

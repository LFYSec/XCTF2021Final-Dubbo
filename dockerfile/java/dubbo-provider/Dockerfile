FROM ctfhub/base_web_tomcat_8u191

COPY _files /tmp/files

RUN apk update && \
    apk add --no-cache curl && \
    rm -rf /etc/apk/* /var/cache/apk/* /usr/share/man && \
    mv /tmp/files/dubbo-demo-provider-1.0.jar /opt/provider.jar && \
    rm -rf /tmp/*

CMD ["java","-jar","/opt/provider.jar"]
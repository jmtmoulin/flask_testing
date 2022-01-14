FROM "ubuntu:20.04"

RUN apt-get update -y \
    && apt-get install -y zlib1g \ 
    && apt-get install -y zlib1g-dev \ 
    && apt-get install -y libffi-dev \ 
    && apt-get install -y build-essential \
    && apt-get install -y python-dev \
    && apt-get install -y libpcre3  \ 
    && apt-get install -y libpcre3-dev  \ 
    && apt-get install -y libssl-dev \
    && apt-get install -y unixodbc-dev \ 
    && apt install -y net-tools \ 
    && apt install -y psmisc \ 
    && apt install -y vim  

COPY ./static_packages/Python-3.10.1.tgz /tmp/Python-3.10.1.tgz
WORKDIR /tmp
RUN tar -zxvf /tmp/Python-3.10.1.tgz \
    && mkdir /usr/share/python3.10 \
    && mv /tmp/Python-3.10.1/* /usr/share/python3.10 \ 
    && rm -f /tmp/Python-3.10.1.tgz 



WORKDIR /usr/share/python3.10

RUN ./configure --enable-optimizations \
    && make altinstall \
    && ln -s /usr/share/python3.10/python /usr/bin/python3.10 \
    && /usr/share/python3.10/python -m pip install -U pip


COPY ./files/requirements.txt /tmp/requirements.txt
RUN /usr/share/python3.10/python -m pip install -r /tmp/requirements.txt

WORKDIR /tmp

RUN groupadd nginx_API \
    && groupadd nginx \
    && useradd nginx -g nginx \
    && useradd nginx_API -g nginx_API \
    && usermod -a -G nginx_API nginx \
    && usermod -a -G nginx nginx_API \ 
    && mkdir /home/nginx \
    && mkdir /home/nginx_API \
    && chmod 640 /home/nginx \
    && chmod 740 /home/nginx_API \
    && chown nginx:nginx -R /home/nginx \
    && chown nginx_API:nginx_API -R /home/nginx_API 

COPY ./files/flask/__init__.py /home/nginx_API/__init__.py
WORKDIR /home/nginx_API
ENTRYPOINT ["tail", "-f", "/dev/null"]
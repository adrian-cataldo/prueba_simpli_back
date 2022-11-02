FROM python:3.10.0-alpine3.14

LABEL maintainer="adrian.cataldo093@gmail.com"

# https://stackoverflow.com/questions/25682408/docker-setup-with-a-mysql-container-for-a-python-app/47967647
# https://pkgs.alpinelinux.org/packages

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        mariadb-dev \
        gettext-dev \
        zlib-dev \
        build-base \
    ;

RUN python3 -m pip install --upgrade pip

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

#translations
RUN python3 manage.py makemessages -a && python3 manage.py compilemessages
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
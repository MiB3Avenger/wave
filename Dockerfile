FROM python:3.10-slim AS base
ENV PYTHONUNBUFFERED 1

ENV C_FORCE_ROOT true

# Fix timezone, needs tzdata to be installed
ARG TZ='Europe/London'
ENV TZ ${TZ}

RUN apt-get update
RUN apt-get install --no-install-recommends -y python3-dev gcc musl-dev gettext openssl libssl-dev tzdata htop
RUN apt-get install --no-install-recommends -y curl

ENV NVM_DIR /.nvm
RUN mkdir $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
ENV NODE_VERSION v20.0.0
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH
ENV APP_ENV local

WORKDIR /code

COPY requirements.txt /code
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code

COPY vite.config.js /code
COPY package.json /code/

FROM base AS install
RUN npm set progress=false && npm config set depth 0
RUN npm install
RUN npm ci

FROM install AS build
COPY . .

RUN npm run build

FROM build AS deploy
EXPOSE 8000
EXPOSE 3000
CMD python manage.py migrate;python manage.py collectstatic --no-input;gunicorn wave.wsgi -b 0.0.0.0:8000 --chdir /code/ --config gunicorn_conf.py 

RUN apt-get autoremove
RUN apt-get clean
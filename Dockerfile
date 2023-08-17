FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

ENV C_FORCE_ROOT true

# Fix timezone, needs tzdata to be installed
ARG TZ='Europe/Oslo'
ENV TZ ${TZ}

RUN apt-get update
RUN apt-get install --no-install-recommends -y python3-dev gcc musl-dev gettext openssl libssl-dev tzdata htop
RUN apt-get install --no-install-recommends -y curl

ENV NVM_DIR /.nvm
RUN mkdir $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
ENV NODE_VERSION v16.17.1
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

WORKDIR /code

COPY requirements.txt /code
RUN pip install --no-cache-dir -r requirements.txt

COPY vite.config.js /code
COPY package* /code/
RUN npm install

COPY . .

# RUN npm run build

EXPOSE 8000
EXPOSE 3000
CMD python manage.py migrate;python manage.py collectstatic --no-input;\
    gunicorn wave.wsgi -b 0.0.0.0:8000 --chdir /code/ --config gunicorn_conf.py 

RUN apt-get autoremove
RUN apt-get clean
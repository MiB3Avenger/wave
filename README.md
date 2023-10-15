# Wave

This is the repository for an Masters of Science Course Assignment, Internet Technology: Wave - A social media website.

Vue components are located in `frontend/js` folder. This app comes with Vue, Vuetify,
Vuex and Vue router included. Also on demo page we have 2 independent Vue apps along with
Django rendered elements.

In places where we have both Django and Vue app, any changes that are made to Vue app, will be
immediately visible since Vite supports hot module replacement (changes to js, vue and style files).

Thanks to [@elrik](https://gitlab.com/elrik/django-vite-example) for initial boilerplate for Django + Vite.

## Trello
To track changes visit:
[Trello](https://trello.com/b/EiOsPn4b/wave-social-media)<br />

# Contents
- [Running the app](#running-the-app)
    - [Running with Docker](#running-with-docker)
    - [Running Locally](#running-locally)
- [Building Files for Production](#building-files-for-production)
- [Team Members](#team-members)

<a id="running-the-app"></a>
# Running the app

<a id="running-with-docker"></a>
## Running with docker

Clone repository, switch dir to the cloned repo and run `docker compose -f docker-compose.yml up -d --build`
Once you build the image, run `docker compose up -d` in the future, unless image has been changed.
This will build Docker container and spin up Django application on `http://localhost:8000`
and vite dev server on port `http://localhost:3000/static/vite/`

Open browser and visit [http://localhost:8000](http://localhost:8000)

<a id="running-locally"></a>
## Running locally

You should be running Node v19.3.0 and Npm v9.2.0 or later for this to work.

Clone repository, switch dir to the cloned repo. Set up python virtualenv and activate it.
After you have activated virtualenv run following commands:
```sh
pip install -r requirements.txt
python manage.py migrate
npm install
npm ci
```

If you want you can run single command, but you should have 2 terminals and start
Django server and Vite dev server separately.
Single command:
```sh
python manage.py runserver 0:8000 & npm run dev
```

If you have 2 terminals you can run:
```sh
python manage.py runserver 0:8000
```
and in second terminal   
```sh
npm run dev
```

Open browser and visit [http://localhost:8000](http://localhost:8000)

<a id="building-files-for-production"></a>
# Building files for production

In production we don't want to run Vite dev server so we need to build frontend app.

To build your front end app run
```sh
npm install
npm ci
npm run build
```

This will bundle your front-end app and save files in `./frontend/dist`. This folder is added
to the `STATICFILES_DIRS` in Django settings, and for Django to be able to access these files
you need to run `./manage.py collectstatic`.

<a id="team-members"></a>
# Team Members
The initial team members who worked on the project.
|Name|Github|GUID|Course|
|---|---|---|---|---|
|Zhou, Xin|[@didi-0](https://github.com/didi-0)|2756254|MSc in |
|Mcintyre, Robbie|[@RobbieMcintyre99](https://github.com/RobbieMcintyre99)|2330005|MSc in |
|Yang, Yuang|[@RyanXXXXXXXX](https://github.com/RyanXXXXXXXX)|2754318|MSc in |
|Wang, Yifan|[@wangyigou](https://github.com/wangyigou)|2788173|MSc in |
|Nagrale, Chinmay|[@MiB3Avenger](https://github.com/MiB3Avenger)|2788044 |MSc in Computer Systems Engineering|
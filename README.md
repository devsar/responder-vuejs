# About me 
This will setup, using docker-compose, a basic [Responder API](https://python-responder.org/en/latest/) + Vuejs `(vue-cli project)` project.

# Status:

- [x]  Ready to be used for development (hot reload, etc) 
- [x]  Ready to be used on Production (prod settings, etc) 

# First steps 

Start all containers:
  - `docker-compose up`

# How to use it
First, be sure to complete `First steps` (describe above).
Then, after you start all containers (with `docker-compose up`, you are free to start coding the backend or frontend (the code will be auto-reloaded, both
the backend and frontend, each time you save the files in your editor).

# I have a problem, this is not working
Please fill a bug :)

# Directory structure

  - File `docker-compose.yml`: Orchestrate all containers settings
  - Directory `dockerfiles`: 
    - File `responder`: Dockerfile to setup a Responder API 
    - File `vuejs`: Dockerfile to setup Vuejs + Webpack + NPM + etc...
  - File `Pipfile` and `Pipfile.lock`: Pipenv files to install a Responder API project, locally in your system.
  - File `README.md`: You are here :)
  - File `requirements.txt`: Requirements written here will be installed in the `backend` container. This file should be autogenerated by `pipenv lock -r > requirements.txt`, but you are free to set it by hand (at your own risk :-P) 
  - Directory `src`:
    - Directory `backend`: Here is the Responder API project
    - Drirectory `frontend`: Here is the Vuejs project.

# About the backend

## Python version

Responder container uses `python:latest` (more info at `https://hub.docker.com/_/python/`. To know which version is running on the container, run: `docker-compose run backend python --version`

**Important:** Responder runs only with Python versions **>= 3.6**.

## Backend/Responder related things

  > Question: How can i test that the backend is working? 
  - Answer: Just go to `http://localhost:8000/ping`, you should get back a json with info about the framework/version running and the Python version being used in the container.

  > Question: Can i change the port where Responder runs? If `true`, how?
  - Answer: Yes you can. Just change `PORT` environment var (at `.env` file) or in `docker-compose.yml` 

  > Question: How can i disable/enable **code hot reloading**?
  - Answer: To disable it, change `.env` file, and set `DEBUG` var to an empty string (`DEBUG=""`). To enable it, set `DEBUG` value to anything different to an empty string. 

## Deploy API/Web service on Prod
Thanks to [Responder](https://python-responder.org/en/latest/) and [Uvicorn](https://www.uvicorn.org/) the backend is ready to be deployed on prod (no need to setup `ningx`, or anything else). This gets you a ASGI app, with a production static files server (WhiteNoise) pre-installed, jinja2 templating (without additional imports), and a production webserver based on uvloop, serving up requests with gzip compression automatically.

**Important**: Just be sure to not leave `DEBUG` enabled on prod.

## (optional) Install requirements locally on your host 

  - Install `pipenv` with your distro package manager, or as you prefer.
  - In the same directory where `Pipfile` and `Pipfile.lock` exists, run: `pipenv install`
  - Done, now you are able to add your bugs at `src/backend`

# About the frontend 

## (optional) Install `vue-cli` locally on your host

  - Create a directory where `npm i -g ...` will be installed. Run: `mkdir ~/.npm-global`
  - Let `npm` where to find installed packages. Run: `npm config set prefix '~/.npm-global'`
  - Let your `bash` knows where `excecutable` installed by `npm` are. Run: ` echo "export PATH=~/.npm-global/bin:$PATH" >> ~/.bashrc `. Apply changes made on `$PATH` running: `source ~/.bashrc`, or open a new terminal. 
  - Install `@vue-cli`, run: `npm install -g @vue/cli`
  - Install `@vue/cli-init`, run: `npm install -g @vue/cli-init`

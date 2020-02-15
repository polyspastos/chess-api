<span style="font-family:Consolas">

# Chess analysis API
___
___

Analysis of positions based on FEN, putting results in database, query said results through a REST API.
https://www.youtube.com/watch?v=CVuTCrLeq-Y

__Tasks done:__
1. database creation automation
1. database population
1. database and schema models
1. analysis module
1. resource models framework

__Tasks to be done:__
1. accepting different notations
2. polling lichess for ongoing grandmaster games
3. checkmate solver
4. GUI
5. feel free to suggest anything else

---
## I. Installation

### 1. Python packages
#### a. Using pipenv/Pipfile:
* pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy psycopg2 python-chess logging
* pipenv shell

> Pipfile lock should be generated separately if multiple python versions are being used. For now, I only used python 3.6.9. Not included in repository.

#### b. Using pip:
python -m pip install --upgrade flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy psycopg2 python-chess logging

### 2. Vagrant
[Installing Vagrant](https://www.vagrantup.com/docs/installation/ "vagrant installation instructions")
[Installing bionic64 18.04 LTS on Vagrant](https://app.vagrantup.com/hashicorp/boxes/bionic64 "bionic64 installation instructions")


### 3. Docker + PostgreSQL
[Installing Docker on bionic64](https://docs.docker.com/install/linux/docker-ce/ubuntu/ "docker on bionic installation instructions")
[Installing PostgreSQL service on Docker](https://docs.docker.com/engine/examples/postgresql_service/ "docker postgresql installation instructions")
[Repository of Dockerfile and entrypoint](https://github.com/docker-library/postgres/tree/4a82eb932030788572b637c8e138abb94401640c/12 "dockerfile+entrypoint repo link")

### 4. Create the database
#### 4.1. psql
\c <database name\>
#### 4.2. Python
py
from models import db\
db.create_all()
#### 4.3. initdb endpoint eg. with requests (see point 5.)
requests.get('http://127.0.0.1:5000/initdb')
___
## II. Usage
#### 1. Start Vagrant
cd \<working directory>
vagrant up
vagrant ssh

#### 2. Connect to container
docker run --rm -P -e POSTGRES_PASSWORD=bimmbamm --name /<container name> -p 5432:5432 -v $HOME/docker/postgresql/data:/var/lib/postgresql/data postgres


#### 3. Connect to postgres
* psql -h localhost -p 5432:5432 -U postgres __or__
* docker exec -it /<container name> psql -U postgres -W

#### 4. Run development server
py app&#46;py

#### 5. Run browser, Postman or python requests, etc. to send requests to API endpoints
[Postman download](https://www.getpostman.com/downloads/ "postman download link")
pip install requests
</span>











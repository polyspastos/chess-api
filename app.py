from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import inspect, exc

import os
import sys

from flask_restful import Api, Resource

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

from sqlalchemy_utils import database_exists, create_database

from models import model_evaluations

from resources import evaluation

import logging


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_DIR)  
sys.path.append(PROJECT_DIR)

log_format = "%(asctime)-15s:%(name)s:%(levelname)s:%(message)s"
logging.basicConfig(filename='chess_api.log',
                    format=log_format, level=logging.INFO)

logging.info('logging initiated')

app = Flask(__name__)
api = Api(app)

postgrespath = 'postgresql://postgres:bimmbamm@localhost'
database_name = 'chessapi_test2'
database_path = postgrespath + '/' + database_name
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['SECRET_KEY'] = 'hmmm'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class InitializeDatabase(Resource):
    def get(self):
        engine = create_engine(postgrespath)
        if not database_exists(database_path):
            create_database(database_path)
            result = 'Database created.'
        else:
            result = 'Database already created.'
        from init_models import db
        db.create_all()
        if 'already' in result: result += ' Database tables already created.'
        else: result += ' Database tables created.'
        logging.info(result)
        return jsonify(result)


@app.before_first_request
def initialize_api():
    add_resources()
    logging.info('API resources imported. Ready to receive HTTP requests.')

def add_resources():
    api.add_resource(InitializeDatabase,
                     '/initdb')
    api.add_resource(evaluation.EvaluationResource,\
        '/evaluations', '/evaluations/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


postgrespath = 'postgresql://postgres:bimmbamm@localhost'
database_name = 'chessapi_test2'
database_path = postgrespath + '/' + database_name

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['SECRET_KEY'] = 'hmmm'

db = SQLAlchemy(app)


class evaluations(db.Model):
    def __repr__(self):
        return '<id_ %r>' % self.id_

    id_ = db.Column(db.Integer, nullable=False, primary_key=True)
    
    name = db.Column(db.String(100), unique=True)
    position = db.Column(db.String(300), unique=True, nullable=False)
    evaluation = db.Column(db.String(100), nullable=False)
    top_line = db.Column(db.String(1000), nullable=False)
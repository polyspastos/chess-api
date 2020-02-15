from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

postgrespath = 'postgresql://postgres:bimmbamm@localhost'
database_name = 'chessapi_test2'
database_path = postgrespath + '/' + database_name
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Evaluations(db.Model):
    def __repr__(self):
        return '<id_ %r>' % self.id_

    id_ = db.Column(db.Integer, nullable=False, primary_key=True)

    name = db.Column(db.String(100), unique=True)
    position = db.Column(db.String(300), unique=True, nullable=False)
    evaluation = db.Column(db.String(100), nullable=False)
    top_line = db.Column(db.String(1000), nullable=False)

    def __init__(self,
                 id_,
                 name,
                 position,
                 evaluation,
                 top_line):
                 self.name = name
                 self.position = position
                 self.evaluation = evaluation
                 self.top_line = top_line


class EvaluationSchema(ma.Schema):
    class Meta:
        fields = ('id_', 'name', 'position', 'evaluation', 'top_line')



evaluation_schema = EvaluationSchema()
evaluations_schema = EvaluationSchema(many=True)





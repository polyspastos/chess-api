from flask import Flask, request, jsonify
from flask_restful import Resource
from sqlalchemy import exc, func
from psycopg2 import errors

from models.model_evaluations import * 

import analyse

import logging

log_format = "%(asctime)-15s:%(name)s:%(levelname)s:%(message)s"
logging.basicConfig(filename='chess_api.log',
                    format=log_format, level=logging.INFO)


class EvaluationResource(Resource):
    def get(self, name=''):
        evaluations = Evaluations.query.all()
        if name == '':
            result = evaluations_schema.dump(evaluations)
            logging.info(result)
            return jsonify(result)

        else:
            for el in evaluations:
                if el.name == name:
                    evaluation_info = {'id_': el.id_,
                                       'name': el.name,
                                       'position': el.position,
                                       'evaluation': el.evaluation,
                                       'top_line': el.top_line}
                    logging.info(f'Evaluation info requested for {name}.\n{evaluation_info}')
                    return jsonify(evaluation_info)
                else:
                    logging.info(f'Evaluation info not found for {name}.')
                    return f'Position name not found in database.', 401
        
    def post(self, name):
        payload  = request.json

        if 'fen' not in payload.keys():
            return f'FEN missing.', 401

        else:
            analysis_result = analyse.get_analysis_score(payload['fen'])
            if analysis_result:
                temp_top_line = str(analysis_result['pv']).replace('Move.from_uci(', '')
            else: return 'Incorrect FEN position. Please check input.', 401

            formatted_top_line = temp_top_line.replace(')', '')

            if formatted_top_line:
                rows = db.session.query(func.count(Evaluations.id_)).scalar()
                new_evaluation = Evaluations(id_=rows+1,
                                            name=name,
                                            position=payload['fen'],
                                            evaluation=str(analysis_result['score']),
                                            top_line=formatted_top_line)

                try:
                    db.session.add(new_evaluation)
                    db.session.commit()
                except Exception as e:
                    logging.info(e)
                    return f'Database exception: \n{e}', 403
                    db.session.rollback()
                finally: db.session.close()
            else: return f'Invalid request. Analysis error.', 401

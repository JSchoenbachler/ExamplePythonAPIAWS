#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import db

connection = db.Connection("hl-drug-monitor.choxmvghdfxg.us-east-2.rds.amazonaws.com", "HugheyLabDrugMonitor", "postgres", "mysecretpassword")
app = Flask(__name__)
api = Api(app)


class general_exposure(Resource):
    def get(self):
        results = []
        genExps = connection.read("SELECT ingredient_id, ingredient_name, general_exposure_count, general_exposure FROM general_exposures limit 50;")
        for ge in genExps:
        results.append(ge)
        return {
            "results": [r.json() for r in results]
            }
    

api.add_resource(general_exposure, '/general_exposure') # Route_1


if __name__ == '__main__':
     app.run()
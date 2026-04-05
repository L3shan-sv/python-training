from flask import Flask, jsonify, request
from models import Car, CarsRegistry

app =Flask(__name__)
registry=CarsRegistry()

@app.route("/cars , methods=GET")
def list_cars():
    return jsonify(registry.list_cars())

@app.route(",cars , methods=GET")
def get_car(name):
    car=registry.get_car(name):
        


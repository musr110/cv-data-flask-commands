import json
from pprint import pprint

import click
from flask import Flask, jsonify, request

from utils import filter_data

app = Flask(__name__)

# Load CV data from a separate JSON file
try:
    with open("cv_data.json") as json_file:
        cv_data = json.load(json_file)
except FileNotFoundError:
    print("cv_data.json file not found")
except json.decoder.JSONDecodeError:
    print("Invalid json file")


# API endpoints
@app.route("/personal", methods=["GET"])
def get_personal():
    return jsonify(cv_data["personal"])


# using the request object to get the year parameter from the query string
@app.route("/experience", methods=["GET"])
def get_experience():
    if "year" in request.args:
        year = request.args["year"]
        if not year.isdigit() or int(year) < 0:
            return jsonify({"error": "Invalid year"}), 400
        filtered_data = filter_data(cv_data["experience"], year)
        if filtered_data:
            return jsonify(filtered_data)
        else:
            return jsonify({"error": "Invalid year"}), 404
    return jsonify(cv_data["experience"])


# using a path parameter to define the endpoint as "/experience/int:year"
@app.route("/experience/<int:year>", methods=["GET"])
def get_experience_by_year(year):
    """
    Get experience data by year
    """
    filtered_data = filter_data(cv_data["experience"], year)
    if filtered_data:
        return jsonify(filtered_data)
    else:
        return jsonify({"error": "Invalid year"}), 404


@app.route("/education", methods=["GET"])
def get_education():
    return jsonify(cv_data["education"])


# CLI command
@app.cli.command()
def personal():
    pprint(cv_data["personal"])


@app.cli.command()
@click.argument("year")
def experience(year):
    filtered_data = filter_data(cv_data["experience"], year)
    if filtered_data:
        pprint(filtered_data)
    else:
        pprint('{"error": "Invalid year"}')


@app.cli.command()
def education():
    pprint(cv_data["education"])


if __name__ == "__main__":
    app.run()

"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
import string

from flask import Flask, request
from flask import typing as flask_typing

from pract_2.ht_template.job1 import api

AUTH_TOKEN = os.environ.get("OC_API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer
    Proposed POST body in JSON:
    {
      "doi: "10.1103/PhysRevLett.113.251301",
      "raw_dir": "/path/to/my_dir/raw/doi/10.1103/PhysRevLett.113.251301"
    }
    """
    input_data: dict = request.json
    # TODO: implement me
    doi = input_data.get('doi')
    raw_dir = input_data.get('raw_dir')

    if not doi:
        return {
                   "message": "doi parameter is missed",
               }, 400

    # NB: you should handle the request and call these functions:
    api.get_citations(doi=string)

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)

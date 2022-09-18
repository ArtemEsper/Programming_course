"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer for job2
"""
import os

from flask import Flask, request
from flask import typing as flask_typing

import save_in_avro

AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

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
       "data: "2022-08-09",
       "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
     }
     """
# implement the slack response to save file in avro format


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)

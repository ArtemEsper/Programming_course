"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer for job2
"""
import os

from flask import Flask, request
from flask import typing as flask_typing

import save_in_avro

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
          "stg_dir: "/path/to/my_dir/stg/doi/10.1103/PhysRevLett.113.251301",
          "raw_dir": "/path/to/my_dir/raw/doi/10.1103/PhysRevLett.113.251301"
        }
        """
# implement the slack response to save file in avro format


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)

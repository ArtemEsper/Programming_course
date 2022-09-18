"""
Convert giles from raw json to avro format.
"""
import json
import os
from fastavro import writer, parse_schema


def avro(raw_dir, stg_dir):
    # create the parent dir if not exist

    # join path and filename

    # use the following schema for the avro format
    schema = {
        "namespace": "sales_2022-08-09.avro",
        "type": "record",
        "name": "store",
        "fields": [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"}
        ]
    }

    # save file in avro format


if __name__ == "__main__":
    avro()

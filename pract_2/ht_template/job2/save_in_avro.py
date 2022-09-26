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
        "namespace": "doi.avro",
        "type": "record",
        "name": "open citations",
        "fields": [
            {
                'default': None,
                "name": "cited",
                "type": "string"
            },
            {
                'default': None,
                "name": "author_sc",
                "type": "string"
            },
            {
                'default': None,
                "name": "timespan",
                "type": "string"
            },
            {
                'default': None,
                "name": "creation",
                "type": ['null', {'logicalType': 'date', 'type': 'int'}]
            },
            {
                'default': None,
                "name": "citing",
                "type": "string"
            },
            {
                'default': None,
                "name": "oci",
                "type": "string"
            },
            {
                'default': None,
                "name": "journal_sc",
                "type": "string"
            }
        ]
    }

    # save file in avro format


if __name__ == "__main__":
    avro()

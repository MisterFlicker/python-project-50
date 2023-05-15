import json


def parse(data, data_format):
    if data_format == 'json':
        return json.loads(data)
    raise ValueError(f'Unrecognizid extension: {data_format}')

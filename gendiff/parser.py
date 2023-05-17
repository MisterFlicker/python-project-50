import json
import yaml


def parse(data, data_format):
    if data_format == 'yaml' or data_format == 'yml':
        return yaml.safe_load(data)
    if data_format == 'json':
        return json.loads(data)
    raise ValueError(f'Unrecognizid extension: {data_format}')

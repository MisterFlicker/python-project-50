from gendiff.stylish import lets_stylish
from gendiff.plain import lets_plain
from gendiff.json import lets_json


def pick_formater(diff, formater):
    if formater == 'stylish':
        return lets_stylish(diff)
    elif formater == 'plain':
        return lets_plain(diff)
    elif formater == 'json':
        return lets_json(diff)
    raise ValueError(f'Unrecognized formater: {formater}')

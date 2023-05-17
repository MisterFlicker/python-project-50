from os.path import splitext

ADM_EXTENSIONS = ('json', 'yaml', 'yml')


def opening_file(path):
    extension = splitext(path)[1][1:]
    if extension in ADM_EXTENSIONS:
        with open(path) as x:
            data = x.read()
            return data, extension
    raise ValueError(f'Unrecognized extension: {extension}')

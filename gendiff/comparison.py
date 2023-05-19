def comparing(data1, data2):  # noqa: C901
    result = list()
    keys = sorted(set(list(data1.keys()) + list(data2.keys())))
    for key in keys:
        if key not in data1:
            result.append({
                'key': key,
                'operation': 'add',
                'new': data2[key]
                })
        elif key not in data2:
            result.append({
                'key': key,
                'operation': 'removed',
                'old': data1[key]
                })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child = comparing(data1[key], data2[key])
            result.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key,
                'operation': 'same',
                'value': data1[key]
                })
        elif data1[key] != data2[key]:
            result.append({
                'key': key,
                'operation': 'changed',
                'old': data1[key],
                'new': data2[key]
                })
    return result

def making_sorted_list(unsorted):
    result = {}
    for i in unsorted:
        if i['operation'] == 'same':
            result['   ' + i['key']] = i['value']
        elif i['operation'] == 'removed':
            result[' - ' + i['key']] = i['old']
        elif i['operation'] == 'add':
            result[' + ' + i['key']] = i['new']
        elif i['operation'] == 'changed':
            result[' - ' + i['key']] = i['old']
            result[' + ' + i['key']] = i['new']
    result = str(result)
    result = result[:1] + '\n ' + result[1:]
    result = result[:-1] + '\n' + result[-1:]
    result = result.replace("'", "")
    result = result.replace(",", '\n')
    return result

def making_sorted_list_bool(part):
    if 'value' in part:
        part.update({'value': str(part['value']).lower()})
    elif 'old' in part:
        part.update({'old': str(part['old']).lower()})
    elif 'new' in part:
        part.update({'new': str(part['new']).lower()})
    return part



def making_sorted_list(unsorted, format_in):
    result = {}
    for i in unsorted:
        if list(i.values())[2] == 'False' or 'True':
            i = making_sorted_list_bool(i)
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

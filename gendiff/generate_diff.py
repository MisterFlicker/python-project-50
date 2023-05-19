from gendiff.work_data import opening_file
from gendiff.parser import parse
from gendiff.comparison import comparing
from gendiff.all_formaters import pick_formater


def generate_diff(file_path1, file_path2, formater='stylish'):
    data1, format1 = opening_file(file_path1)
    data2, format2 = opening_file(file_path2)
    parced_data1 = parse(data1, format1)
    parced_data2 = parse(data2, format2)
    diff = comparing(parced_data1, parced_data2)
    return pick_formater(diff, formater)

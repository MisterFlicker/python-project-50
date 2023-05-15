from gendiff.work_data import opening_file
from gendiff.parser import parse
from gendiff.comparison import comparison_of_files
from gendiff.sorting_result import making_sorted_list


def generate_diff(file_path1, file_path2):
        data1, format1 = opening_file(file_path1)
        data2, format2 = opening_file(file_path2)
        parced_data1 = parse(data1, format1)
        parced_data2 = parse(data2, format2)
        diff = comparison_of_files(parced_data1, parced_data2)
        return making_sorted_list(diff)


import os
import re


pattern = re.compile(r'@\w+\([\d]+\)')
directory_path = os.path.abspath('/Users/r_khripunov/Git/client/Scripts/automation/blitz/autotests/functional/settings')


def get_file_name():
    file_name = input('Enter file name: ') or 'graphic_options.py'
    return file_name


def get_all_ids():
    file_path = os.path.join(directory_path, get_file_name())
    with open(file_path) as file:
        ids = [re.sub(r'\D+', '', line) for line in file if re.search(pattern, line)]
        return ids


if __name__ == '__main__':
    for test_id in get_all_ids():
            print(test_id, end=' ')

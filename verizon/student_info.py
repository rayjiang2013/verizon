'''
Created on Sep 20, 2015

@author: ljiang
'''
import re

def print_student_info(filename):
    info_dict={}
    with open(filename) as f_obj:
        for line in f_obj:
            keys_list = line.split(' ', 1)
            key=re.search(r'^name:(\w+)', keys_list[0]).group(1)
            value=re.search(r'address:(\w+\s?\w+)$|\n', keys_list[1]).group(1)
            info_dict[key]=value
    return info_dict

print_student_info('student.txt')
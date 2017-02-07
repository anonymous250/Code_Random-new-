# -*- coding:UTF-8 -*-


import random


str ='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTXYZ'
count_number = int(raw_input('输入激活码数量：'))


def count_code(count_number):
    while count_number > 0:
        str_code = ''
        code_lengh = 20
        while code_lengh > 0:
            random_code = random.choice(str)
            str_code = str_code + random_code
            code_lengh = code_lengh - 1
        print str_code
        count_number = count_number -1
count_code(count_number)


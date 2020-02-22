#! /usr/bin/env python3
import re,pyperclip

len_re = re.compile(r'.{8,}') #[a-zA-Z0-9]{8,}避免非法字符
a_re = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
num_re = re.compile(r'\d')

def checkPW(PW):
    if len_re.search(PW) and a_re.search(PW) and num_re.search(PW):
        print('your password is safe')
    else:
        print('please check your password')

PW = str(pyperclip.paste())
checkPW(PW)

#sample hdazf31498H 232424


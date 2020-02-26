#!/usr/bin/env python3
#pw.py - An insecure  pawword locker program.

Passwords = {'email':'12345@123.com',
             'blog':'blog123',
             'luggage':'123'}

import sys,pyperclip
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: ", str(sys.argv))
print ("The arguments are: ", sys.argv[1:])
if len(sys.argv)<2:
    print('Usage:python pw.py[account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Password for' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)

#sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键。
    #外部参数可以是多个，获得的是一个列表（list)，所以才能用[]提取其中的元素，还可以提取切片。
    #其第一个元素是程序名称，随后才依次是外部给予的参数，以空格相连

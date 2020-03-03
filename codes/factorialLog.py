#! /usr/bin/env python3

import logging
logging.basicConfig(filename='factorialLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
                    
logging.debug('Start of program')#一次调用

def factorial(n):
    logging.debug('Start of factorial(%s)' % n) #二次调用
    total = 1
    for i in range(1,n + 1):
          total *= i
          logging.debug('i is ' + str(i) + ', total is ' + str(total))#循环调用
    logging.debug('End of factorial(%s)' % n)#循环结束调用
    return total

print(factorial(5))
logging.debug('End of program')#最后调用


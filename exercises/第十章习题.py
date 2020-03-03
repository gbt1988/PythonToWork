10.7 习题
 1.写一条 assert 语句，如果变量 spam 是一个小于 10 的整数，就触发 AssertionError。
assert(spam >= 10,'The spam variable is less than 10')
 2.编写一条 assert 语句，如果 eggs 和 bacon 包含的字符串彼此相同，而且不论大小写如何，就触发 AssertionError
assert(eggs.lower()!= bacon.lower(),'The eggs and bacon variables are the same!')
assert(eggs.upper()!=bacon.upper(),'The eggs and bacon variables are the same!')
 3.编写一条 assert 语句，总是触发 AssertionError
assert(False,'This assertion always triggers')
 4.为了能调用 logging.debug(), 程序中必须加入哪两行代码？
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
 5.为了让 logging.debug()将日志消息发送到名为 programLog.txt的文件中，程序必须加入哪两行代码？
import logging
logging.basicConfig(filename = 'programLog.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(messages)s')
 6.5 个日志级别是什么？
DEBUG,INFO,WARNING,ERROR,CRITICAL
 7.你可以加入哪一行代码，禁用程序中所有的日志消息？
logging.disable(logging.CRTICAL)
 8.显示同样的消息，为什么使用日志消息比使用 print()好？
可以禁用日志消息，不必删除日志函数调用。可以选择禁用低级别日志消息。可以创建日志消息。日志消息提供了时间戳。
 9.调试窗口中的 step over 和 out 有什么区别？
Step 让调试器进入函数调用，Over 将快速执行函数调用 不会单步进入其中，OUT 将快速执行余下的代码，直到走出当前所处的函数。
 10.点击调试窗口中的 go 按钮，调试器何时会停下来？
点击 go 后，调试器在程序末尾或断点处停止。
 11.什么是断点？
断点设在一行代码上，在程序执行到达该行时，它导致调试器暂停。
 12.在 IDlE中，如何在一行代码中设置断点？
右键点击选择 setbreakpoint

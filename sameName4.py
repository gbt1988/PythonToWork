def spam():
    print(eggs) #error!
    eggs = 'spam local'
eggs = 'global'
#spam()  #调用函数的 print 和函数外的 print 是不一样的,调用函数如果被识别为局部变量，则不能引用全局变量
print(eggs)

def func(list):
    for i in range(len(list)):
        if i < len(list)-2:
            print(list[i] + ' ' +',',end = ' ')
            #return list[i] + ' ' +','
        elif i == len(list)-2:
            print(list[len(list)-2] + ' ' + 'and', end = ' ')
            #return list[len(list)-2] + 'and' + ' '
        elif i == len(list)-1:    
            print(list[len(list)-1],end = ' ')
            #return list[i]
            
spam = ['apples','bananas','tofu','cats']
result = func(spam)

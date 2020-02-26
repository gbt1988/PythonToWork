#sum = 0
#for i in range(0,101):
#    print('当 i等于' +str(i) + '时,'+ '这是第'+ str(i+1) + '次循环')
#    print(str(sum) +'+'+ str(i))
#    sum = sum + i
#    print('等于'+str(sum))
#print(sum)

b = 0
for i in range(0,101):
    a = b + i
    print('当 i 等于'+str(i)+'时,'+'这是第'+str(i+1)+'次循环'+',0到'+str(i-1)+'总和为'+str(b) + '，i为' + str(i))
    b = a
    print('总和为'+str(a))
print(a)


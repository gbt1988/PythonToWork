catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + '(or enter nothing to stop)')
    name = input()
    if name == ' ':
        break
    catNames = catNames + [name] #list concatenation
print('The cat names are:')


#for name in range(len(catNames)):
#    print('catname'+ str(name + 1) + ' ' + catNames[name])

for i in range(5):
    print('catename' + str(i+1) + ' ' +catNames[i])

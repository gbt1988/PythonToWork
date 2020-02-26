def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    elif number%2 == 1:
        print(3*number + 1)
        return 3*number + 1

print('Please input an int')
try:
    num =int(input())
    while True:
        collatz(num)
        num = collatz(num)
        if collatz(num) == 1:
            break
except:
    print('you should input an int')

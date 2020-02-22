theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)#输出初始上一步状态
    print('Turn for ' + turn + '.Move on which space?')#输出提示
    move = input()
    theBoard[move] = turn#操作键值，并不打印结果，在下一轮作为初始状态打印出
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'#改变操作者，但并未改变字典
    #printBoard(theBoard)#放在这里的话，每一步都输出
    print(i)
printBoard(theBoard)#循环结束后输出最后改变后的结果。
#print(i)

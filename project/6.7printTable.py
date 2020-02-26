#! usr/bin/env python3

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


def tablePrint(tableDate):  
    columnWidth=[] #确定每列的宽度 
    for k in range(len(tableDate)):#列表中的每个子列表，分别求出每个子列表下的最长字符串的长度，再加 1
        length=len(tableDate[k][0]) #第 k 个子列表-即第k行的第1个字符串的长度
        for v in range(len(tableDate[0])):
            if len(tableDate[k][v])>length:
                length=len(tableDate[k][v])       
        length+=1
        columnWidth.append(length)                    
    for k in range(len(tableDate[0])):#排版对齐     
        new=tableDate[0][k].rjust(columnWidth[0])+' '
        for v in range(1,len(tableDate)):
            new=new+tableDate[v][k].ljust(columnWidth[v])
        print(new)
tableDateOne=[['apple','oranges','cherries','banana'],
           ['alice','bob','carol','david'],
           ['dogs','cats','moose','goose']]       
tablePrint(tableData)

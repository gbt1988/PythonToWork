def chart(g):
    #x = len(g)  #纵向的列表数;图的每一列，对应列表的每一行，y是固定的
    #y = len(g[0])#横向的列表项数;图的每一行，对应列表的每一列，x是固定的
    for x in range(len(g[0])):
        #对每一行进行循环,每行对应表中一列，该行对应列表中的横坐标x是确定的
        #每一行确定了，即x确定了，横坐标确定了，只要循环出该行每一列，对应的列表中的纵坐标y即可。
        #图中第x行，对应列表中第 x 列;位置对应列表中位置y。
        for y in range(len(g)): #第x行第y列的值是 g[y][x]，第0行的值是 g[y][0]
            #第 1 行的值得是 g[y][1]
            print(g[y][x] ,end = ' ')
        print(' ')
        #print(g[i])
grid = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]
chart(grid)

#对 grid



#g(0,0)g(1,0)g(2,0)g(3,0)g(4,0)g(5,0)g(6,0)g(7,0)g(8,0)
#g(0,1)g(1,1)g(2,1)g(3,1)g(4,1)g(5,1)g(6,1)g(7,1)g(8,1)
#g(0,2)g(1,2)g(2,2)g(3,2)g(4,2)g(5,2)g(6,2)g(7,2)g(8,2)
#g(0,3)g(1,3)g(2,3)g(3,3)g(4,3)g(5,3)g(6,3)g(7,3)g(8,3)
#g(0,4)g(1,4)g(2,4)g(3,4)g(4,4)g(5,4)g(6,4)g(7,4)g(8,4)
#g(0,5)g(1,5)g(2,5)g(3,5)g(4,5)g(5,5)g(6,5)g(7,5)g(8,5)
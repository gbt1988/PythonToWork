def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items + str(item_total)')#循环内,循环完打印

def addToInventory(inventory,addedItems):
    count={}
    for a in addedItems:
            count.setdefault(a,0)
            count[a] += 1
    print(count)
    for k,v in count.items():
            if k in inventory:
                inventory[k]=inventory[k] + count[k]
            else:
                inventory.setdefault(k,count[k])
                #inventory[k]=count[k]这两个写法都行
            
    return inventory
inv = {'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv,dragonLoot)
#displayInventory(inv)
print(inv)

#或者以下：
#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#def displayInventory(inventory):
#    print("Inventory:")
#    item_total = 0
#    for k, v in inventory.items():
#        print(str(v) + ' ' + k)
#        item_total += v
#    print("Total number of items: " + str(item_total))
# displayInventory(stuff)

#def addToInventory(inventory, addedItems):
#    for i in addedItems:
#        if i in inventory:  i 既可以是字典 b 的键，也可以是字典 a 的键，都可以用 in 查询。
#            inventory[i] += 1 可以直接按照字典 b 中的键名，找到字典 a 中的同名键，直接更改键值。
#        else:                 这里是按照列表中的元素名，查看是否同时是字典的键名。
#            inventory[i] = 1
#    return inventory

#inv = {'gold coin': 42, 'rope': 1}
#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#inv = addToInventory(inv, dragonLoot)
#displayInventory(inv)

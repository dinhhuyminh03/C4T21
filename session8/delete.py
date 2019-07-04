items = ['pho', 'com', 'chao', 'pho xao']
# i = int(input("Enter index: "))
# items.pop(i)
# print(*items, sep = ',')

o = input("Enter a item you want to delete: ")
items.remove(o)
print(*items, sep = ',')

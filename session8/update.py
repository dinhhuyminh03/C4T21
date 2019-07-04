items = ['Sport', 'LOL', 'BTS']
print(items)
items[1] = input("Replace: ")
items[2] = 'LMAO AYYY'
print(*items, sep = ',')
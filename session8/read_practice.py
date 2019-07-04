items = ['sport', 'LOL', 'BTS']
# new_item = input("Enter a hobby: ")
# items.append(new_item)
# print(*items, sep = ',')

# index1 =items[0]
# x = index1.upper()
# print(x)
# print(items[1])
# print(items[2])
items[1] = 'ACC'
print(*items, sep = ',')
if 'LOL' not in items:
    print("LOL is not available in the list.")
else:
    items.remove('LOL')
    print("LOL has been deleted.")

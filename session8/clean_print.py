items = ['Sport', 'LOL', 'BTS']
print(*items, sep = '|')
new_item = input("Enter a hobby: ")
items.append(new_item)
print(*items, sep = '|')


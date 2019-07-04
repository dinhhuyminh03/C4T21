hobby = ['play game', 'read book', 'go fishing', 'play sports']
for i in range(len(hobby)):
    print(hobby[i])
a = "Press 1 if you want to add another hobby to the list."
b = "Press 2 if you want to print the list out."
c = "Press 3 if you want to update the list and make a change in the list."
d = "Press 4 if you want to delete a hobby from the list"
print(a)
print(b)
print(c)
print(d)
create = 1
read = 2
update = 3
delete = 4

crud = int(input("Press the number you want to do: "))
if crud == 1:
    new_item = input("Enter a hobby to the list: ")
    hobby.append(new_item)
    print(*hobby, sep = ',')
elif crud == 2:
    print(*hobby, sep = ',' )
elif crud == 3:
    for i, item in enumerate(hobby):
        print(i + 1, ".", item)
    g = int(input("Enter the hobby you want to change: "))
    if g == 1:
        hobby[0] = input("Enter a new hobby to replace this hobby:")
        print(*hobby, sep = ',' )
    elif g == 2:
        hobby[1] = input("Enter a new hobby to replace this hobby:")
        print(*hobby, sep = ',' )
    elif g == 3:
        hobby[2] = input("Enter a new hobby to replace this hobby:")
        print(*hobby, sep = ',' )
    else:
        hobby[3] = input("Enter a new hobby to replace this hobby:")
        print(*hobby, sep = ',' )
else:
    k = int(input("Enter index: "))
    hobby.pop(k)
    print(*hobby, sep = ',' )



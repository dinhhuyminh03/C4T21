high_scr = [45, 56, 67, 78]
high_scr.sort(reverse = True)
for i, item in enumerate(high_scr):
    print(i + 1, ".", item)
new_high_scr = int(input("Enter your new high score: "))
high_scr.append(new_high_scr)
high_scr.sort(reverse = True)
for i, item in enumerate(high_scr):
    print(i + 1, ".", item)

import random
print("True = 1")
print("False = 0")
true = 1
false = 0
diem = 0
# ans = int(input("Is it true or false ?"))py
while True:
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    d = random.randint(-1, 1)
    print("d : ",d)
    c = a + b +d
    print (f"{a} + {b} = {c}")
    if d == 0:
        ans = int(input("Is it true or false ?"))
        if ans == 1:
            print("Correct")
            diem = diem + 1
        else:
            print("false")
            print(diem)
            break
    else:
        ans = int(input("Is it true or false ?"))
        if ans == 1:
            print("False")
            print(diem)
            break
        else:
            print("True")
            diem = diem + 1
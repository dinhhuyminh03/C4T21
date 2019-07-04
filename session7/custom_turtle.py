x = int(input("nhap1: "))
y = int(input("nhap2: "))

from turtle import *
shape("turtle")
speed(-1)
for i in range (360):
    left(x)
    forward(y)
mainloop()
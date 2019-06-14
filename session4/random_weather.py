import random
r1 = random.randint(0,100)
print(r1)
if r1 < 30:
    print("Rainy")
elif 30<= r1 <60:
    print("Cloudy")
else:
    print("Sunny")
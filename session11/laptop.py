laptop = {
    "HP": 20,
    "DELL": 50,
    'MACBOOK': 12,
    'ASUS': 30,
    'TOSHIBA': 10,
}
laptop["DELL"] = 60
laptop["MACBOOK"] = 2
laptop["FUJITSU"] = 15
laptop["ALIENWARE"] = 5
print(laptop)
a = input("Enter the brand of laptop you want to check the stock: ")
if a in laptop:
    print("The number of laptops of that brand in stock is", laptop[a])
print("The number of laptop in stock is: ", sum(laptop.values()))

b = input("Enter the brand of laptop you want to buy: ")
if b in laptop:
    c = int(input("How many laptops of that brand do you want to buy ?"))
d = laptop[b] - c
print("That brand you bought in stock now has: ", d)


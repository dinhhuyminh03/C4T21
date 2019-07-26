price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000,
}
print(price)
a = input("Enter a brand you want to check the price: ")
print("The price of the brand you entered is: ", price[a])
order = int(input("How many laptops do you want to buy ?"))
pri = order*price[a]
print("The price you have to pay is: ", pri)
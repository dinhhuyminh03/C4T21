laptop = {
    "HP": 20,
    "DELL": 60,
    'MACBOOK': 2,
    'ASUS': 30,
    'TOSHIBA': 10,
    'FUJITSU': 15,
    'ALIENWARE': 5,
}
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
print("The laptop prices are listed below: ")
for k,v in laptop.items():
    print (k,v, sep = ":")
    
    if k in price:
        gia = v*price[k]
        print(k, gia, sep = ":")
        

meaning ={
    "raichu": "raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.",
    "onix": "Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.",

}
print(meaning)
finding = input("Enter a key value you want to find more information: ")
while True: 
    if finding in meaning:
        if finding == "raichu":
            print(meaning["raichu"])
        elif finding == "onix":
            print(meaning["onix"])
    else:
        print("Invalid key value !")



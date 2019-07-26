chracter = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf', 'Flint Stone'],
    'Gold': 150,
    'Level': 2,
    'Pocket': ['Monster Dex', 'Flashlight']
}
print("The description of the chracter is: ", chracter, sep = ":")

skill1 = {
    'Name':'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3,
}
skill2 = {
    'Name': 'Quick Attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,
}
skill3 ={
    'Name':'Strong Kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2,
}
print("The skills you can use in combat are: ")
print("Skill 1 is: ")
for i, (k, v) in enumerate(skill1.items()):
    print(i+1,".", k ,v )
print("Skill 2 is: ")
for i, (k, v) in enumerate(skill2.items()):
    print(i+1,".", k ,v )
print("Skill 3 is: ")
for i, (k, v) in enumerate(skill3.items()):
    print(i+1,".", k ,v )

# skill1 = 1
# skill2 = 2
# skill3 = 3
a = int(input("Enter the skill you want to use: "))
import random
r1 = random.uniform(0,1)
if a == 1:
    if chracter["Level"] >= skill1["Minimum level"]:
        if r1 < skill1['Hit rate']:
            print("You have hit the enemy with the damage of", skill1['Damage'])
        else:
            print("You have missed the enemy !")
    else:
        print("You have not reach the required level to use the skill !")
elif a == 2:
    if chracter["Level"] >= skill2["Minimum level"]:
        if r1 < skill2['Hit rate']:
            print("You have hit the enemy with the damage of", skill2['Damage'])
        else:
            print("You have missed the enemy !")
    else:
        print("You have not reach the required level to use the skill !")
else: 
    if chracter['Level'] >= skill3["Minimum level"]:
        if r1 < skill3['Hit rate']:
            print("You have hit the enemy with the damage of", skill3['Damage'] )
        else:
            print("You have missed the enemy !")
    else:
        print("You have not reach the required level to use the skill !")









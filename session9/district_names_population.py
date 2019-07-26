district = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
l = len(district)
for i in range(l):
    print(district[i])

population = [150300, 247100, 333300, 266800, 420900, 318000]
print("The according population of these districts are: ")
print(*population, sep = "\n")
print("The highest value of population is:", max(population))
print("The lowest value of population is:", min(population))
print("The district with the highest value of population is: DD, with", max(population))
print("The district with the lowest value of population is: ST, with", min(population))
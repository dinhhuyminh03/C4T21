area = ['117.43', '9.224', '43.35', '12.04', '9.96', '10.09']
l = len(area)
print("The area according to the list of population are: ")
for i in range(l):
    print(area[i])

population = [150300, 247100, 333300, 266800, 420900, 318000]
f = len(population)
print("The according population of these districts are: ")
print(*population, sep = "\n")
print("The according population density of these districts are: ")
for i in range(f):
   p = population[i]
   a = float(area[i])
   b = p/a  
   print(b)
avg_den = sum(population) / 6
print("The average population density is: ", avg_den)
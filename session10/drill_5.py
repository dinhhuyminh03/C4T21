

p1 = {
    'name':'Huy',
    'role':'waiter',
    'hours':12,
    'salary per hour': 0.8,
}

p2 = {
    'name':'Tung',
    'role':'cook',
    'hours':24,
    'salary per hour': 1.5,
}

p3 = {
    'name':'M.Duc',
    'role':'manager',
    'hours':20,
    'salary per hour': 2,
}
person_list = [p1, p2, p3]
print(person_list)
print(person_list[2])


s1 = 12*0.8*30
s2 = 24*1.5*30
s3 = 20*2*30

salary = [s1, s2 ,s3]
print(salary)
total_salary = s1 + s2 + s3
print(total_salary)
book = {
    'name': 'The Great Gatsby',
    'publish date': 'April 10th 1925',
    'chracters in the book': ['Jay Gatsby', 'Nick Carraway', 'Daisy Buchaanan']
}
book['author'] = 'F. Scott Fitzgerald'

del book['name']
for k,v in book.items():
    print(k, v, sep = "-")
a = book['chracters in the book']
print(*a, sep = ',')
for k,v in book.items():
    print(k, v, sep = "-")
print("Which chracter is in the book ?")
chracter = {
    "a": 'Jay Gatsby',
    "b": 'John Wick',
    "c": 'Mr.Bean',
    "d": 'All of the above',
}
for k,v in chracter.items():
    print(k, v, sep = "-")
diem = 0
while True:
    ans = input("Enter the correct answer: ")
    if ans == "a" in chracter:
        print("Correct !")
        diem = diem + 1 
        print("Your point now is: ", diem)
        break
    elif ans == "b" in chracter:
        print("Wrong answer please try again")
        break
    elif ans == "d" in chracter:
        print("Wrong answer please try again")
        break
    else:
        print("Wrong answer please try again")
        break

print("Who is the author of the book ?")
author = {
    "a": "F. Scott Fitzgerald",
    "b": "Herman Melville",
    "c": "Ernest Hemmingway",
    "d": "William Golding"
}
for k,v in author.items():
    print(k, v, sep = "-")
while True:
    ans2 = input("Enter the correct answer: ")
    if ans2 == "a" in author:
        print("Correct !")
        diem = diem + 1
        print("Your point now is: ", diem)
        break
    elif ans == "b" in chracter:
        print("Wrong answer ")
        break
    elif ans == "c" in chracter:
        print("Wrong answer ")
        break
    else:
        print("Wrong answer ")
        break
    
per = diem*100/2
print("Your percentage of correct answer is: ", per)

 
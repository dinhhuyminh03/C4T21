import random
word_list = ['cat', 'water', 'hot', 'cold', 'book', 'newspaper', 'dog', 'corn', 'clean', 'create']
random_word = random.choice(word_list)
shuffled = list(random_word)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print("The word has been shuffled from the list is: ", shuffled)
answer = input("Enter the correct word: ")
if answer == random_word:
    print("The correct word is: ", random_word) 
    print("You have the correct answer !")
else: 
    print("The correct word is: ", random_word) 
    print("You have the wrong answer !")
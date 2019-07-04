while True:
    import random
    word = input("Enter a word to shuffle it: ")
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print (shuffled)
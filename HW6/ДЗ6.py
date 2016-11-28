word = input('Type in a word: ')
for i in range(len(word)  , 0, -1):
    print(word[i:] + word[:i])
    

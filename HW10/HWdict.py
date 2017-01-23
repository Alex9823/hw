import random
def dict(words):
    with open("new1.csv", 'r', encoding = "utf-8") as f:
        puzzle = {}
        word = []
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip('\n')        
        for i in range(len(lines)):
            word = lines[i].split(',')
            puzzle[word[0]] = word[1]
        return(puzzle)

def main():
    puzzle = dict('new1.csv')
    for noun in puzzle:
        a=('')
        for i in range(len(noun)):
           a=('.'+a)
        print(puzzle[noun], a)
        a=input('Отгадайте слово:')
        if a ==noun:
            print('Молодец!')
        else:
            print('Не угадал, попробуй еще раз!')
        return()
a=main()
print(a)

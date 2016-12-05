##with open('word_game.txt', 'w', encoding='utf-8') as f:
##    f.write(n+'/n'+b+'/n'+c+d+e)

with open('information.txt', 'w', encoding = 'utf-8') as n:
    name = input('Введите Имя: ')
    n.write(name+'\n')
    age = input('Введите возраст: ')
    n.write(str(age)+'\n')
    color = input('Введите любимый цвет: ')
    n.write(color+'\n')
    musician = input('Ведите любимого музыкального исполнителя: ')
    n.write(musician+'\n')
    dream = input('Введите мечту: ')
    n.write(dream+'\n')

with open('information1.txt','r', encoding = 'utf-8') as f:
    info = f.readlines()
    for line in range(len(info)):
        info[line] = info[line].strip()
    response = input('Как Вашего соседа зовут? ')
    if response == info[0]:
        print('Правильно!')
    else:
        print('Нет, его зовут '+info[0]+'.')
    response = input('Сколько Вашему соседу лет? ')
    if str(response) == info[1]:
        print('Правильно!')
    else:
        print('Нет, ему '+info[1]+' лет.')
    response = input('Какой у Вашего соседа любимый цвет?')
    if response == info[2]:
        print('Правильно!')
    else:
        print('Нет, его любимый цвет - '+info[2]+'.')
    response = input('Какой у Вашего соседа любимый исполнитель?')
    if response == info[3]:
        print('Правильно!')
    else:
        print('Нет, его любимый исполнитель - '+info[3]+'.')
    response = input('Какая у Вашего соседа мечта?')
    if response == info[4]:
        print('Правильно!')
    else:
        print('Нет, его мечта - '+info[4]+'.')
    

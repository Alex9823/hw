import re
#regex = '<.*?>'
#text='<p>Hello, World!</p>'
#re.sub(regex, '', text)
##Comprehensions

a=[1,2,3,4,5,6,66]
b=[]
for i in a:
    if i< 10 and i%2==0:
        b.append(i**2)

new_b=[i**2 for i in a if  i< 10 and i %2==0]
    
#print(b)
new_b=[i**2 for i in a]
#print(new_b)
words =['Mary','John']
new_words=[w.upper() for w in words]
#print(new_words)

other_words=[w.upper() for w in words if re.search('[aAjJ]', w)]
print(other_words)

## Dict Comprehension
d={"Корова": "му", "собака": "гав" }
sounds={d[key]: key for key in d if len(key) > 4}
print (sounds)

## Массив массивов
BIG=[a, new_b, words]
print(BIG)
flat=[]
for arr in BIG:
    for item in arr:
        flat.append(item)
print(flat)
flat1=[item for arr in BIG for item in arr]
print(flat1)


#s='", World! thats all folks!"
#s.capitalize#Hello, {} {}!'.format('Петя', 'Иванов')
#template.format('John')
#template.format(input('Введите имя: '))
#'Hello, {1} {0}, you {} are our'.format('Петя', 'Иванов')





template='Возраст: {:>10}'
for i in a:
    print(template.format(i))
# можно вместо > поставить ^
print('{:+>10}'.format('text'))

pi=3.14159265
print('Ваще число {:.2f}'.format(pi))

#pyformat.info

##Задания
##написать функцию align_right(), которая получает на вход массив слов и распечатывает их в столбик выравненными справа.

def allign_right():
    words =['Mary','John', 'Окунь и Санчоус', 'Пик']
    for i in words:
        print('{:>15}'.format(i))
allign_right()








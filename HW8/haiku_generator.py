##Текст должен представлять собой правильное хайку, то есть стихотворение
##на одном из изучаемых вами языков (французский, испанский) из трёх строк
##без рифмы, при этом длина первой строки должна быть 5 слогов,
##второй строки - 7 слогов, третьей строки - 5 слогов.
##Количество предложений в таком тексте может быть любым.

import random

def haiku_generator():

    def word1():
        with open('haiku.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)

    def word2():
        with open('wrd1.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    def word3():
        with open('wrd4.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    def word4():
        with open('wrd2.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    def word5():
        with open('wrd3.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    def word6():
        with open('wrd6.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    def word7():
        with open('wrd5.txt','r', encoding = 'utf-8') as f:
                word = f.read()
                a = word.split(' ')
                return random.choice(a)
    a=word1()
    b=word2()
    c=word3()
    d=word4()
    e=word5()
    f=word6()
    g=word7()

    line1= a+' '+b
    line2=c+' '+d+' '+e
    line3=f+' '+g

    result=line1+','+'\n'+line2+' '+'-'+'\n'+line3+'.'
    return(result)
a=haiku_generator()
print(a)

    

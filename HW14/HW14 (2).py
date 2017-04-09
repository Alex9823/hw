#4. Создать словарь, в котором ключами являются предложения, а
#в качестве значения выступает словарь с ключами-словами и значениями-длинами слов (например,
#{"Мама вымыла раму": {"Мама": 4, "вымыла": 6, "раму": 4}, ...}).


import re

def opentext(text):
    sentences = []
    with open (text, 'r', encoding = 'utf-8') as t:
        newtext = t.read()
   
        word=newtext.strip('”“".,!?')
        word=word.split()
    return word
print(opentext('т.txt'))


def form(text):

    key=opentext(text)
    freq = {}

    for i in key:
        for k in range(len(i)):
        
            n = k+1
            freq[i] = n
    print (freq)

def main():
    form('т.txt')
    
if __name__ == '__main__':
    main()

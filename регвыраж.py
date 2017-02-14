#массив кортежей (tupple)
#пишутся в круглых скобочках, их нельзя изменять после создания(также ведут себя строки)
#dic[(1,2,3)]=u'питон'кортеж может быть ключом словаря hashable (можно положить в словарь)
#dic[u'my']=25
#split возвращает картежи
#
#def func():
#    return 1,2,3
#print(func())
#>>(1,2,3)
#a,b,c=func
# замена функция sub
# m=re.sub(r'[^;]+',r'',s) первое это рег выр, второе замена, третье -строка для изменения
#[^;]+ это все что не ;, больше ноля
#re.search результат - переменная match
#findall - массив или массив картежей
#sub - cтрока
#m=re.sub(r'\b[Кк]ош?ек', r'собак',s)
#text=...m)
#написать две замены, для больших буква и маленьких
#когда мы экранируем нужен r'\w+' равно '\\w+'
#\b - граница слова
#обратные ссылки
#m=re.sub(r'(\\w+) \\1', r'\\1',s, flags=re.DOTALL)заменияет 2 одинаковых слова на одно этот флаг включает \n его можно вставлять в любые функции модуля re
# флаги изменяют поведение регулярного выражения
#m=re.sub(r'(\\w+)', u'\\1 \\1',s)
#m=re.sub(u'[иео]'.'[иео]')
#[^\w]+=\W
#[\W0-1]
#m=re.sub(r'<.*?>', u'', flags=re.DOTALL)
#\s tab

import re
def open_html(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        content=f.read()
    return content

def find_links(content):
    m=re.sub(r'<.*?>',r' ', content)
    s=re.sub(r'\s+', r' ', m)
    d=re.sub(r'Стив Джобс', r'Феечка Винкс',s)
    return d
text=open_html('steve.html')
a=find_links(text)
print(a)

def syllable ():
    m=re.sub(r'[бвгджзклмнпрстфхцчшй][оаеи][]',)


Kriik

import re

def readtext():
    with open(input('Введите путь к файлу: '), 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text


def normaltext(text):
    ##обрезает у словоформ в массиве всякие знаки препинания, включая тире, сводит все
    ## словоформы к нижнему регистру и возвращает массив словоформ
    arr = []
    text = re.sub(r'—\s?', r' ', text)
    text = text.split()
    for i in range(len(text)):
        word = text[i].strip('.,?()":')
        arr.append(word.lower())
    return arr


def countwords(wordlist):
    ## 1 задание. Открыть файл, посчитать словоформы
    countall = len(wordlist)
    print('Число слов', countall)


def freqdict(text):
    ##Возвращает словарь, в котором ключи слова, а значения - их частотность в тексте
    freq = {}
    for i in text:
        n = text.count(i)
        freq[i] = n
    return freq


def delete_doubles(d):
    ##удаляет повторы из словаря
    nd = {}
    a = sorted(d.keys())
    for key in a:
        if key not in nd.keys():
            nd[key] = d[key]
    return nd


def writedict(wordlist):
    ## 2 задание. Посчитать частотность словоформ, создать словарь "слово - частота", записать его в .csv
    fdict = delete_doubles(freqdict(wordlist))
    s = sorted(fdict.keys())
    file = open(input('Введите путь к csv файлу: '), 'a', encoding = 'utf-8')
    for word in s:
        file.write(word+','+str(fdict[word])+'\n')
    file.close()

    
def main():
    wordlist = normaltext(readtext())
    countwords(wordlist)
    writedict(wordlist)

   
main()


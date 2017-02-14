import re
##№1
def readtext():
    with open('f.xml', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    return text
#input('Введите путь к файлу: ')
def countlines():
    a=readtext ()
    b=len(a)
    print(b)
    b=str(b)
    with open ('a.txt', 'w', encoding = 'utf-8') as l:
        l.write('Количество строк в файле - '+b+'.')
countlines()
##№2
def make_keys():
    a=str(readtext ())
    #print(a)
    k =re.findall('type="(?:.|\n)+?"', a)
    k=str(k)
    key=re.sub('(type="|"|)', r'',k)
    #key=str(key)
    key=re.sub('punctuation', r'',key)
    key=re.sub(r'([|]|,)', r'',key)

    key=key.split(' ')
    return key
def writedict():
    key=make_keys()
    freq = {}

    for i in key:
        n = key.count(i)
        freq[i] = n
    print(freq)
    a=freq.keys()
    a=str(a)
    with open ('a.txt', 'w', encoding = 'utf-8') as l:
        l.write('/n Ключи: '+a)
writedict()

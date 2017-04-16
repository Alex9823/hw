#Программа должна просмотреть все папки и файлы, находящиеся в
#одной папке с ней, и сообщить
#4.Сколько найдено файлов, название которых состоит только из латинских символов.
import re
import os
import shutil
f_name=os.listdir('.')
f_name.remove('15.py')
a=len(f_name)
print(f_name)
latt = '[A-Za-z]*'
s = '[А-Яа-яЁё\.\?!0-9"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'

names = []
for f in os.listdir('.'):
        if os.path.isdir(f) and re.search(latt, f) and re.search(s, f) == None:
            names.append(f)
print(names)

kir = '[А-Яа-яЁё\.\?!0-9"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]*'
lat = '[A-Za-z]'
nn = []
for f in os.listdir('.'):
    if os.path.isdir(f) and re.search(kir, f) and re.search(lat, f) == None:
        nn.append(f)
print(nn)
k=len(nn)
l=len(names)
res=a-l-k
print(l)

files = []
name = '.*\.'
for s in os.listdir('.'):
    if os.path.isdir(s) and s not in files:
        files.append(s)
    elif os.path.isfile(s) and re.search(name, s):
        n = re.search(name, s).group(0)
        n = n.strip('.')
        if n not in files:
            files.append(n)
print("Вот названия всех найденных в текущей папке файлов и папок: ")
#for s in files:
print(files)

    


if names == []:
    print("В текущей папке нет папок, название которых состоит только из кириллических символов.")
else:
    print("В данной папке "+ str(res) +" файл(а), название которого(ых) состоит только из латинских символов.")

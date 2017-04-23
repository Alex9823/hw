# на какую букву начинается название большинства папок
#(если таких много, можно печатать только одну);



import os

letters=[]
s =  os.listdir('.')

a=''
l = len(s)
for i in range(len(s)):
    letters.append(s[i][0])
    a=a+(s[i][0])
     



freq=[]
dic={}
for i in letters:
    n = a.count(i)
    dic[i]=n
    
f=0
maxkey=''
for key in dic.keys():
    if dic[key]>f:
        f=dic[key]
        maxkey=key
print('Большинство папок начинаются на букву ' + maxkey+ '.')



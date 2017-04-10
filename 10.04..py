#Пользователь вводит предложение на английском языке,
#и программа создает вложенные друг в друга папки,
#так чтобы путь к самой глубокой из них составлял введенное предложение.
#Например, если пользователь ввел предложение
#"It is a wonderful day", программа должна создать вложенные папки,
#и путь к последней из них должен быть "it/is/a/wonderful/day"
import os
import shutil
#a=input('Type in something: ')
#f_name=a.replace(' ','\\')
#os.makedirs(f_name)
n=int(input('bbb: '))

for i in range (1,n+1):
     
    os.mkdir(str(i))
    for j in range(1,i):
        open(str(j),'w')

#работа с папками и файлами
# os (module) shutil
#jupiter notebook
import os
import shutil
#with open(f)
#Windows C: \\Users\\ student\\Downloads
#Mac:/home/student/downloads
#папкав которой лежит программа текущая
print(os.path.abspath('.'))
#print(os.getcdwd())
os.path.join('1.txt','2txt')
#f=''texts\\1.txt
# ''join('Hello', 'world')
os.path.exists('text name')
os.listdir('.')
s='Hello'
i=1
for f in os.listdir('.'):
    if f.endswith('txt'):
        with open(f, 'a', encoding='utf-8') as w:
            w.write(s*i)
            i+=1

#os.mkdir('crpus')
#os.makedirs('a\\long\\path')#вложенные папки
#os.rename('corpus','newcorpus')
#os.rename('text')#rename files
print(os.path.isfile('22'))
print(os.path.isdir('22'))

#shutil.copy('11.txt', 'newcorpus\\1.txt')
#shutil.copytree('text', 'crpu')
#shutil.move('text','a')
#os.remove('newcorpus\\1.txt')
#shutil.rmtree('a')
            

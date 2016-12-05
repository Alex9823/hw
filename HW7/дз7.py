#Программа должна открывать файл с русским текстом в utf-8 и
#сообщать про него следующую информацию (по вариантам):
# какой процент от общего количества слов не оканчивается знаком препинания
#(можно взять только запятую и точку);
word=[]
with open('doc.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    sign = 0
    word = text.split(' ')
    n=len(word)
    print(n)
    for i in word:
       if i.endswith('.') or i.endswith(',') :
            sign+=1
    q=sign/n*100
    result=100-q
    print('Знаком препинания заканчиваются ' + str(result) + '% слов.')

   
       
        

 


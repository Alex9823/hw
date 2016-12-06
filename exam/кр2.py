elem = []
with open('freq1.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    elem = text.split('\n')
f = []
summ = 0
word = ''
gram = ''
ipm = ''
for i in range(len(elem)):
    if 'сущ' in elem[i] and  'жен' in elem[i]:
        f.append(elem[i])
        word, gram, ipm = elem[i].split('|') 
        summ += float(ipm)
for i in range(len(f)):
    print(f[i]+',')
print(summ)

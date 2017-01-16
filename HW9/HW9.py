s=[]
freq=[]
def opentext(text):
    words = []
    with open (text, 'r', encoding = 'utf-8') as t:
        newtext = t.read()
    newtext = newtext.lower()
    words = newtext.split()
    for i in range(len(words)): 
        words[i] = words[i].strip('”“".,!?')
    return words
text=input('Type in a file name: ')
a=opentext(text)


def ending1(ed):

    c=opentext(text)    

    freq=0
    for i,w in enumerate (c):
        if c[i].endswith('ed')==True:
            s.append(c[i])
            freq+=1
    return(freq)
b=ending1(freq)
b=str(b)
print('There are '+b+' verbs in the text that end with -ed.')

def ending2(ied):
    c=opentext(text)    
    freq=0
    for i,w in enumerate (c):
        if c[i].endswith('ied')==True:
            s.append(c[i])
            freq+=1
    return(freq)
l=ending2(freq)
l=str(l)
print(l+' of them are derived from verbs that end with -y .')

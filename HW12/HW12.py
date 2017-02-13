import re
def open_html(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        content=f.read()
    return content

f=[]
def find_links():
    a=open_html(input())
    links=re.findall('Научная сфера(?:.|\n)+?</td>', a)
    links=str(*links)                          
    li=re.sub('Научная(?:.|\n)+?title', r'',links)
    li=re.sub('<a href=(?:.|\n)+?title', r'',li)
    li =re.findall('title="(?:.|\n)+?"', links)
    print(li)

    for i,n in enumerate(li):
        a=str(li[i])
        a=a.lower()  
        a=re.sub('title="|"','',a)
        f.append(a)
    print(f)
    with open ('n.txt', 'w', encoding = 'utf-8') as l:
        for word in f:
            print(word)
    
            l.write(word+'\n')


a=find_links()

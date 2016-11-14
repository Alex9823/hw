a=[]
n=input()
while n!= '':
    if n.endswith('re') or n.endswith('ri'):
        a.append(n)
        n=input()
else:
    print(a)

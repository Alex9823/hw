lines=[]
with open('freq1.txt','r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        word =line.split('|')
        for i in word:
            if i.endswith('союз') or i.endswith('союз '):
                print (line)
    
    
 
   
        

    

import os 
import re 

def func(d, filename): 
    with open(filename,'w', encoding='utf-8') as f: 
        
        for key in d: 
            line = key + '\t' + str(d[key])+'\n' 
            f.write(line)
            
#print('dictionary successfully saved') 
    return 

def os_walk(): 
    d = dict() 
    path = '.\\news' 
    for root, dirs, files in os.walk(path): 
        for file in files: 
        #print(file) 
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f: 
                txt = f.read() 
                d[file] = txt.count('<se>') 
                func(d, 'sentencesnumber.csv') 

def main(): 
    os_walk()
    if __name__ == '__main__':
        main()

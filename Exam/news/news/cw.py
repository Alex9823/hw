import os 
import re 

def savedict(d, filename): 
    with open(filename,'w', encoding='utf-8') as f: 
        for key in d: 
            line = key + '\t' + str(d[key])+'\n' 
            f.write(line) 
#print('dictionary successfully saved') 
    return 

def task1(): 
    d = dict() 
    path = '.\\news' 
    for root, dirs, files in os.walk(path): 
        for file in files: 
        #print(file) 
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f: 
                txt = f.read() 
                d[file] = txt.count('<se>') 
                savedict(d, 'sentencesnumber.csv') 

def main(): 
    task1()
    if __name__ == '__main__':
        main()

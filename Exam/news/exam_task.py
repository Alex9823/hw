import re 
import os 
import csv 
def open(): 
    names = {} 
    tree = os.walk('news') 
    for root, dirs, files in os.walk('news'): 
        for f in files: 
            with open(os.path.join(root,f), 'r') as x: 
                texts = x.readlines() 
                sentences = 0
                for text in texts: 
                    if '/se' in text: 
                        sentences = sentences + 1 
                        names[f] = sentences 
                        main(names) 



def write():
    with open('amount of sentences.txt', 'w', encoding='utf-8') as f:
        for filename in file_texts_dict:
            text = file_texts_dict[filename]
            sent_am = open(text)
            f.writelines(filename+'\t'+str()+'\n')
     

def main(dict): 
    new = "" 
    with open("new.txt", "w", encoding="utf-8") as file: 
        for i in dict.keys(): 
            new += "\n" + i.strip() + "\t" + str(dict[i]) 
            file.write('result.txt') 
            open()




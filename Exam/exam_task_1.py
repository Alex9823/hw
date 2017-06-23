import re 
import os 
import csv 
def open(): 
    names = {} 
    tree = os.walk('news') 
    for root, dirs, files in os.walk('news'): 
        for f in files: 
            with open(os.path.join(root,f), 'r') as f0: 
                texts = f0.readlines() 
                sentences = 0 
                for text in texts: 
                    if '/se' in text: 
                        sentences = sentences + 1 
                        names[f] = sentences 
                        main(names) 
def main(dict): 
    new = "" 
    with open("new.txt", "w", encoding="utf-8") as file: 
        for i in dict.keys(): 
            new += "\n" + i.strip() + "\t" + str(dict[i]) 
            file.write(new) 
            open()

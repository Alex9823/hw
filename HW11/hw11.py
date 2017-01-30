
import re

m = []
def wordlist():
    with open ('new1.txt', 'r', encoding = 'utf-8') as t:
        text = t.read()
        text = text.lower()
    text = text.split()
    for i in range(len(text)): 
        text[i] = text[i].strip('”“".,!?{{}}/')
    return text

def reg_expression():
    text= wordlist()
    drink = r"\bвып(и(в(ш((ий|ая|ее|его|ему|им|ем|ей|ую|ей)(ся)?|и(сь)?))?|ть|л(ся|[аои](сь)?)?)|у(ю(сь|(т|щ(ий|ая|ее|его|ему|им|ем|ую|ей|))(ся)?)?|е((шь|т|м)(ся)?|те(сь)?)|я(сь)?))\b"


    for i in range(len(text)):
        if re.search(drink,text[i]) != None:
            if text[i] not in m:
                m.append(text[i])
    return m

def main () :    
    a=reg_expression()
    b=print('Формы глагола "выпить":  ' + ', '.join(m) + '.')
    return a
a= main()






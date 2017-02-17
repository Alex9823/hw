import re

def open1():
    with open ('f.html', 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def resub():
    text = open1()
    lang = '(философ)(и(и|й|е)?|у|ям|й|ю|ях|я)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    Lang = '(Философ)(и(и|й|е)?|у|ям|й|ю|ях|я)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    langg ='(философск)(ие|ое|ой|ие|ими|им|й|еих|им|ио|йа|ие|ую|е|ям|ий|ю|ях|им|я|ий)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    langgg ='(Философск)(ие|ое|ая|й|е|ие|ими|им|ой|их|им|ио|йа|ие|ую|е|ям|ий|ю|ях|им|я|ий)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    langggg ='(философы)(<)?'

    l = re.search(lang, text)
    L = re.search(Lang, text)
    ll = re.search(langg, text)
    b = re.search(langgg, text)
    a = re.search(langggg, text)
    if re.search(lang, text):
        text = re.sub(l.group(1), 'астролог', text)
    if re.search(Lang, text):
        text = re.sub(L.group(1), 'Астролог', text)
    if re.search(langg, text):
        text = re.sub(ll.group(1), 'астрологическ', text)
    if re.search(langgg, text):
        text = re.sub(b.group(1), 'Астрологическ', text)
    if re.search(langggg, text):
        text = re.sub(a.group(1), 'астрологи', text)
  
    return text

def main():
    text = resub()
    with open ('newlingua.html', 'w', encoding = 'utf-8') as t:
        t.write(text)
main()

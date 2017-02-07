
import re
def open_html(fname):
    with open ('fname', 'r', encoding = 'utf-8') as f:
        conten=f.read()
    return content
def find_links(content):
    reg=r'<a\s+href="(.*?)".*?>(.*?)</a>'
    links=re.findall(reg, conten)
    return links
text=open_html('Хлеб.html')
links=find_links(text)
for link in links [:20]:
    print(link[1], '-->', link[0])

rel=r'(\D)'
smth=rel.findall(rel, conten)

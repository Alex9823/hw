# Программа должна читать текст из файла и сообщать,
# есть ли в тексте хотя бы одна биграмма (два слова, стоящих в тексте друг за другом),
# встречающаяся больше двух раз. Регистр и знаки препинания нужно не учитывать.
# В программе хотя бы один раз нужно использовать list comprehensions.



def open_file(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    words = []
    for line in f:
        line = line.strip()
        words += line.split()
    for word_num in range(len(words)):
        words[word_num] = words[word_num].strip(u'.,!?:;()\'\"1234567890')
        words[word_num] = words[word_num].lower()
    f.close()
    return words


def bigramms(words):
    # bi = [words[i]+words[i+1] for i in range(len(words)) if i<len(words)]
    bi = create_list(words)
    dic = {}
    for j in bi:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
    answer = [key for key in dic if dic[key]> 2]
    print('\n'.join(answer))
    print(answer)
    return answer


def create_list(words):
    bi = []
    for i in range(len(words)):
        if i < len(words)-1:
            j = i+1
            bi.append(words[i]+' ' + words[j])

    return bi

words = open_file(u'text.txt')
bigramms(words)

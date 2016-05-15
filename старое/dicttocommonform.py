#-*- coding: utf-8 -*-
import re
import codecs

def foo(a):
    return len(a[1])

def sochet(word):
    word2 = word.replace(u'уо', u'У')
    word2 = word2.replace(u'оу', u'У')
    word2 = word2.replace(u'жы', u'жи')
    word2 = word2.replace(u'шы', u'ши')
    word2 = word2.replace(u'щы', u'щи')
    word2 = word2.replace(u'чы', u'чи')
    word2 = word2.replace(u'жю', u'жу')
    word2 = word2.replace(u'шю', u'шу')
    word2 = word2.replace(u'щю', u'щу')
    return word2

def one_letter(word):
    global bukv
    word2 = u''
    for i in range(len(word)):
        try:
            word2 += bukv[word[i]]
        except:
            word2 += word[i]
    return word2

def begend(word):
    if word[-1] == u'ъ':
        word = word[:-1]
    return word

def inter(word):
    cons = u'цкнгшщзхфвпрлджчсмтб'
    word2 = u''
    for i in range(len(word)-1):
       # print u'букву взял'
        word2 += word[i]
        if word[i] in cons and word[i+1] in cons:
           # print u'два согласных рядом'
            word2 += u'ъ'
        #print word2
    word2 += word[-1]
    return word2

def prefix(word, pos):
    if word[:4] == u'расъ':
        word = u'разъ' + word[4:]
    if word[:4] == u'вОсъ':
        word = u'вОзъ' + word[4:]
    if word[:4] == u'рОсъ':
        word = u'рОзъ' + word[4:]
    if word[:4] == u'бЕсъ':
        word = u'бЕзъ' + word[4:]
    if word[:6] == u'чърЕсъ' or word[:6] == u'чЕрЕсъ' or word[:6] == u'чьрЕсъ':
        word = u'чЕрЕзъ' + word[6:]
    if pos == u'V': #НУЖНО ВЕРНУТЬСЯ ОБРАТНО, ЕСЛИ НЕ ОПРЕДЕЛИЛОСЬ, КАК ГЛАГОЛ
        if word[:3] == u'зъг' or word[:3] == u'зъз' or word[:3] == u'зъв' or word[:3] == u'зъд' or word[:3] == u'зъж' or word[:3] == u'зъб': #тут вообще-то нестандартно несколько + здесь -- содесь
            word = u'съ' + word[2:]
        if word[:2] == u'съ':
            # print word, pos
            word = u'сО' + word[2:]
    return word

def main(word, pos):
    #print word
    word = sochet(word)
    #print word
    word = one_letter(word)
    #print word
    try:
        word = begend(word)
        #print word
    except:
        #print word
        pass
    try:
        word = inter(word)
    except:
        #print word
        pass
    word = prefix(word, pos)
    # print word
    word = boyary(word)
    return word

def boyary(word):
    word = re.sub(u'([Иь])У', u'\\1Ю', word)
    word = re.sub(u'([Иь])ы', u'ы', word)
    word = re.sub(u'([Иь])а', u'\\1Я', word)
    word = re.sub(u'([Иь])О', u'\\1ё', word)
    word = re.sub(u'([Иь])И', u'\\1й', word)
    word = word.replace(u'уа', u'уЯ')
    word = word.replace(u'Еа', u'ЕЯ')
    word = word.replace(u'ыа', u'ыЯ')
    word = word.replace(u'Оа', u'ОЯ')
    word = word.replace(u'эа', u'эЯ')
    word = word.replace(u'Яа', u'ЯЯ')
    word = word.replace(u'Иа', u'ИЯ')
    word = word.replace(u'Юа', u'ЮЯ')
    word = word.replace(u'аа', u'аЯ')
    return word

def problemcommon(stems, pos):
    # print stems
    if u'|' in stems:
        # print u'| in stems'
        stems1 = stems.split(u'.|')
        stems1a = []
        for stems1e in stems1:
            if u'//' in stems1e:
                stems2 = stems1e.split(u'.//')
                stems2a = []
                for stems2e in stems2:
                    # stems2a.append(stems2e)
                    stems2en = main(stems2e, pos)
                    if stems2en != None:
                        stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a)
                stems1a.append(stems2)
            else:
                stems2a = []
                # stems2a.append(stems1e)
                stems2en = main(stems1e, pos)
                if stems2en != None:
                    stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a) #?
                stems1a.append(stems2)
        stems1 = u'.|'.join(stems1a)
    else:
        # print u'no | in stems'
        if u'//' in stems:
            # print u'// in stems'
            stems1 = stems.split(u'.//')
            stems1a = []
            for stems1e in stems1:
                # stems1a.append(stems1e)
                stems1en = main(stems1e, pos)
                if stems1a != None:
                    stems1a.append(stems1en)
            stems1 = u'.//'.join(stems1a)
        else:
            # print u'nothing in stems'
            stems = stems.replace(u'.', u'') # Надо?
            stemsa = []
            # print u'еще помним, что тут?', stems
            # stemsa.append(stems)
            for item in stemsa:
                pass
                # print u'check1', item
            stemsen = main(stems, pos)
            # print stemsen
            if stemsen != None:
                stemsa.append(stemsen)
            else:
                pass
                # print u'none таки'
            for item in stemsa:
                pass
                # print u'check2', item
            for item in stemsa:
                # print item
                pass
            stems1 = u'.//'.join(stemsa)
    return stems1

s = codecs.open('bukv.csv', 'r', 'utf-8')
bukv = {}
for line in s:
    line = line.rstrip()
    line = line.split(u'	')
    bukv[line[0]] = line[1]

od = codecs.open(u'total_new_dict_sevpar.txt', "r", "utf-8")
nd = codecs.open(u'total_new_dict_sevpar_CF.txt', u'w', u'utf-8')

oda = od.read()
odar = oda.split(u'-lexeme\r\n')
odag = []
for word in odar:
    m = re.search(u' lex: (.+)\r\n stem: (.*)\r\n gramm: (.*)\r\n paradigm: (.*)\r\n transl_ru: (.*)\r\n', word)
    try:
        bealexeme = m.group(1)
    except:
        # print u'split_error', word
        continue
    stem = m.group(2)
    trans = m.group(5)
    paradigma = m.group(4)
    gramm = m.group(3)
    pos = gramm[0]
    tstems = problemcommon(stem, pos)
    try:
        if tstems[-1] != u'.':
            tstems += u'.'
    except:
        # print bealexeme, gramm
        tstems = u'.'
    wordinf = u' lex: ' + bealexeme + u'\r\n stem: ' + tstems + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigma + u'\r\n transl_ru: ' + trans + u'\r\n'
    odag.append(wordinf)
oda = u'-lexeme\r\n'.join(odag)
oda = u'-lexeme\r\n' + oda

nd.write(oda)

'''
for line in od:
    if line[1] == u's':
        #print line
        li = re.search(u'stem: (.*?)\r\n', line)
        stems = li.group(1)
        tstems = problemcommon(stems)
        line = u' stem: ' + tstems + u'\r\n'
        #print line
    nd.write(line)
    '''
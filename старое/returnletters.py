#-*- coding: utf-8 -*-
import re
import codecs
import json

def missedletters(word):
    newword = word
    newword = newword.replace(u'i', u'и')
    newword = newword.replace(u'і', u'и')
    newword = newword.replace(u'ѡ', u'о')
    newword = newword.replace(u'є', u'e')
    newword = newword.replace(u'́', u'')
    # newword = newword.replace(u'ѵ', u'и') # !!!!!!!!!!!!!!!!!!!!!!!!!!
    newword = newword.replace(u'ѵ', u'и')
    newword = newword.replace(u'̂', u'')
    newword = newword.replace(u'ѻ', u'о')
    return newword

nazv = u'All_dict_polyakov_all_let.txt'

od = codecs.open(nazv, "r", "utf-8")

truedict = {}

for line in od:
    transl_ru = u''
    info = re.search(u'<p>(.+)</a>  <i>(.+)</i>  (.+?)</a> (?:<em>(.+)</em>)?.*</p>', line)
    try:
        lexeme = info.group(1)
    except:
        print u'search_error ', line
        continue
    if u'+' in lexeme:
        if lexeme[0] + lexeme[1] == u'не':
            lexeme = lexeme[3:]
        else:
            #print u'тоска', lexeme #непонятно, что делать с местоимениями. Глаголы решили игнорить
            continue
    if lexeme[-2:] == u'ся':
        lexeme = lexeme[:-2]
    gramm = info.group(2)
    try:
        paradigm = info.group(3)
        if u'<em>' in paradigm:
            hi = re.search(u'<em>(.+)</em>', paradigm)
            transl_ru = hi.group()
            paradigm = u''
    except:
        paradigm = u''
    if transl_ru == u'':
        transl_ru = info.group(4)
    if transl_ru == None:
        transl_ru = u''
    truedict[missedletters(lexeme)] = [lexeme, gramm, paradigm, transl_ru]

w = codecs.open('missedletters.json', 'w', 'utf-8')
json.dump(truedict, w, ensure_ascii=False, indent=2)
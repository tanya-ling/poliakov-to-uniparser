#-*- coding: utf-8 -*-
import re
import codecs
import json

def letterchange(word):
    newword = word
    newword = newword.replace(u'i', u'и')
    newword = newword.replace(u'і', u'и')
    newword = newword.replace(u'ѡ', u'о')
    newword = newword.replace(u'є', u'e')
    newword = newword.replace(u'́', u'')
    # newword = newword.replace(u'ѵ', u'в') #!!!!!!!!!!!!!!!!!!!!!!!!!!
    newword = newword.replace(u'ѵ', u'и')
    newword = newword.replace(u'̂', u'')
    newword = newword.replace(u'ѻ', u'о')
    newword = newword.replace(u'ѳ', u'ф')
    newword = newword.replace(u'ѯ', u'кс')
    newword = newword.replace(u'ѱ', u'пс')
    newword = newword.replace(u'ѕ', u'з')
    return newword

def historyparadigm(paradigm, word):
    add_paradigm = u''
    if word == u'волъ' or word == u'полъ' or word == u'медъ' or word == u'вьрхъ' or word == u'домъ' or word == u'буйволъ' or word == u'мидъ':
        add_paradigm += u'/N6t'
        # print word
    if word == u'камень':
        add_paradigm += u'/N5en'
    if u'N43' in paradigm:
        add_paradigm += u'/N1j//N1j*//N1s//N1sj'# может быть еще N1t//N1t*//N1k//N1g//N1k*//N1c//N1c*//N1a//N1i//N1e//N1in
    if u'N1j' in paradigm:
        add_paradigm += u'/N42'
    if u'N5er' in paradigm or u'N5ov' in paradigm or u'N5*ov' in paradigm:
        add_paradigm += u'/N41'
    if u'N5en' in paradigm or u'N5et' in paradigm or u'N5es' in paradigm:
        add_paradigm += u'/N1j//N1j*//N1s//N1sj'# может быть еще N1t//N1t*//N1k//N1g//N1k*//N1c//N1c*//N1a//N1i//N1e//N1in
    if u'N1t' in paradigm:
        add_paradigm += u'/N1t*'
    if u'N2t' in paradigm:
        add_paradigm += u'/N2t*'
    if u'N2c' in paradigm:
        add_paradigm += u'/N2c*'
    if add_paradigm == u'':
        return
    add_paradigm = add_paradigm.replace(u'//', u'/')
    return add_paradigm

def changefirst_e_a(word):
    words = []
    # print word
    if len(word) > 3 and word[0] == u'е':
        # print u'like a one', word
        word1 = u'о' + word[1:]
        words.append(word1)
    elif len(word) > 3 and word[0] == u'а':
        # print u'like a lam', word
        word1 = u'я' + word[1:]
        words.append(word1)
    else:
        return
    words = u'.//'.join(words)
    return words

def moreproblemsadj(word):
    words = []
    # print u'adj problem'
    if word[-2:] == u'ск':
        # print word, u'ck adj'
        word1 = word[:-2] + u'т'
        words.append(word1)
    else:
        return
    words = u'.//'.join(words)
    return words

def moreproblemsnou(word):
    words = []
    if u'жд' in word:
        # print word, u'жд'
        word1 = word.replace(u'жд', u'ж')
        words.append(word1)
    else:
        return
    words = u'.//'.join(words)
    return words

def moreproblems1(word):
    # print u'problem1'
    words = []
    if word[-5:] == u'еческ':
        # print word, u'еческ'
        word1 = word.replace(u'еческ', u'ецк')
        # print word1
        words.append(word1)
        word2 = word.replace(u'еческ', u'етск')
        # print word2
        words.append(word2)
    else:
        # print u'no p1 found'
        return
    # print u'p1 found'
    words = u'.//'.join(words)
    # print words
    return words

def moreproblems2(word):
    words = []
    if re.search(u'[уеыаоэяиюѣ]г[уеыаоэяиюѣ]', word):
        # print word
        word1 = re.sub(u'([уеыаоэяиюѣ])г([уеыаоэяиюѣ])', u'\\1\\2', word)
        words.append(word1)
        words = u'.//'.join(words)
    else:
        return
    return words

def moreproblems(word):
    if len(word) == 0:
        return
    if word[-1] == u'.':
        word = word[:-1]
    words = []
    # print word
    word0 = changefirst_e_a(word)
    if word0 != None:
        words.append(word0)
        word0a = word0.split(u'.//')
        for word0ae in word0a:
            word1 = moreproblems1(word0ae)
            if word1 != None:
                # print u'p1 really found'
                print word1, u'like единоведческий'
                words.append(word1)
            word1 = moreproblems2(word0ae)
            if word1 != None:
                # print u'p2 really found'
                # print word1, u'like единогодный'
                words.append(word1)
    word15 = moreproblems1(word)
    if word15 != None:
        # print u'p1 really found'
        words.append(word15)
        word1a = word15.split(u'.//')
        for word1ae in word1a:
            word16 = moreproblems2(word1ae)
            if word16 != None:
                # print u'p2 really found'
                # print word16, u'like рогоческий'
                words.append(word16)
    word2 = moreproblems2(word)
    if word2 != None:
        words.append(word2)
    # print words, word, u'whai i get'
    words = u'.//'.join(words)
    if words == []:
        return
    return words

def problem(stems, gramm): # на самом деле так не все косвенные основы порождаются, потому что нужно же порождать варианты от порожденных, и уже слишком сложно, АААААААААА
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
                    stems2a.append(stems2e)
                    stems2en = moreproblems(stems2e)
                    if stems2en != None:
                        stems2a.append(stems2en)
                    if gramm[0] == u'N':
                        stems2en = moreproblemsnou(stems2e)
                        if stems2en != None:
                            stems2a.append(stems2en)
                    elif gramm == u'A':
                        stems2en = moreproblemsadj(stems2e)
                        if stems2en != None:
                            stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a)
                stems1a.append(stems2)
            else:
                stems2a = []
                stems2a.append(stems1e)
                stems2en = moreproblems(stems1e)
                if stems2en != None:
                    stems2a.append(stems2en)
                if gramm[0] == u'N':
                    stems2en = moreproblemsnou(stems1e)
                    if stems2en != None:
                        stems2a.append(stems2en)
                elif gramm == u'A':
                    stems2en = moreproblemsadj(stems1e)
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
                stems1a.append(stems1e)
                stems1en = moreproblems(stems1e)
                if stems1a != None:
                    stems1a.append(stems1en)
                if gramm[0] == u'N':
                    stems1en = moreproblemsnou(stems1e)
                    if stems1a != None:
                        stems1a.append(stems1en)
                elif gramm == u'A':
                    stems1en = moreproblemsadj(stems1e)
                    if stems1en != None:
                        stems1a.append(stems1en)
            stems1 = u'.//'.join(stems1a)
        else:
            # print u'nothing in stems'
            stems = stems.replace(u'.', u'') # Надо?
            stemsa = []
            # print u'еще помним, что тут?', stems
            stemsa.append(stems)
            for item in stemsa:
                pass
                # print u'check1', item
            stemsen = moreproblems(stems)
            # print stemsen
            if stemsen != None:
                stemsa.append(stemsen)
            else:
                pass
                # print u'none таки'
            for item in stemsa:
                pass
                # print u'check2', item
            if gramm[0] == u'N':
                stemsen = moreproblemsnou(stems)
                if stemsen != None:
                    stemsa.append(stemsen)
                for item in stemsa:
                    pass
                    # print u'check3', item
            elif gramm == u'A' or gramm == u'A,poss':
                for item in stemsa:
                    # print u'check4', item
                    pass
                stemsen = moreproblemsadj(stems)
                for item in stemsa:
                    # print u'check5', item
                    pass
                if stemsen != None:
                    # print u'dfghjkl'
                    stemsa.append(stemsen)
                for item in stemsa:
                    # print u'check6', item
                    pass
            for item in stemsa:
                # print item
                pass
            stems1 = u'.//'.join(stemsa)
    return stems1


def v12xstar(orig):
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in consonants and word[-2] in consonants:
            word1 = word[:-1] + u'е' + word[-1]
            stems.append(word1)
        else:
            print u'v12star_wow', orig[0]
    return stems

def add_l(orig):
    #ВОЗМОЖНА ВЫДАЧА МАССИВА
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            # без кластеров
            word1 = word+u'л'
            stems.append(word1)
        else:
            print u'addl_wow', orig[0]
    return stems
def change_dsz(orig):
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] == u'д':
            word1 = word[:-1] + u'жд'
            stems.append(word1)
        elif word[-1] == u'с':
            word1 = word[:-1] + u'ш'
            stems.append(word1)
        elif word[-1] == u'з':
            word1 = word[:-1] + u'ж'
            stems.append(word1)
        elif word[-1] == u'т':
            if word[-2] != u'c':
                word1 = word[:-1] + u'щ'
                stems.append(word1)
            if word[-2] == u'с':
                word1 = word[:-2] + u'щ'
                stems.append(word1)
        else:
            print u'change_gdz_wow', orig[0]
    return stems
def begl_jat(orig):
    stems = []
    for word in orig:
        if word[-1] == u'ѣ' or word[-1] == u'я':
            word1 = word[:-1]
            stems.append(word1)
        else:
            print u'Begl_jat_wow', orig[0]
    return stems
def ov(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] == u'а' and word[-2] == u'в' and word[-3] == u'о':
            word1 = word[:-3] + u'у'
            stems.append(word1)
        elif word[-1] == u'а' and word[-2] == u'в' and word[-3] == u'е':
            word1 = word[:-3] + u'ю'
            stems.append(word1)
        else:
            print u'ov_wow', orig
    return stems
def change_k_g_h(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ч'
            stems.append(word1)
        elif word[-1] == u'х':
            word1 = word[:-1] + u'ш'
            stems.append(word1)
        elif word[-1] == u'г':
            word1 = word[:-1] + u'ж'
            stems.append(word1)
        else:
            print u'change_k_g_h_wow', orig
    return stems
def change_t(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] == u'д':
            word1 = word[:-1] + u'жд'
            stems.append(word1)
        elif word[-1] == u'с':
            word1 = word[:-1] + u'ш'
            stems.append(word1)
        elif word[-1] == u'з':
            word1 = word[:-1] + u'ж'
            stems.append(word1)
        elif word[-1] == u'т':
            if word[-2] != u'c':
                word1 = word[:-1] + u'щ'
                stems.append(word1)
            elif word[-2] == u'с':
                word1 = word[:-2] + u'щ'
                stems.append(word1)
            else:
                print u'change_t_t_wow', orig
        else:
            print u'change_t_wow', orig[0]
    return stems
def change_k(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ч'
            stems.append(word1)
        elif word[-1] == u'х':
            word1 = word[:-1] + u'ш'
            stems.append(word1)
        else:
            print u'change_k_wow', orig[0]
    return stems
def change_psti(orig):
    stems = []
    for word in orig:
        if word[-1] == u'п':
            word1 = word[:-1]
            stems.append(word1)
        elif word[-1] == u'б':
            word1 = word[:-1]
            stems.append(word1)
        else:
            print u'change_psti_wow', orig[0]
    return stems
def add_d(orig):
    stems = []
    for word in orig:
        if word[-1] != u'д':
            word1 = word + u'д'
            stems.append(word1)
        else:
            print u'add_d_wow', orig[0]
    return stems
def t_e_0(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-1]+u'т'
            word2= word[:-1]
            stems.append(word1)
            stems.append(word2)
        else:
            print u't_e_0_wow', orig[0]
    return stems
def k_ch_c_0(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    for word in orig:
        if True:
        #if word[-1] in vowels:
            word1= word+u'к'
            word2= word+u'ч'
            word3= word+u'ц'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
        else:
            print u'k_ch_c_0_wow', orig[0]
    return stems
def zh_zh(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-1]+u'г'
            word2= word[:-1]+u'ж'
            word3= word[:-1]+u'з'
            word4= word[:-1]+u'ег'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
        else:
            print u'zh_zh_wow', orig[0]
    return stems
def eg(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-1]+u'яг'
            word2= word[:-1]+u'яж'
            word3= word[:-1]+u'яз'
            word4= word[:-1]+u'ег'
            word5= word[:-1]+u'еж'
            #word6= word[:-1]+u'ещ'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
            stems.append(word5)
            #stems.append(word6)
        else:
            print u'wow', orig[0]
    return stems
def sed(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-1]+u'яд'
            word2= word[:-1] + u'ѣд'
            stems.append(word1)
            stems.append(word2)
        else:
            print u'wow', orig[0]
    return stems
def add_t(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] != u'т':
            word1 = word + u'т'
            stems.append(word1)
        else:
            print u'wow', orig[0]
    return stems
def s_st(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    if orig[0] == u'благораст':
        print orig
    for word in orig:
        if word[-1] != u'т':
            word1 = word + u'т'
            stems.append(word1)
        else:
            print u'wow', orig[0]
    return stems
def g_zh_z_0(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word+u'г'
            word2= word+u'ж'
            word3= word+u'з'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
        else:
            print u'wow', orig[0]
    return stems
def el(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-2]+u'ел'
            stems.append(word1)
        else:
            print u'wow', orig[0]
    return stems
def ol(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-2]+u'ол'
            stems.append(word1)
        else:
            print u'wow', orig[0]
    return stems
def change_or(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-2]+u'ор'
            stems.append(word1)
        else:
            print u'wow', orig[0]
    return stems
def er(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    for word in orig:
        if word[-1] in vowels:
            word1 = word[:-1]
            word2 = word[:-2]+u'е'+word1[-1]
            stems.append(word1)
            stems.append(word2)
        else:
            word1 = word[:-2]+word[-1]
            word2 = word
            stems.append(word1)
            stems.append(word2)
    return stems
def eee(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1=word[:-1]+u'о'
        stems.append(word1)
    return stems
def mya(orig):
    stems = []
    for word in orig:
        word1=word[:-1]+u'н'
        stems.append(word1)
    return stems
def vvv(orig):
    stems = []
    for word in orig:
        word1=word+u'в'
        stems.append(word1)
    return stems
def add_sh(orig):
    stems = []
    for word in orig:
        word1=word[:-1]+u'щ'
        stems.append(word1)
    return stems
def idti(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if len(word) <=1 or ((word[-1] == u'и' or word[-1] == u'й') and word[-2] in vowels):
            if word[-1] == u'и':
                word1 = word +u'д' + u'.//' + word[:-1] + u'йд'
            else:
                word1 = word +u'д' + u'.//' + word[:-1] + u'ид'
            try:
                if word[-2] == u'и':
                    word1 = word1 + u'.//' + word[:-2] + u'ид'
            except:
                pass
                #print u'идти out of range', orig[0]
            if len(word) <= 1:
                word2=u'ш'
            else:
                word2=word[:-1]+u'ш'
            word3=word2+u'е'
            word4=word3+u'д'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
        elif word[-1] == u'и' and word[-2] == u'н':
            word1=word+u'д'
            word2=word[:-2]+u'ош'
            word3=word2+u'е'
            word4=word[:-2]+u'(о)шед'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
        elif (word[-1] == u'и' or word[-1] == u'ы') and (word[-2] in consonants or word[-2] == u'ъ'):
            word1=word+u'д'
            if word[-2] == u'ъ':
                word2=word[:-2]+u'ш'
            elif word[-2] in consonants:
                word2=word[:-1]+u'ш'
            word3=word2+u'е'
            word4=word3+u'д'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
        else:
            print u'idti_wow', orig[0]
    return stems
def exat(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1 = word[:-2]+u'д'
        stems.append(word1)
    return stems
def ved(orig):
    stems = []
    for word in orig:
        word1 = word+u'д'
        stems.append(word1)
    return stems

def beglyi(orig):
    #удаляем последний гласный основы(после него макс 3), соответсвует * у полякова
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word = list(word)
        if word[-1] in consonants:
            if word[-2] in vowels:
                del word[-2]
            elif word[-3] in vowels:
                del word[-3]
            else:
                print u'beglyi_v_wow', orig[0]
        else:
            print u'beglyi_c_wow', orig[0]
        word1 = u''
        for el in word:
            word1 += el
        stems.append(word1)
    return stems
def palatal_k(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            word2 = word[:-1] + u'ч'
            stems.append(word1)
            stems.append(word2)
        else:
            print u'palatal_k_wow', orig[0]
    return stems
def palatal_g_h(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    stems = []
    for word in orig:
        if word[-1] == u'х':
            word1 = word[:-1] + u'с'
            word2 = word[:-1] + u'ш'
            stems.append(word1)
            stems.append(word2)
        elif word[-1] == u'г':
            word2 = word[:-1] + u'ж'
            word1 = word[:-1] + u'з'
            stems.append(word1)
            stems.append(word2)
        else:
            print u'palatal_g_wow', orig[0]
    return stems
def palatal_k_g_h(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    stems = []
    for word in orig:
        if word[-1] == u'х':
            word1 = word[:-1] + u'с'
            word2 = word[:-1] + u'ш'
            stems.append(word1)
            stems.append(word2)
        elif word[-1] == u'г':
            word2 = word[:-1] + u'ж'
            word1 = word[:-1] + u'з'
            stems.append(word1)
            stems.append(word2)
        elif word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            word2 = word[:-1] + u'ч'
            stems.append(word1)
            stems.append(word2)
        else:
            print u'palatal_k_g_wow', orig[0]
    return stems
def change_c(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант звонких
    stems = []
    for word in orig:
        if word[-1] == u'ц':
            word1 = word[:-1] + u'ч'
        else:
            print u'change_c_wow', orig[0]
        stems.append(word1)
    return stems
def change_k_noun(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант звонких
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            stems.append(word1)
        else:
            print u'Change_k_wow', orig[0]
    return stems
def change_k_g_h_adj(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант звонких
    stems = []
    for word in orig:
        if word[-1] == u'х':
            word1 = word[:-1] + u'с'
            stems.append(word1)
        elif word[-1] == u'г':
            word1 = word[:-1] + u'з'
            stems.append(word1)
        elif word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            stems.append(word1)
        else:
            print u'Change_k_g_h_adj_wow', orig[0]
    return stems
def vstavnoi_o(orig):
    #ВОЗМОЖНА ВЫДАЧА МАССИВА
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants and word[-2] in consonants:
            #без кластеров
            word1 = word[:-1]+u'о'+word[-1]
            stems.append(word1)
        #с одним кластером
            #elif word[-3] in consonants:
             #   word1 = word[:-2]+u'о'+word[-2]+word[-1]
              #  word2 = word[:-1]+u'о'+word[-1]
               # stems.append(word1)
                #stems.append(word2)
        elif word[-1] in consonants and word[-3] in consonants and (word[-2]==u'ь' or word[-2]==u'ъ'):
            word = word[:-2]+word[-1]
            #без кластеров
            word1 = word[:-1]+u'о'+word[-1]
            stems.append(word1)
        else:
            print u'vsvn_o_wow', orig[0]
        #с одним кластером
            #elif word[-3] in consonants:
             #   word1 = word[:-2]+u'о'+word[-2]+word[-1]
              #  word2 = word[:-1]+u'о'+word[-1]
               # stems.append(word1)
                #stems.append(word2)
    return stems
def vstavnoi_e(orig):
    #ВОЗМОЖНА ВЫДАЧА МАССИВА
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in consonants and word[-2] in consonants:
            #без кластеров
            word1 = word[:-1]+u'е'+word[-1]
            stems.append(word1)
        #с одним кластером
            #elif word[-3] in consonants:
             #   word1 = word[:-2]+u'е'+word[-2]+word[-1]
              #  word2 = word[:-1]+u'е'+word[-1]
               # stems.append(word1)
                #stems.append(word2)
        elif word[-1] in consonants and word[-3] in consonants and (word[-2]==u'ь' or word[-2]==u'ъ'):
            word = word[:-2]+word[-1]
            #без кластеров
            word1 = word[:-1]+u'е'+word[-1]
            stems.append(word1)
        else:
            #print u'vstvn_e_wow', orig[0]
            stems = orig[0] + u'.|' + orig[0] + u'.'
        #с одним кластером
            #elif word[-3] in consonants:
             #   word1 = word[:-2]+u'е'+word[-2]+word[-1]
              #  word2 = word[:-1]+u'е'+word[-1]
               # stems.append(word1)
                #stems.append(word2)
    return stems
def narashenie(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ес'
            word2 = word + u'ен'
            word3 = word + u'ер'
            word4 = word + u'ов'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
        elif word[-1] in vowels:
            word1 = word[:-1] + u'ес'
            word2 = word + u'т'
            word3 = word[:-1] + u'ен'
            word4 = word[:-1] + u'ер'
            word5 = word[:-1] + u'ов'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
            stems.append(word4)
            stems.append(word5)
        else:
            print u'naraschenie_wow', orig[0]
    return stems
def narashenie_es (orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ес'
        elif word[-1] in vowels:
            word1 = word[:-1] + u'ес'
        else:
            print u'narashenie_es_wow', orig[0]
        stems.append(word1)
    return stems
def narashenie_en (orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ен'
        elif word[-1] in vowels:
            word1 = word[:-1] + u'ен'
        else:
            print u'narash_en_wow', orig[0]
        stems.append(word1)
    return stems
def narashenie_er (orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ер'
        elif word[-1] in vowels:
            word1 = word[:-1] + u'ер'
        else:
            print u'narash_er_wow', orig[0]
        stems.append(word1)
    return stems
def narashenie_ov (orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ов'
        elif word[-1] in vowels:
            word1 = word[:-1] + u'ов'
        else:
            print u'narash_ov_wow', orig[0]
        stems.append(word1)
    return stems
def narashenie_at (orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            word1 = word + u'ят'
        elif word[-1] in vowels:
            word1 = word + u'т'
        else:
            print u'narash_at_wow', orig[0]
        stems.append(word1)
    return stems


def osninf(inf, paradigm):
    dwa = [u'V12g', u'V11u', u'V14st', u'V11a', u'V11e', u'V12ov', u'V14z', u'V14k', u'V14g',	u'V14g*',	u'V14eg', u'V15er',	u'V15ol', u'V15or',	u'V15el',	u'V15i',u'V15y',	u'V15e', u'V15n',	u'V15a', u'V15v', u'Viti',	u'Vexat',	u'Vdat']
    tri = [u'V14et', u'V14t*', u'V14ed', u'V14t',u'V14d', u'V14p', u'V13a', u'V21n', u'V21a', u'V21s', u'V21p',	u'V21t', u'V22n', u'V22p', u'V22t',	u'V22s', u'V22a', u'V12ov',	u'V12n', u'V12p', u'V12t', u'V12k', u'V12a', u'Vest', u'Vved', u'Vima', u'V12x',	u'V12x*', u'V13p+V22s',	u'V12t+V22t']
    four =[u'V13t',	u'V13k']
    if paradigm == u'Vbyt':
        print u'так не должно быть'
        return u'aaa'
    if u'+' in inf:
        print u'печаль', paradigm #печали нет
        return u'aaa'
    if inf[-2:] == u'ся':
        inf = inf[:-2]
    if paradigm in dwa:
        infstem = inf[:-2]
        #if infstem.startswith(u'благорас'):
           # print infstem
    elif paradigm in tri:
        infstem = inf[:-3]
    elif paradigm in four:
        infstem = inf[:-4]
    else:
        if u'/' in paradigm:
            '''
            arpar = paradigm.split(u'/')

            bigstem = u''
            for item in arpar:
                newstem = verbstem(inf, item)
                bigstem = bigstem + u'//' + newstem
            infstem = bigstem
            '''
            return u'difV'
        else:
            #print u'грусть', paradigm, inf #грксти нет
            return u'aaa'
    #print infstem
    return infstem

def osnnoun(dic_word, paradigm):
    '''
    if dic_word == u'ноевъ':
        print u'но́евъ'
    '''
    if paradigm == u'Pro':
        if dic_word[-1] == u'й' or dic_word[-1] == u'и':
            stem0 = dic_word[:-2]
        elif dic_word[-1] == u'ъ' or dic_word[-1] == u'ь':
            stem0 = dic_word[:-1]
    elif paradigm == u'NUM' or paradigm == u'N1t' or paradigm == u'N6t' or paradigm == u'N3j' or paradigm == u'N1c' or paradigm == u'N1t*' or paradigm == u'N1k' or paradigm == u'N1g' or paradigm == u'N1k*' or paradigm == u'N1s' or paradigm == u'N1c*':
        stem0 = dic_word[:-1]  #минус ъ
    elif paradigm == u'N1a' or paradigm == u'N1i' or paradigm == u'N1e':
        stem0 = dic_word[:-1]     #минус й
    elif paradigm == u'N1in':
        stem0 = dic_word[:-3]     #минус инъ
    elif paradigm == u'N2t' or paradigm == u'N2t*' or paradigm == u'N2k':
        stem0 = dic_word[:-1]     #минус о
    elif paradigm == u'N2s' or paradigm == u'N2c' or paradigm == u'N2c*' or paradigm == u'N2i' or paradigm == u'N2e' or paradigm == u'N2j':
        stem0 = dic_word[:-1]     #минус е
    elif paradigm == u'N3t' or paradigm == u'N3t*' or paradigm == u'N3k' or paradigm == u'N3k*' or paradigm == u'N3s' or paradigm == u'N3c' or paradigm == u'N3c*':
        stem0 = dic_word[:-1]     #минус а
    elif paradigm == u'N3j*' or paradigm == u'N3a' or paradigm == u'N3i':
        stem0 = dic_word[:-1]     #минус я
    elif paradigm == u'N3e':
        stem0 = dic_word[:-1]     #минус а/я
    elif paradigm == u'N41' or paradigm == u'N42' or paradigm == u'N43' or paradigm == u'N43*' or paradigm == u'N5*ov' or paradigm == u'N1j' or paradigm == u'N1j*' or paradigm == u'N1sj':
        stem0 = dic_word[:-1]     #минус ь
    elif paradigm == u'N5en' or paradigm == u'N5et' or paradigm == u'N5es' or paradigm == u'N5er' or paradigm == u'N5ov':
        stem0 = dic_word     #минус ничего
    elif paradigm == u'A1i':
        stem0 = dic_word[:-1]
    elif paradigm[0] == u'A':
        if dic_word[-1] == u'й' or dic_word[-2:] == u'ое':
            stem0 = dic_word[:-2]
        elif dic_word[-1] == u'ъ' or dic_word[-1] == u'ь' or dic_word[-3:] == u'ина':
            stem0 = dic_word[:-1]
        else:
            print u'some strange adj', dic_word
    else:
        # print u'what is it', dic_word, paradigm
        stem0 = u'No_paradigm'
    '''
    if dic_word == u'ноевъ':
        print u'но́евъ', stem0
    '''
    return stem0

def verbstem(lexeme, paradigm):
    #paradigm = raw_input(u'Введите тип парадигмы: ').decode(u'utf-8')
    #infi = raw_input(u'Введите инфинитив: ').decode(u'utf-8')
    if paradigm == u'V11u':
        paradigm = u'V11a/V11e'
    if paradigm == u'V14et':
        paradigm = u'V14p/V14z/V14t/V14d/V14st/V14t*/V14ed/V14k/V14g/V14g*/V14eg'
    if paradigm == u'V12g':
        paradigm = u'V12ov/V12n/V12p/V12t/V12k/V12a/V12x/V12x*'
    if paradigm == u'V12p+V22s':
        #print u'work'
        paradigm = u'V13p+V22s'
    if paradigm == u'V12x':
        paradigm += u'/V12x*'
    infi = lexeme
    osnova = osninf(infi, paradigm)
    if osnova == u'aaa': #значит не указана парадигма!
        return u'no_paradigm'
    if osnova == u'difV': #несколько парадигм
        stem1 = u''
    #print osnova
    stem = []
    stem.append(osnova)
    if paradigm == u'V12x*':
        stem1 = v12xstar(stem)
    if paradigm == u'V14st':
        stem1 = s_st(stem)
    elif paradigm == u'V14p':
        stem1 = change_psti(stem)
    elif paradigm == u'V14d':
        stem1 = add_d(stem)
    elif paradigm == u'V14t':
        stem1 = add_t(stem)
    elif paradigm == u'V14t*':
        stem1 = t_e_0(stem)
    elif paradigm == u'V14ed':
        stem1 = sed(stem)
    elif paradigm == u'V14k':
        stem1 = k_ch_c_0(stem)
    elif paradigm == u'V14g':
        stem1 = g_zh_z_0(stem)
    elif paradigm == u'V14g*':
        stem1 = zh_zh(stem)
    elif paradigm == u'V14eg':
        stem1 = eg(stem)
    elif paradigm == u'V15el':
        stem1 = el(stem)
    elif paradigm == u'V15ol':
        stem1 = ol(stem)
    elif paradigm == u'V15or':
        stem1 = change_or(stem)
    elif paradigm == u'V15er':
        stem1 = er(stem)
    elif paradigm == u'V15e':
        stem1 = eee(stem)
    elif paradigm == u'V15n':
        stem1 = mya(stem)
    elif paradigm == u'V15v':
        stem1 = vvv(stem)
    elif paradigm == u'V13p+V22s':
        stem1 = add_l(stem)
    elif paradigm == u'V12t+V22t':
        stem1 = add_sh(stem)
    elif paradigm == u'Viti':
        stem1 = idti(stem)
    elif paradigm == u'Vexat':
        stem1 = exat(stem)
    elif paradigm == u'Vved':
        stem1 = exat(stem)
    elif paradigm == u'V21p':
        stem1 = add_l(stem)
    elif paradigm == u'V22p':
        stem1 = add_l(stem)
    elif paradigm == u'V21t':
        stem1 = change_dsz(stem)
    elif paradigm == u'V22t':
        stem1 = change_t(stem)
    elif paradigm == u'V11e':
        stem1 = begl_jat(stem)
    elif paradigm == u'V12ov':
        stem1 = ov(stem)
    elif paradigm == u'V12p':
        stem1 = add_l(stem)
    elif paradigm == u'V12t':
        stem1 = change_dsz(stem)
    elif paradigm == u'V12k':
        stem1 = change_k(stem)
    elif paradigm == u'V12g':
        stem1 = change_k_g_h(stem)
   # elif paradigm == u'V12x*':
    #    stem1 = change_k_g_h(stem)
    elif paradigm == u'V13k':
        stem1 = change_k_g_h(stem)
    else:
        stem1 = []
#тестовая часть
     #if paradigm == u'':
      #  stem1 =
    #print u'stem1'
    try:
        result = u'.|'.join(stem1)
    except:
        result = stem1
    result = osnova + u'.|' + result + u'.'
    return result

def nounstem(paradigm, osnova):
    stem = []
    stem.append(osnova)
    stemsC = u''
    stem2 = []
    if paradigm == u'N1t*' or paradigm == u'N1j*':
        stem1 = beglyi(stem)
    elif paradigm == u'N1g':
        stem1 = palatal_g_h(stem)
    elif paradigm == u'N1k':
        stem1 = palatal_k(stem)
    elif paradigm == u'N1k*':
        stem1 = beglyi(stem)
        stem2 = palatal_k(stem1)
    elif paradigm == u'N1c*':
        stem1 = beglyi(stem)
        stem2 = change_c(stem1)
    elif paradigm == u'N2t*':
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
        stems1 = u'.|'.join(stem1)
        stems2 = u'.|'.join(stem2)
        stems = stems1 + u'.//' + stems2 + u'.'
        stemsC = stems
        stem2 = []
    elif paradigm == u'N2k':
        #все 2
        stem1 = palatal_k_g_h(stem)
    elif paradigm == u'N2c*':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N3t*':
        #все 2
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
        stems1 = u'.|'.join(stem1)
        stems2 = u'.|'.join(stem2)
        stems = stems1 + u'.//' + stems2 + u'.'
        stemsC = stems
        stem2 = []
    elif paradigm == u'N3j*':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N3k':
        #все 2
        stem1 = palatal_k_g_h(stem)
    elif paradigm == u'N3k*':
        #все 2
        stem1 = vstavnoi_o(stem)
        stem2 = change_k_noun(stem)
    elif paradigm == u'N3c*':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N43*':
        #все 2
        stem1 = beglyi(stem)
    elif paradigm == u'N5en':
        #все 2
        stem1 = narashenie_en(stem)
    elif paradigm == u'N5et':
        #все 2
        stem1 = narashenie_at(stem)
    elif paradigm == u'N5es':
        #все 2
        stem1 = narashenie_es(stem)
    elif paradigm == u'N5er':
        #все 2
        stem1 = narashenie_er(stem)
    elif paradigm == u'N5ov':
        #все 2
        stem1 = narashenie_ov(stem)
    elif paradigm == u'N5*ov':
        stem1 = beglyi(stem)
    elif paradigm == u'A1k' or paradigm == u'A1g':
        stem1 = change_k_g_h_adj(stem)
    elif paradigm == u'A1t*':
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'A1j*':
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'A1k*':
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
        stems1 = u'.|'.join(stem1)
        stems2 = u'.|'.join(stem2)
        stems = stems1 + u'.//' + stems2 + u'.'
        stemsC = stems
        stem2 = []
    else:
        # print stem[0], paradigm, u'эт что такое?'
        stem1 = stem[:]
        return stem1[0]
    if len(stemsC) > 0:
        return osnova + u'.|' + stemsC
    stems1 =  u'.|'.join(stem1)
    if len(stem2)>0:
        stems2 = u'.|'.join(stem2)
        stems = osnova + u'.|' + stems1 + u'.|' + stems2 + u'.'
    else:
        stems = osnova + u'.|' + stems1
    return stems

def noverbparad(lexeme):
                paradigm = u''
                if lexeme[-3:] == u'ити' or lexeme[-3] == u'ѣти':
                    paradigm = u'V21n/V21a/V21s/V21p/V21t/V22n/V22p/V22t/V22s/V22a'
                if lexeme[-3:] == u'ѣти' or lexeme[-3:] == u'ати':
                    paradigm += u'/V11a/V11e/V12ov/V12n/V12p/V12t/V12k/V12a/V12x/V12x*'
                if lexeme[-4:] == u'нути':
                    paradigm = u'V13a/V13t/V13k'
                elif lexeme[-2:] == u'щи':
                    paradigm = u'V14k/V14g/V14g*/V14eg'
                elif lexeme[-3:] == u'сти':
                    paradigm = u'V14p/V14z/V14t/V14d/V14st/V14t*/V14ed'
                elif lexeme[-3:] == u'ити':
                    paradigm += u'/V15i'
                elif lexeme[-3:] == u'ыти':
                    paradigm += u'/V15y'
                else:
                    paradigm += u'/V15e/V15n/V15a/V15v'
                if u'л' in lexeme[-4:]:
                    paradigm += u'/V15ol/V15el'
                if u'р' in lexeme[-4:]:
                    paradigm += u'/V15or/V15er'
                return paradigm

def nonounparad(lexeme, gramm):
    if gramm == u'NUM':
        paradigm = u'N41/N1t/N2t/N3t'
        return paradigm
    if gramm == u'A-NUM':
        paradigm = u'A1t/A1j'
        return paradigm
    if gramm == u'A-PRO':
        pos = gramm
    elif gramm == u'N-PRO':
        pos = gramm
    else:
        pos = gramm[0]
    word = lexeme
    if pos == u'N':
        if word[-1] == u'ъ':
            paradigm = u'N1t/N1t*/N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1c/N1c*/N6t'
        elif word[-1] == u'ь':
            paradigm = u'N1t/N1t*/N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1c/N1c*/N5*ov/N41/N42/N43/N43*'
        elif word[-1] == u'о':
            paradigm = u'N2t/N2t*/N2k/N5es'
            print word, u'примерчик'
        elif word[-1] == u'й':
            paradigm = u'N1i/N1e/N1in'
        elif word[-1] == u'е':
            paradigm = u'N2j/N2s/N2c/N2c*/N2i/N2e'
        elif word[-1] == u'а':
            paradigm = u'N3t/N3t*/N3k/N3k*/N3s/N3c/N3c*/N3e'
        elif word[-1] == u'я':
            if word[-2] != u'м':
                paradigm = u'N3j/N3j*/N3a/N3i/N3e/N5en/N5et'
            elif word[-2] == u'м':
                paradigm = u'N3j/N3j*/N3a/N3i/N3e/N5en/N5et/N5en'
        elif word[-4:] == u'мати':
            paradigm = u'N5er'
        else:#если мы точно знаем, что это существительное, но ничего сверху не подходит (может быть pluralia tantum)
            paradigm = u'N1t/N1t*/N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1c/N1c*/N1a/N1i/N1e/N1in/N2t/N2t*/N2j/N2k/N2s/N2c/N2c*/N2i/N2e/N3t/N3t*/N3j/N3j*/N3k/N3k*/N3s/N3c/N3c*/N3a/N3i/N3e/N41/N42/N43/N43*/N5en/N5et/N5es/N5er/N5ov/N5*ov/N6t'
    elif pos == u'A':
        if word[-2:] == u'ый' or word[-2:] == u'ыи' or word[-2:] == u'ий' or word[-2:] == u'ии':
            paradigm = u'A1t/A2t/A1j/A2j/A1k/A1g/A1s/A1i/A1t*/A1j*/A1k*'
        else:
            print u"what a paradigm A?", word
    elif pos == u'A-PRO': # местоимение-прилагательное, это в словаре не тег парадигмы а тег частиречи а парадигмы там нет. зато у меня есть:
        paradigm = u'Pro'
    elif u'N-PRO': # местоимение-существительное, это в словаре не тег парадигмы а тег частиречи а парадигмы там нет.
        paradigm = u'N-PRO'
    else:
        print u'What a pos?', word, pos
    return paradigm

def irrstems(lexeme, paradigm):
                if lexeme in iryd:
                    stem1 = iryd[lexeme]
                    stem = u'.|'.join(stem1)
                elif lexeme[-4:] in irsd:
                    bigstem = u''
                    for stemic in irsd[lexeme[-4:]]:
                        if u'/' in stemic:
                            bigstemic = u''
                            arrstemic = stemic.split(u'/')
                            for item in arrstemic:
                                bigstemic += lexeme[:-4] + item + u'.//'
                            stemic = bigstemic
                            bigstem += stemic + u'.|'
                        else:
                            bigstem += lexeme[:-4] + stemic + u'.|'
                    stem = bigstem
                elif lexeme[-5:] in irsd:
                    bigstem = u''
                    for stemic in irsd[lexeme[-5:]]:
                        if u'/' in stemic:
                            bigstemic = u''
                            arrstemic = stemic.split(u'/')
                            for item in arrstemic:
                                bigstemic += lexeme[:-5] + item + u'.//'
                            stemic = bigstemic
                            bigstem += stemic + u'.|'
                        else:
                            bigstem += lexeme[:-5] + stemic + u'.|'
                    stem = bigstem
                else:
                    stem = verbstem(lexeme, paradigm)
                return stem

def toska(lexeme, gramm):
    lex = lexeme.split(u'+')
    lexeme = lex[0]
    if gramm[0] == u'V':
        return lexeme
    else:
        chast = lex[1]
        return lexeme, chast

def clearinfo(wordinf):
    wordinf = wordinf.replace(u'|.\r\n', u'\r\n')
    wordinf = wordinf.replace(u'//.', u'//')
    wordinf = wordinf.replace(u'//.|\r\n', u'\r\n')
    wordinf = wordinf.replace(u'//|', u'|')
    wordinf = wordinf.replace(u'|\r\n', u'\r\n')
    wordinf = re.sub(u'//+', u'//', wordinf)
    wordinf = re.sub(u'\.+', u'.', wordinf)
    wordinf = wordinf.replace(u'//\r\n', u'\r\n')
    wordinf = wordinf.replace(u'.|.|', u'.|')
    wordinf = wordinf.replace(u' /', u' ')
    wordinf = wordinf.replace(u'|.\r\n', u'\r\n')
    return wordinf

mlf = codecs.open(u'missedletters.json', u'r', u'utf-8')
ml = json.load(mlf)


nazv = u'All_dict_polyakov.txt'
od = codecs.open(nazv, "r", "utf-8")
nd = codecs.open(u'new_dict_3.txt', u'w', u'utf-8')

irs = codecs.open(u'irrstems_checked.txt', u'r', u'utf-8')
irsd = {}
for lin in irs:
    lin = lin.rstrip()
    lin = lin.split(u'	')
    irsd[lin[0]] = lin[1:]

iry = codecs.open(u'yati_checked.txt', u'r', u'utf-8')
iryd = {}
for lin in iry:
    lin = lin.rstrip()
    lin = lin.split(u'	')
    iryd[lin[0]] = lin[1:]

for line in od:
    transl_ru = u''
    chast = u'normal_word'
    info = re.search(u'<p>(.+)</a>  <i>(.+)</i>  (.+?)</a> (?:<em>(.+)</em>)?.*</p>', line)
    try:
        lexeme = info.group(1)
    except:
        print u'search_error ', line
        continue
    gramm = info.group(2)
    if u'+' in lexeme:
        if lexeme[0] + lexeme[1] == u'не':
            lexeme = lexeme[3:]
        else:
            try:
                lexeme, chast = toska(lexeme, gramm)
                # print u'тоска', lexeme
            except:
                lexeme = toska(lexeme, gramm)
    if lexeme[-2:] == u'ся':
        lexeme = lexeme[:-2]
    try:
        paradigm = info.group(3)
        if u'<em>' in paradigm:
            hi = re.search(u'<em>(.+)</em>', paradigm)
            transl_ru = hi.group()
            paradigm = u'нет парадигмы'
    except:
        paradigm = u''
    if transl_ru == u'':
        transl_ru = info.group(4)
    if transl_ru == None:
        transl_ru = u''
    if lexeme in ml:
        #print u'tr'
        bealexeme = ml[lexeme][0]
        lexeme = letterchange(bealexeme)
    else:
        #print u'what can I see?', lexeme
        bealexeme = lexeme
        lexeme = letterchange(bealexeme)
    try:
        if gramm[0] == u'V':
            if u'V12x' in paradigm:
                paradigm += u'/V12x*'
            if u'/' in paradigm:
                stem = u'difV'
            elif paradigm == u'Vbyt':
                stem = lexeme[:-4]
            else:
                try:
                    stem = irrstems(lexeme, paradigm)
                except:
                    stem = verbstem(lexeme, paradigm)
                if stem == u'no_paradigm':
                    paradigm = noverbparad(lexeme)
        elif gramm == u'A' or  gramm[0] == u'N' or gramm[0] + gramm[1] == u'N,' or gramm[0] + gramm[1] == u'A,' or gramm == u'A-PRO':
            if paradigm == u'А2sj':
                paradigm = u'A1i/A1s/A1j'
            if u'N3k' in paradigm:
                paradigm += u'/N3k*'
            if u'N3t' in paradigm:
                paradigm += u'/N3t*'
            if u'N3j' in paradigm:
                paradigm += u'/N3j*'
            if u'A1j' in paradigm:
                paradigm += u'/A1j*'
                # print u'A1j* nanana'
            a_paradigm = historyparadigm(paradigm, lexeme)
            if a_paradigm != None:
                paradigm = paradigm + a_paradigm
                # print u'hist_par', lexeme, paradigm, a_paradigm
            if u'/' in paradigm:
                stem = u'difN'
            else:
                stem0 = osnnoun(lexeme, paradigm)
                if stem0 == u'No_paradigm':
                    paradigm = nonounparad(lexeme, gramm)
                    if u'/' in paradigm:
                        stem = u'difN'
                    else:
                        stem0 = osnnoun(lexeme, paradigm)
                        stem = nounstem(paradigm, stem0)
                else:
                    stem0 = osnnoun(lexeme, paradigm)
                    stem = nounstem(paradigm, stem0)
        else:
            stem = lexeme
            paradigm = u'unchangeable'
    except:
        # paradigm = u'unchangeable'
        stem = lexeme
    '''
    if paradigm == u'':
        paradigm = nonounparad(lexeme, gramm)
        print paradigm, lexeme, gramm, u'то лт то лт'
    '''
    if stem == u'No_paradigm':
        pass
    elif gramm[0] == u'V' or gramm[0] == u'A' or gramm[0] == u'N':
        stem = problem(stem, gramm)
        try:
            if stem[-1] != u'.':
                stem += u'.'
        except:
            # print stem, u'the bad one'
            pass
    if stem == u'No_paradigm':  # это N-PRO на самом деле
        if lexeme[-3:] == u'что':
            stem = lexeme[:-3] + u'.'
        else:
            stem = u'.'

    '''
    if paradigm == u'':
        paradigm = gramm
        print paradigm
    '''

    if u'pers' in gramm:
        # print transl_ru
        transl_ru = u''

    if chast == u'normal_word':
        try:
            if stem[-1] != u'.':
                stem = stem + u'.'
        except:
            stem = u'.'
            # print bealexeme, lexeme, gramm, u'no stem hear!'

    wordinf = u'-lexeme\r\n lex: ' + bealexeme + u'\r\n stem: ' + stem + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigm + u'\r\n transl_ru: ' + transl_ru + u'\r\n'
    wordinf = clearinfo(wordinf)
    if chast != u'normal_word':
        wordinf = wordinf.replace(u'.', u'.' + chast)
    nd.write(wordinf)
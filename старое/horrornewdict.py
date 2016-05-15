#-*- coding: utf-8 -*-
import re
import codecs

def add_l(orig):
    #ВОЗМОЖНА ВЫДАЧА МАССИВА
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    #word = list(word)
    for word in orig:
        if word[-1] in consonants:
            #без кластеров
            word1 = word+u'л'
            stems.append(word1)
        else:
            print u'addl_wow', orig[0]
    return stems
def change_dsz(orig):
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
def add_l(orig):
    stems = []
    for word in orig:
        word1=word+u'л'
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

def osninf(inf, paradigm, lexeme, gramm, transl_ru):
    dwa = [u'V14st', u'V11a', u'V11e', u'V12ov', u'V14z', u'V14k', u'V14g',	u'V14g*',	u'V14eg', u'V15er',	u'V15ol', u'V15or',	u'V15el',	u'V15i',u'V15y',	u'V15e', u'V15n',	u'V15a', u'V15v', u'Viti',	u'Vexat',	u'Vdat']
    tri = [u'V14t*', u'V14ed', u'V14t',u'V14d', u'V14p', u'V13a', u'V21n', u'V21a', u'V21s', u'V21p',	u'V21t', u'V22n', u'V22p', u'V22t',	u'V22s', u'V22a', u'V12ov',	u'V12n', u'V12p', u'V12t', u'V12k', u'V12a', u'Vest', u'Vved', u'Vima', u'V12x',	u'V12x*', u'V13p+V22s',	u'V12t+V22t']
    four =[u'V13t',	u'V13k']
    if paradigm == u'Vbyt':
        return u'aaa'
    if u'+' in inf:
        print u'печаль', paradigm
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
            arpar = paradigm.split(u'/')
            for item in arpar:
                almostmain(lexeme,item,transl_ru,gramm)
            return
        else:
            print u'грусть', paradigm
            return u'aaa'
    #print infstem
    return infstem


def verbstem(lexeme, paradigm, gramm, transl_ru):
    #paradigm = raw_input(u'Введите тип парадигмы: ').decode(u'utf-8')
    #infi = raw_input(u'Введите инфинитив: ').decode(u'utf-8')
    infi = lexeme
    osnova = osninf(infi, paradigm, lexeme, gramm, transl_ru)
    if osnova == u'aaa':
        return u'aaa'
    #print osnova
    stem = []
    stem.append(osnova)
    #stem1=[]
    stem2=[]
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
    try:
        result = osnova + u'.|' + result + u'.'
    except:
        print u'innererror osn', osnova, result
    return result
    '''
    if len(stem2) > 0:
        print u'stem2'
        return u'.|'.join(stem2)
    '''

def almostmain(lexeme, paradigm, transl_ru, gramm):
    if gramm[0] == u'V':
        stem = verbstem(lexeme, paradigm, gramm, transl_ru)
        if stem == u'aaa':
            print u'some_stem_problem', lexeme, paradigm
            return
    else:
        stem = lexeme
    wordinf = u'-lexeme\r\n lex: ' + lexeme + u'\r\n stem: ' + stem + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigm + u'\r\n transl_ru: ' + transl_ru + u'\r\n'
    wordinf = wordinf.replace(u'|.\r\n', u'\r\n')
    nd.write(wordinf)

nazv = u'All_dict_polyakov.txt'
od = codecs.open(nazv, "r", "utf-8")
nd = codecs.open(u'new_dict.txt', u'w', u'utf-8')
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
            #print u'тоска', lexeme
            continue
    gramm = info.group(2)
    try:
        paradigm = info.group(3)
        if u'<em>' in paradigm:
            hi = re.search(u'<em>(.+)</em>', paradigm)
            transl_ru = hi.group()
            paradigm = u''
    except:
        paradigm = u''
    #print paradigm
    if transl_ru == u'':
        transl_ru = info.group(4)
    if transl_ru == None:
        transl_ru = u''
    #print transl_ru
    almostmain(lexeme,paradigm,transl_ru,gramm)
    '''
    if gramm[0] == u'V':
        stem = verbstem(lexeme, paradigm)
        if stem == u'aaa':
            continue
    else:
        stem = lexeme
    wordinf = u'-lexeme\r\n lex: ' + lexeme + u'\r\n stem: ' + stem + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigm + u'\r\n transl_ru: ' + transl_ru + u'\r\n'
    wordinf = wordinf.replace(u'|.\r\n', u'\r\n')
    nd.write(wordinf)
    '''

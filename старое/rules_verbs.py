#-*- coding: utf-8 -*-

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
    return stems
def begl_jat(orig):
    stems = []
    for word in orig:
        if word[-1] == u'ѣ':
            word1 = word[:-1]
            stems.append(word1)
def ov(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] == u'а' and word[-2] == u'в' and word[-3] == u'о':
            word1 = word[:-3] + u'у'
            stems.append(word1)
        if word[-1] == u'а' and word[-2] == u'в' and word[-3] == u'е':
            word1 = word[:-3] + u'ю'
            stems.append(word1)
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
        #elif word[-1] == u'т':
        #    if word[-2] != u'c':
         #       word1 = word[:-1] + u'щ'
          #      stems.append(word1)
           # if word[-2] == u'с':
            #    word1 = word[:-2] + u'щ'
             #   stems.append(word1)
    return stems
def change_k(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ч'
            stems.append(word1)
    return stems
def change_psti(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] == u'п':
            word1 = word[:-1]
            stems.append(word1)
        if word[-1] == u'б':
            word1 = word[:-1]
            stems.append(word1)
        else:
            print u'wow'
    return stems
def add_d(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] != u'д':
            word1 = word + u'д'
            stems.append(word1)
        else:
            print u'wow'
    return stems
def t_e_0(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word[:-1]+u'т'
            word2= word[:-1]
            stems.append(word1)
            stems.append(word2)
        else:
            print u'wow'
    return stems
def k_ch_c_0(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1= word+u'к'
            word2= word+u'ч'
            word3= word+u'ц'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
        else:
            print u'wow'
    return stems
def zh_zh(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
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
            print u'wow'
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
            print u'wow'
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
            print u'wow'
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
            print u'wow'
    return stems
def s_st(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] != u'т':
            word1 = word + u'т'
            stems.append(word1)
        else:
            print u'wow'
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
            print u'wow'
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
            print u'wow'
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
            print u'wow'
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
            print u'wow'
    return stems
def er(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in vowels:
            word1 = word[:-1]
            word2 = word[:-2]+u'е'+word1[-1]
            stems.append(word1)
            stems.append(word2)
        if word[-1] not in vowels:
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
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1=word[:-1]+u'н'
        stems.append(word1)
    return stems
def vvv(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1=word+u'в'
        stems.append(word1)
    return stems
def add_l(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1=word+u'л'
        stems.append(word1)
    return stems
def add_sh(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1=word[:-1]+u'щ'
        stems.append(word1)
    return stems
def idti(orig):
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if len(word) <=1 or (word[-1] == u'и' and word[-2] in vowels):
            word1=word+u'д'
            if len(word) <= 1:
                word2=u'ш'
            elif len(word) > 1:
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
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        word1 = word+u'д'
        stems.append(word1)
    return stems

def osninf(inf, paradigm):
    dwa = [u'V14st', u'V11a',	u'V11e', u'V12ov', u'V14z', u'V14k', u'V14g',	u'V14g*',	u'V14eg', u'V15er',	u'V15ol',	u'V15el',	u'V15i',u'V15y',	u'V15e', u'V15n',	u'V15a', u'V15v', u'Viti',	u'Vexat',	u'Vdat']
    tri = [u'V14t*', u'V14ed', u'V14t',u'V14d', u'V14p', u'V13a', u'V21n', u'V21a', u'V21s', u'V21p',	u'V21t', u'V22n', u'V22p', u'V22t',	u'V22s', u'V22a', u'V12ov',	u'V12n', u'V12p', u'V12t', u'V12k', u'V12a', u'Vest', u'Vved', u'Vima', u'V12x',	u'V12x*', u'V13p+V22s',	u'V12t+V22t']
    four =[u'V13t',	u'V13k']
    if paradigm in dwa:
        infstem = inf[:-2]
    elif paradigm in tri:
        infstem = inf[:-3]
    elif paradigm in four:
        infstem = inf[:-4]
    else:
        print u'грусть'
    print infstem
    return infstem


def main():
    paradigm = raw_input(u'Введите тип парадигмы: ').decode(u'utf-8')
    infi = raw_input(u'Введите инфинитив: ').decode(u'utf-8')
    osnova = osninf(infi, paradigm)
    stem = []
    stem.append(osnova)
    #stem1=[]
    stem2=[]
    if paradigm == u'V14st':
        stem1 = s_st(stem)
    if paradigm == u'V14p':
        stem1 = change_psti(stem)
    if paradigm == u'V14d':
        stem1 = add_d(stem)
    if paradigm == u'V14t':
        stem1 = add_t(stem)
    if paradigm == u'V14t*':
        stem1 = t_e_0(stem)
    if paradigm == u'V14ed':
        stem1 = sed(stem)
    if paradigm == u'V14k':
        stem1 = k_ch_c_0(stem)
    if paradigm == u'V14g':
        stem1 = g_zh_z_0(stem)
    if paradigm == u'V14g*':
        stem1 = zh_zh(stem)
    if paradigm == u'V14eg':
        stem1 = eg(stem)
    if paradigm == u'V15el':
        stem1 = el(stem)
    if paradigm == u'V15ol':
        stem1 = ol(stem)
    if paradigm == u'V15or':
        stem1 = change_or(stem)
    if paradigm == u'V15er':
        stem1 = er(stem)
    if paradigm == u'V15e':
        stem1 = eee(stem)
    if paradigm == u'V15n':
        stem1 = mya(stem)
    if paradigm == u'V15v':
        stem1 = vvv(stem)
    if paradigm == u'V13p+V22s':
        stem1 = add_l(stem)
    if paradigm == u'V12t+V22t':
        stem1 = add_sh(stem)
    if paradigm == u'Viti':
        stem1 = idti(stem)
    if paradigm == u'Vexat':
        stem1 = exat(stem)
    if paradigm == u'Vved':
        stem1 = exat(stem)
    if paradigm == u'V21p':
        stem1 = add_l(stem)
    if paradigm == u'V22p':
        stem1 = add_l(stem)
    if paradigm == u'V21t':
        stem1 = change_dsz(stem)
    if paradigm == u'V22t':
        stem1 = change_t(stem)
    if paradigm == u'V11e':
        stem1 = begl_jat(stem)
    if paradigm == u'V12ov':
        stem1 = ov(stem)
    if paradigm == u'V12p':
        stem1 = add_l(stem)
    if paradigm == u'V12t':
        stem1 = change_dsz(stem)
    if paradigm == u'V12k':
        stem1 = change_k(stem)
    if paradigm == u'V12g':
        stem1 = change_k_g_h(stem)
   # elif paradigm == u'V12x*':
    #    stem1 = change_k_g_h(stem)
    if paradigm == u'V13k':
        stem1 = change_k_g_h(stem)




#тестовая часть
     #if paradigm == u'':
      #  stem1 =
    print u'stem1'
    print u' '.join(stem1)
    if len(stem2)>0:
        print u'stem2'
        print u' '.join(stem2)


main()






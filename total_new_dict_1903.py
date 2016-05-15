#-*- coding: utf-8 -*-
import re
import codecs
import json

# штуки про опфографическую вариативность

def clearredcf(stems):
    test = 0
    if stems == u'ни.же':
        test = 1
    stems = clearinfo(stems)
    stems = redundantstems(stems)
    stems = restofcf(stems)
    stems = no_punctum_in_stem(stems)
    return stems

def restofcf(stems):
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
                    stems2en = maincf(stems2e)
                    if stems2en != None:
                        stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a)
                stems1a.append(stems2)
            else:
                stems2a = []
                # stems2a.append(stems1e)
                stems2en = maincf(stems1e)
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
                stems1en = maincf(stems1e)
                if stems1a != None:
                    stems1a.append(stems1en)
            stems1 = u'.//'.join(stems1a)
        else:
            # print u'nothing in stems'
            # stems = stems.replace(u'.', u'') # Надо? нет, так удаляется . посередине основы
            stemsa = []
            # print u'еще помним, что тут?', stems
            # stemsa.append(stems)
            for item in stemsa:
                pass
                # print u'check1', item
            stemsen = maincf(stems)
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

def maincf(word):
    try:
        word = ery(word)
    except:
        #print word
        pass
    # word = begend(word)
    return word

def begend(word):
    try:
        if word[-1] == u'ъ':
            word = word[:-1]
    except:
        pass
    return word

def ery(word): # 0912 меняем на удаление
    # cons = u'цкнгшщзхфвпрлджчсмтб'
    word2 = re.sub(u'([цкнгшщзхфвпрлджчсмтб])(ь|ъ)([цкнгшщзхфвпрлджчсмтб])', u'\\1\\3', word)
    return word2

def gospod(word):
    if word[:4] == u'госп':
        word = u'осп' + word[4:]
    return word

def changefirst_e_a(word):
    if len(word) > 3 and word[0] == u'е':
        # print u'like a one', word
        word1 = u'о' + word[1:]
    elif len(word) > 3 and word[0] == u'а':
        # print u'like a lam', word
        word1 = u'я' + word[1:]
    else:
        word1 = word
    return word1

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

def odezhda(word):
    if u'жд' in word:
        # print word, u'жд'
        word1 = word.replace(u'жд', u'ж')
    else:
        word1 = word
    return word1

def moreproblemsnou(word):
    words = []
    word0 = odezhda(word)
    word1 = bratija(word)
    words.append(word0)
    words.append(word1)
    words = list(set(words))
    words = u'.//'.join(words)
    return words

def moreproblems1(word):
    # print u'problem1'
    words = [word]
    if word == None:
        return u''
    if word[-5:] == u'еческ':
        # print word, u'еческ'
        word1 = word.replace(u'еческ', u'ецк')
        # print word1
        words.append(word1)
        # word2 = word.replace(u'еческ', u'етск') # 09.12 тс - ц вынесено в коммон форм
        # print word2
        # words.append(word2)
    # print u'p1 found'
    # words = u'.//'.join(words)
    # print words
    return words

def moreproblems2(word):
    if re.search(u'[уеыаоэяиюѣ]г[уеыаоэяиюѣ]', word):
        word1 = re.sub(u'([уеыаоэяиюѣ])г([уеыаоэяиюѣ])', u'\\1\\2', word)
    else:
        return word
    return word1

def moreproblems(word):
    if len(word) == 0:
        return
    if word[-1] == u'.':
        word = word[:-1]
    words = [word]
    # print u'changefirst_e_a'
    word0 = changefirst_e_a(word)
    words = normalize(words, word0)

    # print u'enn'
    words0 = []
    for wordic in words:
        word0 = enn(wordic)
        words0 = normalize(words0, word0)
    words += words0

    words0 = []
    for wordic in words:
        word0 = gospod(wordic)
        words0 = normalize(words0, word0)
    words += words0

    words0 = []
    for wordic in words:
        word0 = boary(wordic)
        words0 = normalize(words0, word0)
    words += words0

    # 09.12 гласный + йотированный вынесено в коммонформ
    # 21.03 возвращаем бояр, надеюсь, всё будет хорошо. Не помню, почему удалила

    # print u'mp2'
    words0 = []
    for wordic in words:
        word0 = moreproblems2(wordic)
        words0 = normalize(words0, word0)
    words += words0

    words0 = []
    for wordic in words:
        word0 = vypadenie(wordic)
        words0 = normalize(words0, word0)
    words += words0

    '''words0 = []
    for wordic in words:
        word0 = fromcf(wordic)
        words0 = normalize(words0, word0)
    words += words0'''  # 09.12 вынесено в коммонформ

    # print u'mp1'
    words0 = []
    for wordic in words:
        word0 = moreproblems1(wordic)
        for word0ic in word0:
            words0 = normalize(words0, word0ic)
    words += words0

    # print u'enneenno'
    words0 = []
    for wordic in words:
        word0 = enneenno(wordic)
        words0 = normalize(words0, word0)
    words += words0

    words0 = []
    for wordic in words:
        word0 = samelettter(wordic) # нужно внести ограничения на части речи? вообще подумать
        words0 = normalize(words0, word0)
    words += words0

    '''words0 = []
    for wordic in words:
        word0 = happiness(wordic) # 09.12 сч-щ вынесено в коммонформ
        words0 = normalize(words0, word0)
    words += words0'''


    # print u'problems_finished'
    words = set(words)
    wordline = u''
    for wordic in words:
        if wordic != None:
            wordline = wordline + wordic + u'.//'
    return wordline

def boary(word):
    """word = re.sub(u'([иь])у', u'\\1ю', word)
    word = re.sub(u'([иь])ы', u'ы', word)
    word = re.sub(u'([иь])а', u'\\1я', word)
    word = re.sub(u'([иь])о', u'\\1ё', word)
    word = re.sub(u'([иь])и', u'\\1й', word)"""
    word = word.replace(u'уа', u'уя')
    word = word.replace(u'еа', u'ея')
    word = word.replace(u'ыа', u'ыя')
    word = word.replace(u'оа', u'оя')
    word = word.replace(u'эа', u'эя')
    word = word.replace(u'яа', u'яя')
    word = word.replace(u'иа', u'ия')
    word = word.replace(u'юа', u'юя')
    word = word.replace(u'аа', u'ая')
    return word # пока больше не используется, посмотреть внимательнее на первую часть
    # 21.03 возвращаем в оборот, первую часть на всякий случай закомментила, не помню, в чем была проблема; сейчас создается копия, на самом деле в этом нет необходимости, хватит просто замены

def enn(word):
    if word[-2:] == u'нн':
        word2 = word[:-2] + u'н'
    elif word[-2:] == u'ен':
        word2 = word[:-2] + u'енн'
    elif word[-4:] == u'енно':
        word2 = word[:-4] + u'ено'
    elif word[-3:] == u'ено':
        word2 = word[:-3] + u'енно'
    elif word[-4:] == u'енне':
        word2 = word[:-4] + u'ене'
    elif word[-3:] == u'ене':
        word2 = word[:-3] + u'енне'
    elif word[-4:] == u'инно':
        word2 = word[:-4] + u'ино'
    elif word[-3:] == u'ино':
        word2 = word[:-3] + u'инно'
    else:
        word2 = word
    return word2

def enneenno(word):
    # print u'real enneenno'
    if word[-4:] == u'енно':
        word2 = word[:-4] + u'енне'
    elif word[-4:] == u'ено':
        word2 = word[:-4] + u'ене'
    elif word[-3:] == u'ене':
        word2 = word[:-3] + u'ено'
    elif word[-3:] == u'енне':
        word2 = word[:-3] + u'енно'
    else:
        word2 = word
    # print u'real enneenno_2'
    return word2

def samelettter(word):
    word = word.replace(u'нн', u'н')
    word = word.replace(u'сс', u'с')
    word = word.replace(u'жж', u'ж')
    word = word.replace(u'зз', u'з')
    word = word.replace(u'вв', u'в')
    word = word.replace(u'тт', u'т')
    word = word.replace(u'лл', u'л')
    word = word.replace(u'дд', u'д')
    return word

def normalize(words, word0):
    words.append(word0)
    words = set(words)
    words = list(words)
    return words

def bratija(word):
    try:
        if word[-1] == u'и':
            word1 = word[:-1] + u'ь'
        else:
            word1 = word
        return word1
    except:
        # print u'в братие короткое слово, что за чудо?', word
        return word

def happiness(word):  # 09.12 вынесено в коммонформ
    word = word.replace(u'сч', u'щ')
    word = word.replace(u'жч', u'щ')
    return word

def fromcf(word2):  # 09.12 вынесено в коммонформ
    word2 = word2.replace(u'дч', u'дш')
    word2 = word2.replace(u'дщ', u'дш')
    return word2

def vypadenie(word):
    word = word.replace(u'стн', u'сн')
    word = word.replace(u'зтн', u'зн')
    word = word.replace(u'сдн', u'сн')
    word = word.replace(u'здн', u'зн')
    word = word.replace(u'гск', u'ск')
    word = word.replace(u'кск', u'ск')
    word = word.replace(u'нтс', u'нс')
    return word

def verbprefixgood(wordo):
    word = wordo
    if word[:2] == u'ис':
        word = u'раз' + word[2:]
    elif word[:2] == u'из':
        word = u'ис' + word[2:]
    if word[:2] == u'ис':
        word = u'из' + word[2:]
    elif word[:3] == u'раз':
        word = u'рас' + word[3:]
    if word[:3] == u'вос':
        word = u'воз' + word[3:] + u'.//' + u'вз' + word[2:] + u'.//' + u'вс' + word[2:]
    elif word[:3] == u'воз':
        word = u'вос' + word[3:] + u'.//' + u'вз' + word[2:] + u'.//' + u'вс' + word[2:]
    if word[:3] == u'рос':
        word = u'роз' + word[3:]
    elif word[:3] == u'роз':
        word = u'рос' + word[3:]
    if word[:3] == u'бес':
        word = u'без' + word[3:]
    elif word[:3] == u'без':
        word = u'бес' + word[3:]
    if word[:4] == u'чрес' or word[:5] == u'черес' or word[:5] == u'чьрес':
        word = u'через' + word[5:]
    elif word[:5] == u'через':
        word = u'черес' + word[5:] + u'.//' + u'чрес' + word[5:]
    if word != wordo:
        return word
    return

def verbbadprefix(word): # 09.12 убраны ъ, слдить за +со
    if word[:2] == u'сг' or word[:2] == u'сз' or word[:2] == u'св' or word[:2] == u'сд' or word[:2] == u'сж' or word[:2] == u'сб':
        word1 = u'з' + word[1:]
    if re.match(u'с[кншщхвпрлджчстб]', word):
        word2 = u'со' + word[1:]
    elif word[:2] == u'со':
        word2 = u'с' + word[2:]
    try:
        return word1 + u'.//' + word2
    except:
        return

def verbprefix(word):
    word2 = verbbadprefix(word)
    word3 = verbprefixgood(word)
    if word2 != None:
        return word2
    else:
        return word3

# В эту фунцкию просто страшно заглядывать; я плохо помню, что она делает, кажется, по очереди заходит во все основы и вызывает для них moreproblems, --noun, --verb
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
                    elif gramm[0] == u'V':
                        stems2en = verbprefix(stems2e)
                        if stems2en != None:
                            stems2a.append(stems2en)
                    elif gramm == u'A':
                        stems2en = moreproblemsadj(stems2e)
                        if stems2en != None:
                            stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a)
                stems2 = del_over(stems2)
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
                elif gramm[0] == u'V':
                    stems2en = verbprefix(stems1e)
                    if stems2en != None:
                        stems2a.append(stems2en)
                elif gramm == u'A':
                    stems2en = moreproblemsadj(stems1e)
                    if stems2en != None:
                        stems2a.append(stems2en)
                stems2 = u'.//'.join(stems2a)  # ?
                stems2 = del_over(stems2)
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
                elif gramm[0] == u'V':
                    stems2en = verbprefix(stems1e)
                    if stems2en != None:
                        stems1a.append(stems2en)
            stems1 = u'.//'.join(stems1a)
            stems1 = del_over(stems1)
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
            stems1 = del_over(stems1)
    return stems1

def del_over(stems1): # что делает????
            stems1 = stems1.split(u'//')
            stems1 = set(stems1)
            stems1 = list(stems1)
            stems1 = u'.//'.join(stems1)
            return stems1

# глаголы, порождение косвенных основ
def v12xstar(orig):
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    for word in orig:
        if word[-1] in consonants and word[-2] in consonants:
            word1 = word[:-1] + u'е' + word[-1]
            stems.append(word1)
            # print word1, u'V12x*'
        else:
            return u'wrong'
            print u'v12star_wow', orig[0]
    # print stems[0], u'V12x'
    return stems
def add_l(orig):
    # ВОЗМОЖНА ВЫДАЧА МАССИВА
    stems = []
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    # word = list(word)
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
            #print u'change_gdz_wow', orig[0]
            return u'wrong' #эта парадигма к этому глаголу отношения не имеет
    return stems
def begl_jat(orig):
    stems = []
    for word in orig:
        if word[-1] == u'ѣ' or word[-1] == u'я' or word[-1] == u'е':
            word1 = word[:-1]
            stems.append(word1)
        else:
            #print u'Begl_jat_wow', orig[0]
            return u'wrong' #эта парадигма к этому глаголу отношения не имеет
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
            #print u'ov_wow', orig
            return u'wrong' #эта парадигма к этому глаголу отношения не имеет
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
            return u'wrong'
            print u'change_k_g_h_wow', orig
    return stems
def change_t(orig):
    stems = []
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
            return u'wrong' #эта парадигма к этому глаголу отношения не имеет
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
            #print u'change_k_wow', orig[0]
            return u'wrong' #эта парадигма к этому глаголу отношения не имеет
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
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
    for word in orig:
        if word[-1] in vowels:
            word1= word+u'г'
            word2= word+u'ж'
            word3= word+u'з'
            stems.append(word1)
            stems.append(word2)
            stems.append(word3)
        else:
            return u'wrong'
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

# сущ и прил, порождение косвенных основ
def beglyi(orig):
    #удаляем последний гласный основы(после него макс 3), соответсвует * у полякова
    '''if orig == [u'камен']:
        print u'камень преобразуется'''''
    stems = []
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    if orig[-1] in consonants and orig[-2] in vowels and orig[-3] in vowels: #  паук case
        return u'wrong'
    for word in orig:
        word = list(word)
        if word[-1] in consonants:
            if word[-2] in vowels:
                del word[-2]
            elif word[-3] in vowels:
                del word[-3]
            else:
                return u'wrong'
                print u'beglyi_v_wow', orig[0]
        else:
            # print u'beglyi_c_wow', orig[0]
            return u'wrong'
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
            # print u'palatal_k_wow', orig[0]
            return u'wrong'
    return stems
def palatal_g_h(orig):
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
            # print u'palatal_g_wow', orig[0]
            return u'wrong'
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
            # print u'palatal_k_g_wow', orig[0]
            return u'wrong'
    return stems
def change_c(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант звонких
    stems = []
    for word in orig:
        if word[-1] == u'ц':
            word1 = word[:-1] + u'ч'
        else:
            # print u'change_c_wow', orig[0]
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong' #не та парадигма
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
            stems = [orig[0] + u'.|' + orig[0] + u'.']
            #print stems
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
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
            return u'wrong'
            print u'narash_at_wow', orig[0]
        stems.append(word1)
    return stems

# порождение нулевой основы, а так же добавление всяких основ, если их не хватает
def osninf(inf, paradigm):
    dwa = [u'V12g', u'V11u', u'V14st', u'V11a', u'V11e', u'V12ov', u'V14z', u'V14k', u'V14g',	u'V14g*',	u'V14eg', u'V15er',	u'V15ol', u'V15or',	u'V15el',	u'V15i',u'V15y',	u'V15e', u'V15n',	u'V15a', u'V15v', u'Viti',	u'Vexat',	u'Vdat']
    tri = [u'V14et', u'V14t*', u'V14ed', u'V14t',u'V14d', u'V14p', u'V13a', u'V21n', u'V21a', u'V21s', u'V21p',	u'V21t', u'V22n', u'V22p', u'V22t',	u'V22s', u'V22a', u'V12ov',	u'V12n', u'V12p', u'V12t', u'V12k', u'V12a', u'Vest', u'Vved', u'Vima', u'V12x',	u'V12x*', u'V13p+V22s',	u'V12t+V22t']
    four =[u'V13t',	u'V13k']
    if paradigm == u'Vbyt':
        print u'так не должно быть'
        return u'aaa'
    if u'+' in inf:
        print u'печаль', paradigm  # печали нет
        return u'aaa'
    if inf[-2:] == u'ся':
        inf = inf[:-2]
    if paradigm in dwa:
        infstem = inf[:-2]
        # if infstem.startswith(u'благорас'):
           # print infstem
    elif paradigm in tri:
        infstem = inf[:-3]
    elif paradigm in four:
        infstem = inf[:-4]
    else:
        if u'/' in paradigm:
            return u'difV'
        else:
            #print u'грусть', paradigm, inf #грксти нет
            return u'aaa'
    #print infstem
    return infstem

def pro_stem(dic_word, paradigm):
    libo = 0
    if dic_word[-4:] == u'либо':
        libo = 1
        dic_word = dic_word[:-4]
    zdo = 0
    if dic_word[-3:] == u'ждо':
        zdo = 1
        dic_word = dic_word[:-3]
    ze = 0
    if dic_word[-2:] == u'же':
        ze = 1
        dic_word = dic_word[:-2]
    zde = 0
    if dic_word[-3:] == u'жде':
        zde = 1
        dic_word = dic_word[:-3]
    if dic_word[-1] == u'й' or dic_word[-1] == u'и':
        stem0 = dic_word[:-2]
    elif dic_word[-1] == u'ъ' or dic_word[-1] == u'ь':
        stem0 = dic_word[:-1]
    else:
        # print u'это и', dic_word
        return u'и.'
    stem0 = test_particle(libo, stem0, u'либо')
    stem0 = test_particle(ze, stem0, u'же')
    stem0 = test_particle(zde, stem0, u'жде')
    stem0 = test_particle(zdo, stem0, u'ждо')
    return stem0

def test_particle(particle, dic_word, part):
    if particle == 1:
        dic_word = dic_word + u'.' + part
    else:
        dic_word = dic_word + u'.'
    return dic_word

def osnnoun(dic_word, paradigm):
    if paradigm == u'Pro':
        stem0 = pro_stem(dic_word, paradigm)
    elif paradigm == u'NUM' or paradigm == u'N1t' or paradigm == u'N6t' or paradigm == u'N3j' or paradigm == u'N1c' or paradigm == u'N1t*' or paradigm == u'N1k' or paradigm == u'N1g' or paradigm == u'N1k*' or paradigm == u'N1s' or paradigm == u'N1c*' or paradigm == u'N1t_STAR' or paradigm == u'N1k_STAR' or paradigm == u'N1c_STAR':
        stem0 = dic_word[:-1]  #минус ъ
    elif paradigm == u'N1a' or paradigm == u'N1i' or paradigm == u'N1e':
        stem0 = dic_word[:-1]     #минус й
    elif paradigm == u'N1in':
        stem0 = dic_word[:-3]     #минус инъ
    elif paradigm == u'N2t' or paradigm == u'N2t*' or paradigm == u'N2k' or paradigm == u'N2t_STAR':
        stem0 = dic_word[:-1]     #минус о
    elif paradigm == u'N2s' or paradigm == u'N2c' or paradigm == u'N2c*' or paradigm == u'N2i' or paradigm == u'N2e' or paradigm == u'N2j':
        stem0 = dic_word[:-1]     #минус е
    elif paradigm == u'N3t' or paradigm == u'N3t*' or paradigm == u'N3k' or paradigm == u'N3k*' or paradigm == u'N3s' or paradigm == u'N3c' or paradigm == u'N3c*' or paradigm == u'N3k_STAR' or paradigm == u'N3c_STAR':
        stem0 = dic_word[:-1]     #минус а
    elif paradigm == u'N3j*' or paradigm == u'N3a' or paradigm == u'N3i' or paradigm == u'N3j_STAR':
        stem0 = dic_word[:-1]     #минус я
    elif paradigm == u'N3e':
        stem0 = dic_word[:-1]     #минус а/я
    elif paradigm == u'N41' or paradigm == u'N42' or paradigm == u'N43' or paradigm == u'N43*' or paradigm == u'N5*ov' or paradigm == u'N1j' or paradigm == u'N1j*' or paradigm == u'N1sj' or paradigm == u'N1j_STAR' or paradigm == u'N5_STAR_ov':
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
        stem0 = u'No_paradigm'
    '''if dic_word == u'камень':
        print u'режем камень', paradigm, stem0'''
    return stem0

def add_verb_parad(paradigm): # 15/02 ощущение, что оригинальные раньше бесследно терялись, если я правильно представляю, как это работает, сейчас добавлю;
    # вообще, пугает эта функция. Зачем добавляется столько парадигм? что с оригинальными было не так?
    # print u'add_verb_parad'
    if paradigm == u'V11u':
        paradigm = u'V11a/V11e/V11u'
    if paradigm == u'V14et':
        paradigm = u'V14p/V14z/V14t/V14d/V14st/V14t*/V14ed/V14k/V14g/V14g*/V14eg/V14et'
    if paradigm == u'V12g':
        paradigm = u'V12ov/V12n/V12p/V12t/V12k/V12a/V12x/V12x*/V12g'
    '''if paradigm == u'V12p+V22s':
        paradigm = u'V13p+V22s'''  # Не помню, зачем это было нужно. Парадигмы V13p+V22s в парадигмах нет, и в словаре тоже нет. Что я имел в виду?
    if paradigm == u'V12x':
        paradigm += u'/V12x*'
    return paradigm


def verbstem(lexeme, paradigm, testq, test):
    # print u'verbstem working'
    # print test
    if test == 1:
        print u'verbstem', lexeme, paradigm
    if testq == 0:
        # print u'testq=0 in verbstem'
        paradigm = add_verb_parad(paradigm)
    if test == 1:
        print u'verbstem_2', lexeme, paradigm
    infi = lexeme
    osnova = osninf(infi, paradigm)
    if test == 1:
        print u'verbstem_3', lexeme, paradigm, osnova
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
    if test == 1:
        print u'verbstem_4', lexeme, paradigm, result
    return result, paradigm


def nounstem(paradigm, osnova):
    stem = []
    stem.append(osnova)
    if paradigm == u'N1j*':
        # print u'N1j*', osnova
        pass
    '''if osnova == u'камен':
        print u'камень готов'''''
    stemsC = u''
    stem2 = []
    if paradigm == u'N1t*' or paradigm == u'N1j*' or paradigm == u'N1t_STAR' or paradigm == u'N1j_STAR':
        # print u'arigato'
        if len(stem) > 3:
            stem1 = beglyi(stem)
    elif paradigm == u'N1g':
        stem1 = palatal_g_h(stem)
    elif paradigm == u'N1k':
        stem1 = palatal_k(stem)
    elif paradigm == u'N1k*' or paradigm == u'N1k_STAR':
        stem1 = beglyi(stem)
        stem2 = palatal_k(stem1)
    elif paradigm == u'N1c*' or paradigm == u'N1c_STAR':
        stem1 = beglyi(stem)
        stem2 = change_c(stem1)
    elif paradigm == u'N2t*' or paradigm == u'N2t_STAR':
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
    elif paradigm == u'N2c*' or paradigm == u'N2c_STAR':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N3t*' or paradigm == u'N3t_STAR':
        #все 2
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
        stems1 = u'.|'.join(stem1)
        stems2 = u'.|'.join(stem2)
        stems = stems1 + u'.//' + stems2 + u'.'
        stemsC = stems
        stem2 = []
    elif paradigm == u'N3j*' or paradigm == u'N3j_STAR':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N3k':
        #все 2
        stem1 = palatal_k_g_h(stem)
    elif paradigm == u'N3k*' or paradigm == u'N3k_STAR':
        #все 2
        stem1 = vstavnoi_o(stem)
        stem2 = change_k_noun(stem)
    elif paradigm == u'N3c*' or paradigm == u'N3c_STAR':
        #все 2
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'N43*' or paradigm == u'N43_STAR':
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
    elif paradigm == u'N5*ov' or paradigm == u'N5_STAR_ov':
        stem1 = beglyi(stem)
    elif paradigm == u'A1k' or paradigm == u'A1g':
        stem1 = change_k_g_h_adj(stem)
    elif paradigm == u'A1t*' or paradigm == u'A1t_STAR':
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'A1j*' or paradigm == u'A1j_STAR':
        stem1 = vstavnoi_e(stem)
    elif paradigm == u'A1k*' or paradigm == u'A1k_STAR':
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
        stems1 = u'.|'.join(stem1)
        stems2 = u'.|'.join(stem2)
        stems = stems1 + u'.//' + stems2 + u'.'
        stemsC = stems
        stem2 = []
    else:
        if paradigm == u'Pro':
            print u'A-Pro', stem
        # print stem[0], paradigm, u'эт что такое?'
        stem1 = stem[:]
        return stem1[0]
    if len(stemsC) > 0:
        return osnova + u'.|' + stemsC
    stems1 = u'.|'.join(stem1)
    if len(stem2) > 0:
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

def parad_na_yer(stem):
            if re.search(u'([цкнгшщзхфсвпрлджчмтб])[ое]([цкнгшсщзхфвпрлджчмтб])', stem[-3:]):
                paradigm = u'N1t*/N1j*/N1t/N1j/N6t'
            elif re.search(u'[цкнгшщзхфвспрлджчмтб]', stem[-1]):
                paradigm = u'N1t/N1j/N6t'
            if stem[-2:] == u'ск':
                paradigm = u'N1k'
            if stem[-1] == u'г' or stem[-1] == u'х':
                paradigm = u'N1g'
            if re.search(u'([цкнгшщзхфсвпрлджчмтб])ок', stem[-3:]):
                paradigm = u'N1k*'
            if re.search(u'[шжсз]', stem[-1]):
                paradigm = u'N1s'
            if stem[-1] == u'щ' or stem[-1] == u'ч':
                paradigm = u'N1sj'
            if stem[-1] == u'ц':
                paradigm = u'N1c'
            if re.search(u'([цкнгшщзхфвспрлджчмтб])ец', stem[-3:]):
                paradigm = u'N1c*'
            try:
                return paradigm
            except:
                print u'in parad na yer cannot get a paradigm for', stem

def parad_na_yerj(stem):
            paradigm = parad_na_yer(stem)
            if paradigm == u'N1t/N1j/N6t':
                paradigm = u'N1t/N1j/N6t/N41/N42/N43'
            if paradigm == u'N1t*/N1j*/N1t/N1j/N6t':
                paradigm = u'N1t*/N1j*/N1t/N1j/N6t/N41/N42/N43'
            if re.search(u'([цкнгшщзхсфвпрлджчмтб])е([нфвпрлдмтб])', stem[-3:]):
                paradigm = u'N1t*/N1j*/N1t/N1j/N6t/N43*/N41/N42/N43'
            return paradigm

def parad_na_o(stem):
            if re.search(u'[цкнгшщзхфвпрслджчмтб]', stem[-1]):
                paradigm = u'N2t/N5es'
            if re.search(u'([цкнгшщзхфвпрлсджчмтб])([цкнгшщсзхфвпрлджчмтб])', stem):
                paradigm = u'N2t*'
            if stem[-1] == u'к' or stem[-1] == u'г' or stem[-1] == u'х':
                paradigm = u'N2k'
            return paradigm

def parad_na_j(word):
            if word[-2] == u'е':
                paradigm = u'N1e'
            elif word[-2] == u'и' or word[-2] == u'ь':
                paradigm = u'N1i'
            elif re.search(u'[уаоы]', word[-2]):
                paradigm = u'N1a'
            else:
                print u'in nonoinparad cannot get paradigm for', word
            return paradigm

def parad_na_e(stem):
            if re.search(u'[цкнгшщзхсфвпрлджчмтб]', stem[-1]):
                paradigm = u'N2j'
            if re.search(u'[шжсз]', stem[-1]):
                paradigm = u'N2s'
            if stem[-1] == u'ц':
                paradigm = u'N2c'
            if re.search(u'([цкнгшщсзхфвпрлджчмтб])ц', stem[-2:]):
                paradigm = u'N2c/N2c*'
            if stem[-1] == u'и' or stem[-1] == u'ь':
                paradigm = u'N2i'
            if stem[-1] == u'е' or stem[-1] == u'о':
                paradigm = u'N2e'
            if paradigm == None:
                print u'in parad_na_e cannot get paradigm', stem
                return u'N2j'
            return paradigm

def parad_na_a(stem):
            if re.search(u'[цкнгшщзсхфвпрлджчмтб]', stem[-1]):
                paradigm = u'N3t'
            if re.search(u'([цкнгшщзхфвпрсджчмтб])([цкнгшщзхфсвпрлджчмтб])', stem[-2:]):
                paradigm = u'N3t/N3t*'
            if stem[-1] == u'к' or stem[-1] == u'г' or stem[-1] == u'х':
                paradigm = u'N3k'
            if re.search(u'([цкнгшщзхфсвпрлджчмтб])к', stem[-2:]):
                paradigm = u'N3k/N3k*'
            if re.search(u'[шжсз]', stem[-1]):
                paradigm = u'N3s'
            if stem[-1] == u'ц':
                paradigm = u'N3c'
            if re.search(u'[цкнгсшщзхфвпрлджчмтб]ц', stem[-2:]):
                paradigm = u'N3c/N3c*'
            if stem[-1] == u'о' or stem[-1] == u'е':
                paradigm = u'N3e'
            if stem[-1] == u'и' or stem[-1] == u'а':
                paradigm = u'N3i'
            try:
                return paradigm
            except:
                print u'in parad_na_a cannot get paradigm', stem

def parad_na_ja(stem):
            if re.search(u'[цкнгшщсзхфвпрлджчтб]', stem[-1]):
                paradigm = u'N3j/N5et'
            if stem[-1] == u'м':
                paradigm = u'N5en/N5et/N3j'
            if re.search(u'[цкнгшщзхсфвпрлджчмтб][цкнгшщзсхфвпрлджчмтб]', stem[-2:]):
                paradigm = u'N3j/N3j*/N5et'
            if re.search(u'[цкнгшщзхфвспрлджчмтб]м', stem[-2:]):
                paradigm = u'N3j/N3j*/N5et/N5en'
            if re.search(u'[уаы]', stem[-1]):
                paradigm = u'N3a'
            if re.search(u'([цкнгшщсзхфвпрлджчмтб])[иь]', stem[-2:]):
                paradigm = u'N3i'
            if stem[-1] == u'о':
                paradigm = u'N3a/N3e'
            if stem[-1] == u'е':
                paradigm = u'N3e'
            try:
                return paradigm
            except:
                print u'in parad na ja cannot get a paradigm for ', stem

def plur_tantum(word):
            if word[-1] == u'и':
                if word[-2] == u'о' or word[-2] == u'и':
                    wordsing = word[:-1] + u'й'
                    paradigm = predict_noun_parad(wordsing)
                else:
                    wordsing = word[:-1] + u'ь'
                    paradigm = predict_noun_parad(wordsing)
                wordsing = word[:-1] + u'я'
                paradigm = paradigm + u'/' + predict_noun_parad(wordsing)
                # paradigm = u'N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1a/N1i/N1e/N3j/N3j*/N3k/N3k*/N3s/N3a/N3i/N3e/N41/N42/N5er/N5ov/N5*ov'
            elif word[-1] == u'ы':
                wordsing = word[:-1] + u'ъ'
                paradigm = predict_noun_parad(wordsing)
                wordsing = word[:-1] + u'а'
                paradigm = paradigm + u'/' + predict_noun_parad(wordsing)
                # paradigm = u'N1t/N1t*/N1c/N1c*/N3t/N3t*/N3c/N3c*/N43/N43*'
            else:
                paradigm = u'unchangeable'
            return paradigm

def predict_noun_parad(word):
        if word[-1] == u'ъ':
            stem = word[:-1]
            paradigm = parad_na_yer(stem)
            # paradigm = u'N1t/N1t*/N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1c/N1c*/N6t'
        elif word[-1] == u'ь':
            stem = word[:-1]
            paradigm = parad_na_yerj(stem)
            # paradigm = u'N1t/N1t*/N1j/N1j*/N1k/N1g/N1k*/N1s/N1sj/N1c/N1c*/N5*ov/N41/N42/N43/N43*' # N5*ov не приписываем, так как совпадает с плюралия тантум (как любы)
        elif word[-1] == u'о':
            stem = word[:-1]
            paradigm = parad_na_o(stem)
            # paradigm = u'N2t/N2t*/N2k/N5es'
            # print word, u'примерчик'
        elif word[-1] == u'й':
            paradigm = parad_na_j(word)
            # paradigm = u'N1i/N1e'  # добавление N1in добавляло много омонимии, так как создавалось много слов с пустыми основами
        elif word[-1] == u'е':
            stem = word[:-1]
            paradigm = parad_na_e(stem)
            # paradigm = u'N2j/N2s/N2c/N2c*/N2i/N2e'
        elif word[-1] == u'а':
            stem = word[:-1]
            paradigm = parad_na_a(stem)
            # paradigm = u'N3t/N3t*/N3k/N3k*/N3s/N3c/N3c*/N3e'
        elif word[-1] == u'я':
            stem = word[:-1]
            paradigm = parad_na_ja(stem)
            # paradigm = u'N3j/N3j*/N3a/N3i/N3e/N5en/N5et/N5en'
        elif word[-4:] == u'мати':
            paradigm = u'N5er'
        else:  # если мы точно знаем, что это существительное, но ничего сверху не подходит (может быть pluralia tantum)
            # print word, u'pluralia tantum?'
            paradigm = plur_tantum(word)
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
        paradigm = predict_noun_parad(word)
    elif pos == u'A':
        if word[-2:] == u'ый' or word[-2:] == u'ыи' or word[-2:] == u'ий' or word[-2:] == u'ии':
            paradigm = u'A1t/A2t/A1j/A2j/A1k/A1g/A1s/A1i/A1t*/A1j*/A1k*'
        else:
            print u"what a paradigm A?", word
    elif pos == u'A-PRO': # местоимение-прилагательное, это в словаре не тег парадигмы а тег частиречи а парадигмы там нет. зато у меня есть:
        paradigm = u'Pro'
        # print u'A-pro', lexeme, gramm, paradigm
    elif u'N-PRO': # местоимение-существительное, это в словаре не тег парадигмы а тег частиречи а парадигмы там нет.
        paradigm = u'N-PRO'
    else:
        print u'What a pos?', word, pos
    return paradigm

def irrstems(lexeme, paradigm, iryd, irsd):
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
                    # print u'testq=0, call verbstem'  # Это никогда не выполняется. Норм?
                    testq = 0
                    stem, paradigm = verbstem(lexeme, paradigm, testq)
                return stem

def toska(lexeme, gramm):
    lex = lexeme.split(u'+')
    lexeme = lex[0]
    if gramm[0] == u'V':
        return lexeme
    else:
        chast = lex[1]
        return lexeme, chast

def historyparadigm(paradigm, word):  # also no_noun_parad
    add_paradigm = u''
    if word == u'волъ' or word == u'полъ' or word == u'медъ' or word == u'вьрхъ' or word == u'домъ' or word == u'буйволъ' or word == u'мидъ':
        add_paradigm += u'/N6t'
        # print word
    if word == u'камень':
        add_paradigm += u'/N5en'
    if u'N43' in paradigm:
        add_paradigm += u'/N1j//N1j*//N1s//N1sj' # может быть еще N1t//N1t*//N1k//N1g//N1k*//N1c//N1c*//N1a//N1i//N1e//N1in
    if u'N1j' in paradigm:
        add_paradigm += u'/N42'
    if u'N5er' in paradigm or u'N5ov' in paradigm or u'N5*ov' in paradigm:
        add_paradigm += u'/N41'
    # if  u'N5en' in paradigm: # N1j//N1j*//N1s//N1sj стерли из-за имени, которое в им падеже получало генетив
    if  u'N5et' in paradigm or u'N5es' in paradigm:
        add_paradigm += u'/N1j//N1j*//N1s//N1sj' # может быть еще N1t//N1t*//N1k//N1g//N1k*//N1c//N1c*//N1a//N1i//N1e//N1in
    if u'N1t' in paradigm:
        add_paradigm += u'/N1t*'
    if u'N2t' in paradigm:
        add_paradigm += u'/N2t*'
    if u'N2c' in paradigm:
        add_paradigm += u'/N2c*'
    if u'N1k' in paradigm:
        add_paradigm += u'/N1k*'
    if add_paradigm == u'':
        return
    add_paradigm = add_paradigm.replace(u'//', u'/')
    return add_paradigm

def getAllVerb(paradigm, lexeme, test, iryd, irsd, truetest=0):
            if truetest == 1:
                print paradigm, lexeme, u'this is interesting'
            if test == 1:
                print u'getAllVerb', lexeme, paradigm
            if u'/' in paradigm:
                stem = u'difV'
            elif paradigm == u'Vbyt':
                stem = lexeme[:-4]
            else:
                try:
                    stem = irrstems(lexeme, paradigm, iryd, irsd)
                except:
                    # print u'testq=0, call verbstem'
                    testq = 0
                    # print testq
                    stem, paradigm = verbstem(lexeme, paradigm, testq, test)
                    if test == 1:
                        print u'getAllVerb_1,5', lexeme, paradigm, stem
                if stem == u'no_paradigm':
                    paradigm = noverbparad(lexeme)
                if test == 1:
                    print u'getAllVerb_2', lexeme, paradigm
            return paradigm, stem

def getAllNoun(paradigm, lexeme):
            if paradigm == u'А2sj':
                paradigm = u'A1i/A1s/A1j'
            if u'N3k' in paradigm:
                paradigm += u'/N3k*'
            if u'N3t' in paradigm and len(lexeme) > 4:
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
                        if paradigm == u'Pro':
                            print u'A-pro', lexeme, stem0
                        stem0 = osnnoun(lexeme, paradigm)
                        stem = nounstem(paradigm, stem0)
                else:
                    stem0 = osnnoun(lexeme, paradigm)
                    stem = nounstem(paradigm, stem0)
            return paradigm, stem

def getAllParadigm_getStem(gramm, paradigm, lexeme, test, iryd, irsd, truetest=0):
    if truetest == 1:
        print paradigm, lexeme, u'this is interesting'
    try:
        if gramm[0] == u'V':
            paradigm, stem = getAllVerb(paradigm, lexeme, test, iryd, irsd)
        elif gramm == u'N-PRO':
            if u'что' in lexeme or u'кто' in lexeme:
                paradigm, stem = who_what(lexeme)
            elif lexeme == u'азъ':
                paradigm = u'me'
                stem = u'.'
            elif lexeme == u'вы':
                paradigm = u'vy'
                stem = u'.'
            elif lexeme == u'мы':
                paradigm = u'we'
                stem = u'.'
            elif lexeme == u'ты':
                paradigm = u'you'
                stem = u'.'
            elif lexeme == u'и':
                paradigm = u'uk-i-m'
                stem = u'.'
            elif lexeme == u'иже':
                paradigm = u'uk-i-m'
                stem = u'.же'
            elif lexeme == u'себе':
                paradigm = u'self'
                stem = u'.'
            else:
                # print u'N-PRO', lexeme
                paradigm = u'unchangeable'
                stem = lexeme + u'.'
        elif gramm == u'A' or  gramm[0] == u'N' or gramm[0] + gramm[1] == u'N,' or gramm[0] + gramm[1] == u'A,' or gramm == u'A-PRO':
            paradigm, stem = getAllNoun(paradigm, lexeme)
        else:
            stem = lexeme
            paradigm = u'unchangeable'
    except:
        # paradigm = u'unchangeable'
        stem = lexeme
    try:
        return paradigm, stem
    except:
        print u'getAllP&S чего-то не хватает', lexeme, gramm, paradigm

def foundstem(stem, gramm):
    if stem == u'No_paradigm' or gramm == u'N-PRO':
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
    stem = clearredcf(stem)
    return stem

def noparad(gramm, lexeme):
    lexeme = letterchange(lexeme)
    if gramm[0] == u'V':
        paradigm = noverbparad(lexeme)
    elif gramm[0] == u'N' or gramm[0] == u'A':
        paradigm = nonounparad(lexeme, gramm)
        # if paradigm == u'Pro':
            # print u'A-pro', lexeme
    else:
        paradigm = u'unchangeable'
    return paradigm

def who_what(lexeme):
    # print u'who, what', lexeme
    if u'кто' in lexeme:
        sq = re.search(u'(.*)(кто)(.*)', lexeme)
        paradigm = u'who'
    elif u'что' in lexeme:
        sq = re.search(u'(.*)(что)(.*)', lexeme)
        paradigm = u'what'
    else:
        print u'как мы оказались в who_what, это же не то местоимение', lexeme
        stem = lexeme
        return u'N-PRO', stem
    prefix = sq.group(1)
    postfix = sq.group(3)
    # print prefix, paradigm, postfix
    stem = prefix + u'.' + postfix
    # print stem
    return paradigm, stem

# просто обработка текста и открытие файлов
def letterchange(word):
    newword = word
    newword = newword.replace(u'i', u'и')
    newword = newword.replace(u'і', u'и')
    newword = newword.replace(u'ѡ', u'о')
    newword = newword.replace(u'є', u'e')
    newword = newword.replace(u'́', u'')
    newword = newword.replace(u'́', u'')
    newword = newword.replace(u'ѵ', u'и')
    newword = newword.replace(u'̂', u'')
    newword = newword.replace(u'ѻ', u'о')
    newword = newword.replace(u'ѳ', u'ф')
    newword = newword.replace(u'ѯ', u'кс')
    newword = newword.replace(u'ѱ', u'пс')
    newword = newword.replace(u'ѕ', u'з')
    newword = newword.replace(u'ѣ', u'е')
    newword = newword.replace(u'ꙋ', u'у')
    newword = newword.replace(u'ꙗ', u'я')
    newword = newword.replace(u'ѧ', u'я')
    return newword

def creating_new_dict():
    ml, od, nd, irsd, iryd = openfiles()
    i = 0
    for line in od:
        i += 1
        # print i
        od_line(ml, line, nd, irsd, iryd)
    add_manually(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser/ручные лексемы/ruki.txt', nd)
    add_manually(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser/ручные лексемы/add_torot_lexemes.txt', nd)
    # add_manually(u'./ручные лексемы/местоимения  torot.txt', nd)
    add_manually(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser/ручные лексемы/местоимения нормальные.txt', nd)

def open_old_dict():
    mlf = codecs.open(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser\missedletters.json', u'r', u'utf-8')
    ml = json.load(mlf)
    nazv = u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser\All_dict_polyakov.txt'
    od = codecs.open(nazv, "r", "utf-8")
    nd = codecs.open(u'dictionary_1903_norm_pos.txt', u'w', u'utf-8')
    return ml, od, nd

def irrstemsopen():
    irs = codecs.open(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser\ручные основы\irrstems_checked.txt', u'r', u'utf-8')
    irsd = {}
    for lin in irs:
        lin = lin.rstrip()
        lin = lin.split(u'	')
        irsd[lin[0]] = lin[1:]
    iry = codecs.open(u'C:\Tanya\НИУ ВШЭ\двевн курсач\приведение словаря\poliakov-to-uniparser\ручные основы\yati_checked.txt', u'r', u'utf-8')
    iryd = {}
    for lin in iry:
        lin = lin.rstrip()
        lin = lin.split(u'	')
        iryd[lin[0]] = lin[1:]
    return irsd, iryd

def openfiles():
    ml, od, nd = open_old_dict()
    irsd, iryd = irrstemsopen()
    return ml, od, nd, irsd, iryd

def hugefunction(paradigma, lexema, gramm, iryd, irsd):
    test = 0
    try:
        if paradigma[0] == u'V':
            try:
                stem = irrstems(lexema, paradigma, iryd, irsd)
            except:
                testq = 1
                stem, paradigma = verbstem(lexema, paradigma, testq, test)
        elif paradigma[0] == u'N' or paradigma[0] == u'A' or paradigma == u'Pro':
            stem0 = osnnoun(lexema, paradigma)
            stem = nounstem(paradigma, stem0)
        else:
            print u'smth_dif', paradigma, lexema
            stem = lexema
        if stem == u'No_paradigm':
            pass
        elif gramm[0] == u'V' or gramm[0] == u'A' or gramm[0] == u'N':
            stem = problem(stem, gramm)
            stem = clearredcf(stem)
            # print stem
            try:
                if stem[-1] != u'.':
                    stem += u'.'
            except:
                #print stem, u'the bad one'
                pass
    except:
        #print u'range_error', paradigma, lexema
        stem = u'wrong' #был / в начале строки
    return stem

def sevpar(paradigm, bealexeme, lexeme, gramm, trans, nd, test, iryd, irsd):
            paradigms = paradigm.split(u'/')
            for paradigma in paradigms:
                stem = hugefunction(paradigma, lexeme, gramm, iryd, irsd)
                if test == 1:
                    pass
                    # print u'in sevpar: ', lexeme, paradigma, gramm, stem
                if u'w' in stem:
                    continue
                try:
                    if stem[-1] != u'.':
                            stem = stem + u'.'
                except:
                    # print u'no stem!!!', bealexeme, lexeme, gramm, paradigma
                    continue
                # print u'sevpar has stems', stem
                stem = clearinfo(stem)
                # print u'arter clearing', stem
                stem = clearredcf(stem)
                # print u'and then', stem
                # gramm = transform_pos_for_torot(bealexeme, gramm, paradigm)
                wordinf = u'-lexeme\r\n lex: ' + bealexeme + u'\r\n stem: ' + stem + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigma + u'\r\n transl_ru: ' + trans + u'\r\n'
                wordinf = clearinfo(wordinf)
                if u'w' in wordinf:
                    continue
                wordinf = wordinf.replace(u'*', u'_STAR_')
                nd.write(wordinf)

def getWordinf(chast, bealexeme, stem, gramm, paradigm, transl_ru, nd):
    # print u'getwordinf has stems', stem
    stem = clearredcf(stem)
    # print u'and then', stem
    # gramm = transform_pos_for_torot(bealexeme, gramm, paradigm)
    wordinf = u'-lexeme\r\n lex: ' + bealexeme + u'\r\n stem: ' + stem + u'\r\n gramm: ' + gramm + u'\r\n paradigm: ' + paradigm + u'\r\n transl_ru: ' + transl_ru + u'\r\n'
    wordinf = clearinfo(wordinf)
    if chast != u'normal_word':
        wordinf = wordinf.replace(u'.', u'.' + chast)
    wordinf = wordinf.replace(u'*', u'_STAR_')
    nd.write(wordinf)
    return wordinf

def od_line(ml, line, nd, irsd, iryd):
    test = 0
    transl_ru = u''
    chast = u'normal_word'
    info = re.search(u'<p>(.+)</a>  <i>(.+)</i>  (.+?)</a> (?:<em>(.+)</em>)?.*</p>', line)
    try:
        lexeme = info.group(1)
    except:
        print u'search_error ', line
        return u'bad line'  # Ну практически как continue написать
    gramm = info.group(2)
    lexeme, chast = pluscases(lexeme, chast, gramm)
    lexeme = reflex(lexeme)
    paradigm, transl_ru = getParadigm_correctTranslation(info, transl_ru)
    lexeme, bealexeme = dealWithLetters(lexeme, ml)
    if lexeme == u'подъ':
        print bealexeme
        paradigm, stem = getAllParadigm_getStem(gramm, paradigm, lexeme, test, iryd, irsd, truetest=1)
    if lexeme == u'от':
        print bealexeme
        paradigm, stem = getAllParadigm_getStem(gramm, paradigm, lexeme, test, iryd, irsd, truetest=1)
    paradigm, stem = getAllParadigm_getStem(gramm, paradigm, lexeme, test, iryd, irsd)
    if test == 1:
        pass
        # print bealexeme, paradigm, stem, u'test_1'
    paradigm, stem, bealexeme = cyrillicerror(paradigm, bealexeme, stem, gramm)
    if test == 1:
        pass
        # print bealexeme, paradigm, stem, u'test_2'
    stem = foundstem(stem, gramm)
    if lexeme == u'ничтоже':
        pass
        # print u'3', lexeme, paradigm, stem
    transl_ru = delTrans(gramm, transl_ru)
    if chast == u'normal_word' and u'.':
        try:
            if u'.' not in stem:
                stem = stem + u'.'
        except:
            stem = u'.'
    if paradigm == u'':
        if test == 1:
            print lexeme, paradigm, gramm, stem, u'zero paradigm'
        paradigm, stem = getAllParadigm_getStem(gramm, paradigm, lexeme, test, iryd, irsd)
        if test == 1:
            print lexeme, paradigm, gramm, stem, u'zero paradigm_2'
    if u'/' in paradigm:
        if test == 1:
            print lexeme, paradigm, gramm, stem
        wordinf = sevpar(paradigm, bealexeme, lexeme, gramm, transl_ru, nd, test, iryd, irsd)
    else:
        if test == 1:
            print lexeme, paradigm, gramm, stem
        wordinf = getWordinf(chast, bealexeme, stem, gramm, paradigm, transl_ru, nd)

def torotnb(a):
    lexemes = a.split(u'-lexeme')
    for lex in range(len(lexemes)):
        if u'persn' in lexemes[lex]:
            lexemes[lex] = lexemes[lex].replace(u'N,', u'Ne,')
        else:
            lexemes[lex] = lexemes[lex].replace(u'N,', u'Nb,')
    a = u'-lexeme' + u'-lexeme'.join(lexemes)
    return a

def add_manually(filename, nd, torot = 0):
    f = codecs.open(filename, u'r', u'utf-8')
    a = f.read()
    if torot == 1:
        a = torotnb(a)
    nd.write(a)
    return

# лечение косяков

def transform_pos_for_torot(lexeme, pos, paradigm):
    if paradigm == u'uk-ja-f' or paradigm == u'uk-e-n' or paradigm == u'uk-i-m':
        pos = u'N-PRO-i'
        # print lexeme
    if paradigm == u'uk-ta-f' or paradigm == u'uk-to-n' or paradigm == u'uk-t-m':
        pos = u'N-PRO-to'
        # print lexeme
    if paradigm == u'me' or paradigm == u'you' or paradigm == u'we' or paradigm == u'vy':
        pos = u'N-PRO-pers'
    if paradigm == u'self':
        pos = u'Pk'
        # print lexeme
    if paradigm == u'what' or paradigm == u'who':
        pos = u'N-PRO-wh'
        # print lexeme
    if lexeme == u'мо́й' or lexeme == u'тво́й' or lexeme == u'на́шъ' or lexeme == u'ва́шъ':
        pos = u'Ps'
        # print lexeme
    if lexeme == u'сво́й':
        pos = u'Pt'
        # rint lexeme
    if pos[0] == u'N':
        if u'persn' in pos:
            pos = pos.replace(u'N,', u'Ne,')
            pos = pos.replace(u',persn', u'')
        else:
            pos = pos.replace(u'N,', u'Nb,')
    return pos

def pluscases(lexeme, chast, gramm):
    if u'+' in lexeme:
        if lexeme[0] + lexeme[1] == u'не':
            lexeme = lexeme[3:]
        else:
            try:
                lexeme, chast = toska(lexeme, gramm)
                # print u'тоска', lexeme
            except:
                lexeme = toska(lexeme, gramm)
    return lexeme, chast

def reflex(lexeme):
    if lexeme[-2:] == u'ся':
        lexeme = lexeme[:-2]
    return lexeme

def getParadigm_correctTranslation(info, transl_ru):
    try:
        paradigm = info.group(3)
        if u'<em>' in paradigm:
            hi = re.search(u'<em>(.+)</em>', paradigm)
            transl_ru = hi.group()
            paradigm = u'нет парадигмы'
    except:
        paradigm = u'нет парадигмы'
    if transl_ru == u'':
        transl_ru = info.group(4)
    if transl_ru == None:
        transl_ru = u''
    return paradigm, transl_ru

def dealWithLetters(lexeme, ml):
    if lexeme in ml:
        #print u'tr'
        bealexeme = ml[lexeme][0]
        lexeme = letterchange(bealexeme)
    else:
        #print u'what can I see?', lexeme
        bealexeme = lexeme
        lexeme = letterchange(bealexeme)
    return lexeme, bealexeme

def delTrans(gramm, transl_ru):
    if u'pers' in gramm:
        # print transl_ru
        transl_ru = u''
    return transl_ru

def cyrillicerror(paradigm, bealexeme, stem, gramm):
        cyrillic = u'йцукенгшщзхъфывапролджэячсмитьбюѣ'
        for let in cyrillic:
            if let in paradigm:
                # print u'h'
                oldparadigm = paradigm
                paradigm = u''
                if bealexeme == u'':
                    bealexeme = oldparadigm
                if stem == u'':
                    stem = oldparadigm
        if paradigm == u'':
            paradigm = noparad(gramm, bealexeme)
            if paradigm == u'Pro':
                # print u'A-Pro', bealexeme, stem
                lexeme = letterchange(bealexeme)
                stem = pro_stem(lexeme, paradigm)
        return paradigm, stem, bealexeme

def redundantstems(stems):  # Эта штука точно не удалит кучу того, что должна удалять, но для какой-то части случаев сработает, а я хочу спать
    # print u'redundant', stems
    if u'|' not in stems:
        stems = stems.split(u'//')
        stems = set(stems)
        stems = u'//'.join(list(stems))
    if u'/' not in stems:
        stems = stems.split(u'|')
        stems = set(stems)
        stems = u'|'.join(list(stems))
    # print u'redundant no', stems
    stems = no_punctum_in_stem(stems)
    return stems

def no_punctum_in_stem(stems):
    if u'.' not in stems:
        stems = stems + u'.'
    return stems


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
        wordinf = wordinf.replace(u'//.', u'//')
        wordinf = wordinf.replace(u'//.|\r\n', u'\r\n')
        wordinf = wordinf.replace(u'//|', u'|')
        wordinf = wordinf.replace(u'|\r\n', u'\r\n')
        wordinf = re.sub(u'//+', u'//', wordinf)
        wordinf = re.sub(u'\.+', u'.', wordinf)
        wordinf = wordinf.replace(u'//\r\n', u'\r\n')
        wordinf = wordinf.replace(u'.|.|', u'.|')
        wordinf = re.sub(u'<.+?>', u'', wordinf)
        wordinf = wordinf.replace(u'|.\r\n', u'\r\n')
        wordinf = wordinf.replace(u'.//|', u'.|')
        wordinf = wordinf.replace(u' .//', u' ')
        wordinf = wordinf.replace(u'|.//', u'|')
        wordinf = wordinf.replace(u' /', u' ')
        # print wordinf
        return wordinf

# creating_new_dict()
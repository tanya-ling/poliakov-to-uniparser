#-*- coding: utf-8 -*-
import re
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
        word1 = u''
        for el in word:
            word1 += el
        stems.append(word1)
    return stems

def palatal_k(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант глухих и звонких
    vowels = u'уеыаоэяиюъьѣ'
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            word2 = word[:-1] + u'ч'
            stems.append(word1)
            stems.append(word2)
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
    return stems

def palatal_k_g_h(orig):
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
        elif word[-1] == u'к':
            word1 = word[:-1] + u'ц'
            word2 = word[:-1] + u'ч'
            stems.append(word1)
            stems.append(word2)
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
def change_k(orig):
    #меняем последний согласный основы. не рассатриваем кластеры (надо?) вариант звонких
    stems = []
    for word in orig:
        if word[-1] == u'к':
            word1 = word[:-1] + u'ц'
        stems.append(word1)
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
    #word = list(word)
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
        #с одним кластером
            #elif word[-3] in consonants:
             #   word1 = word[:-2]+u'е'+word[-2]+word[-1]
              #  word2 = word[:-1]+u'е'+word[-1]
               # stems.append(word1)
                #stems.append(word2)
    return stems

def narashenie (orig):
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
        stems.append(word1)
    return stems

def nounstem(paradigm, osnova):
    #paradigm = raw_input(u'Введите тип парадигмы: ').decode(u'utf-8')
    #osnova = raw_input(u'Введите основу: ').decode(u'utf-8')
    stem = []
    stem.append(osnova)
    #stem1=[]
    stem2=[]
    if paradigm == u'N1t*' or paradigm == u'N1j*':
        stem1 = beglyi(stem)
    if paradigm == u'N1g':
        stem1 = palatal_g_h(stem)
    if paradigm == u'N1k':
        stem1 = palatal_k(stem)
    if paradigm == u'N1k*':
        stem1 = beglyi(stem)
        stem2 = palatal_k(stem1)
    if paradigm == u'N1c*':
        stem1 = beglyi(stem)
        stem2 = change_c(stem1)
        #;***
    if paradigm == u'N2t*':
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
    if paradigm == u'N2k':
        #все 2
        stem1 = palatal_k_g_h(stem)
    if paradigm == u'N2c*':
        #все 2
        stem1 = vstavnoi_e(stem)
    if paradigm == u'N3t*':
        #все 2
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)
    if paradigm == u'N3j*':
        #все 2
        stem1 = vstavnoi_e(stem)
    if paradigm == u'N3k':
        #все 2
        stem1 = palatal_k_g_h(stem)
    if paradigm == u'N3k*':
        #все 2
        stem1 = vstavnoi_o(stem)
        stem2 = change_k(stem)
    if paradigm == u'N3c*':
        #все 2
        stem1 = vstavnoi_e(stem)
    if paradigm == u'N43*':
        #все 2
        stem1 = beglyi(stem)
    if paradigm == u'N5en':
        #все 2
        stem1 = narashenie_en(stem)
    if paradigm == u'N5et':
        #все 2
        stem1 = narashenie_at(stem)
    if paradigm == u'N5es':
        #все 2
        stem1 = narashenie_es(stem)
    if paradigm == u'N5er':
        #все 2
        stem1 = narashenie_er(stem)
    if paradigm == u'N5ov':
        #все 2
        stem1 = narashenie_ov(stem)
    if paradigm == u'N5*ov':
        stem1 = beglyi(stem)
    if paradigm == u'A1k' or paradigm == u'A1g':
        stem1 = change_k_g_h_adj(stem)
    if paradigm == u'A1t*':
        stem1 = vstavnoi_e(stem)
    if paradigm == u'A1j*':
        stem1 = vstavnoi_e(stem)
    if paradigm == u'A1k*':
        stem1 = vstavnoi_e(stem)
        stem2 = vstavnoi_o(stem)

#тестовая часть
    #if paradigm == u'':
      #  stem1 =
    #print u'stem1'
    stems1 =  u'.|'.join(stem1)
    if len(stem2)>0:
        stems2 = u'.|'.join(stem2)
        stems = osnova + u'.|' + stems1 + u'.|' + stems2
    else:
        stems = osnova + u'.|' + stems1
    return stems
paradigm = u'N1k*'
osnova = u'отрокъ'

stems = nounstem(paradigm, osnova)
print stems
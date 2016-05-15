# -*- coding: utf-8 -*-
import re
import codecs

def russpars(word):
    consonants = u'йцкнгшщзхфвпрлджчсмтб'
    word = word.replace(u'i', u'и')
    word = word.replace(u'і', u'и')
    word = word.replace(u'ѡ', u'о')
    word = word.replace(u'ꙋ', u'у')
    word = word.replace(u'ꙗ', u'я')
    word = word.replace(u'ѧ', u'я')
    word = word.replace(u'ѣ', u'е')
    word = word.replace(u'жы', u'жи')
    word = word.replace(u'чы', u'чи')
    word = word.replace(u'шы', u'ши')
    word = word.replace(u'щы', u'щи')
    word = word.replace(u'иа', u'ия')
    word = word.replace(u'уа', u'уя')
    word = word.replace(u'еа', u'ея')
    word = word.replace(u'ыа', u'ыя')
    word = word.replace(u'аа', u'ая')
    word = word.replace(u'оа', u'оя')
    word = re.sub(u'ъ([цкншщгзхфвпърлджстбй])', u'\\1', word)
    word = re.sub(u'([шщчцж])ю', u'\\1у', word)
    if word[-1] == u'ъ':
        word = word[:-1]
    return word

print russpars(u'хълѣбавъшюю')
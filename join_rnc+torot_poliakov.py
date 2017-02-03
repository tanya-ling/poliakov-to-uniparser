#-*- coding: utf-8 -*-
import re
import codecs
import json

mlf = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\paradigm_tagging\\joined_2.json', u'r', u'utf-8')
ml = json.load(mlf)

op = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\dictionary_1903_norm_pos.txt', 'r', 'utf-8')
nd = codecs.open('themain_d_for_parser.txt', 'w', 'utf-8')


def listmerge3(lstlst):
    all = []
    for lst in lstlst:
        all.extend(lst)
    return all


def the_main_thing(string_index, word, lemma, gram):
        for paradigm in word[string_index]:
            cont = False
            stems = ''
            for index in range(len(word[string_index][paradigm])):
                try:
                    stemset_real = word['par_stem'][paradigm][index]
                except KeyError:
                    stemset_real = []
                try:
                    stemset_predict = word['predicted_stems'][paradigm][index]
                except IndexError:
                    stemset_predict = []
                except KeyError:
                    stemset_predict = []
                try:
                    stemset_tor = word['tor_par_stem'][paradigm][index]
                except KeyError:
                    stemset_tor = []
                ll = [stemset_predict, stemset_real, stemset_tor]
                try:
                    alt = list(set(listmerge3(ll)))
                except TypeError:
                    alt = list(set(listmerge3([stemset_predict[0], stemset_real, stemset_tor])))
                if alt == []:
                    cont = True
                stems += './/'.join(alt) + '.|'
            if cont:
                continue
            stems = stems[:-1]
            info = u'-lexeme\r\n lex: ' + lemma + '\r\n stem: ' + stems + '\r\n gramm: ' + gram +'\r\n paradigm: ' + paradigm +'\r\n transl_ru: \r\n'
            nd.write(info)


for word in ml:
    if 'lemma_new' in word:
        lemma = word['lemma_new']
    else:
        lemma = word['tor_lemma_new']
    if 'gender' in word:
        gram = word['pos'] + u',' + word['gender']
    elif 'tor_gender' in word:
        gram = word['pos'] + u',' + word['tor_gender']
    else:
        gram = word['pos']
    if 'par_stem' in word:
        the_main_thing('par_stem', word, lemma, gram)
    elif 'tor_par_stem' in word:
        the_main_thing('tor_par_stem', word, lemma, gram)
    else:
        paradigm = 'unchangeable'
        stems = ''
        info = u'-lexeme\r\n lex: ' + lemma + '\r\n stem: ' + stems + '\r\n gramm: ' + gram + '\r\n paradigm: ' + paradigm + '\r\n transl_ru: \r\n'
        nd.write(info)


for line in op:
    line = line.replace(',inan', '')
    line = line.replace(',anim', '')
    line = line.replace(u'́', '')
    nd.write(line)
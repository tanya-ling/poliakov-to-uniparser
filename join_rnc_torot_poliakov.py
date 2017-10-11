#-*- coding: utf-8 -*-
import codecs
import json
import sys
sys.path.insert(0, u'C:\Tanya\НИУ ВШЭ\двевн курсач\parsed\\UniParser2.0_MidRus\MiddleRussian')
from tanyacommonform_2103 import commonform




def listmerge3(lstlst):
    all = []
    for lst in lstlst:
        all.extend(lst)
    return all


def clear_stems(stems):
    stems1n = []
    stems1 = stems.split('|')
    for stems11 in stems1:
        stems2 = stems11.split('//')
        stems2n = []
        for stem21 in stems2:
            # if stem21 == u'лтьск.':
            #     # print 'we are doing greak there'
            if stem21 != u'ся.':
                stem21n = commonform(stem21)
                stems2n.append(stem21n)
        stems12 = '//'.join(set(stems2n))
        stems1n.append(stems12)
    stems = '|'.join(stems1n).replace('..', '.')
    return stems


def dealwithtsa(lemma, pos):
    if pos == 'V':
        if lemma[-2:] == u'ся':
            lemma = lemma[:-2]
    return lemma


def the_main_thing(string_index, word, lemma, gram):
        lemma = dealwithtsa(lemma, gram)
        lemma = zh_lemmas(lemma, gram)
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
            # if lemma == u'летский':
            #     print 'it is ok now', stems
            stems = clear_stems(stems)
            info = u'-lexeme\r\n lex: ' + lemma + '\r\n stem: ' + stems + '\r\n gramm: ' + gram.replace('Adj', 'A') + \
                   '\r\n paradigm: ' + paradigm + '\r\n transl_ru: \r\n'
            nd.write(format_replacement(info))


def format_replacement(line):
    return line.replace('STAR_\r\n', 'STAR\r\n').replace('gramm: N', 'gramm: S').replace('tr\r\n', 'tran\r\n').\
        replace('tr,', 'tran,').replace(u'іе\r\n', u'ие\r\n').replace(u'lex: прѣ', u'lex: пре').\
        replace(u' ннѣ\r\n', u' нынѣ\r\n')


def zh_lemmas(lemma, gramm):
    if lemma[-3:] == u'ець' or lemma[-2:] == u'жь':
        if 'S,m' in gramm or 'N,m' in gramm:
            lemma = lemma[:-1] + u'ъ'
    return lemma

if __name__ == "__main__":

    mlf = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\paradigm_tagging\\joined_3.json', u'r', u'utf-8')
    ml = json.load(mlf)

    op = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\dictionary_1903_norm_pos.txt', 'r',
                     'utf-8')
    nd = codecs.open('themain_d_for_parser.txt', 'w', 'utf-8')

    lemmas = {}

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
        lemmas[commonform(lemma)] = lemma
        if 'par_stem' in word:
            the_main_thing('par_stem', word, lemma, gram)
        elif 'tor_par_stem' in word:
            the_main_thing('tor_par_stem', word, lemma, gram)
        else:
            paradigm = 'unchangeable'
            stems = commonform(lemma) + u'.'
            lemma = zh_lemmas(lemma, gram)
            info = u'-lexeme\r\n lex: ' + lemma + '\r\n stem: ' + stems + '\r\n gramm: ' + gram.replace('Adj', 'A') + \
                   '\r\n paradigm: ' + paradigm + '\r\n transl_ru: \r\n'
            nd.write(format_replacement(info))


    for line in op:
        if line[:6] == u' lex: ':
            lemma = line.rstrip()[6:]
            if commonform(lemma) in lemmas:
                line = u' lex: ' + lemmas[commonform(lemma)] + '\r\n'
        line = line.replace(',inan', '')
        line = line.replace(',anim', '')
        line = line.replace(u'́', '')
        line = line.replace('Adj', 'A,')
        # line = line.replace('Adj\r\n', 'A\r\n')
        # line = line.replace('Adj-', 'A-')
        line = format_replacement(line)
        line = line.replace(u'uk-е-n', 'uk-e-n')
        nd.write(line)
    #
    # print commonform(u'льтьск')
    # print commonform(u'лтьск')
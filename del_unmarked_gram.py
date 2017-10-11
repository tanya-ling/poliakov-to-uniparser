#-*- coding: utf-8 -*-
import codecs
from join_rnc_torot_poliakov import clear_stems


def join_stems(stems1, stems2):
    # print('I1: ', stems1, 'II2: ', stems2)
    if stems1 == stems2:
        return stems1.rstrip()[7:]
    stems1 = stems1.rstrip()[7:]
    stems2 = stems2.rstrip()[7:]
    # print('I: ', stems1, 'II: ', stems2)
    stems1 = stems1.split('|')
    stems2 = stems2.split('|')
    i = 0
    for stem in stems1:
        if stems2[i] != stem:
            stems1[i] += '//' + stems2[i]
    return '|'.join(stems1)

od = codecs.open('themain_d_for_parser.txt', 'r', 'utf-8')
# nd = codecs.open('themain_d_for_parser2.txt', 'w', 'utf-8')

lexemes = od.read().split('-lexeme\r\n')[1:]
i = 0
ind_to_del = []
for lexeme in lexemes:
    content = lexeme.split('\r\n')
    gramm = content[2]
    lemma = content[0]
    # print('__________lemma1', lemma, i)
    paradigm = content[3]
    stem = content[1]
    j = 0
    for lexeme2 in lexemes:
        if i == j:
            j += 1
            continue
        content2 = lexeme2.split('\r\n')
        gramm2 = content2[2]
        lemma2 = content2[0]
        # print('_____lemma2', lemma2, j)
        paradigm2 = content2[3]
        stem2 = content2[1]
        if lemma == lemma2 and paradigm == paradigm2:  # не приведет ли то, что я ограничиваюсь таким сравнением к
            # удалению штук неизмениямых частей речи, у которых совпадает форма, но не часть речи?
            # Союз и наречие, например.
            stems = join_stems(stem, stem2)
            stems = clear_stems(stems)
            # print(stems, 'stems')
            if len(gramm) < len(gramm2):
                ind_to_del.append(i)
                content2[1] = ' stem: ' + stems
                lexemes[j] = '\r\n'.join(content2)
            elif len(gramm) > len(gramm2):
                ind_to_del.append(j)
                content[1] = ' stem: ' + stems
                lexemes[i] = '\r\n'.join(content)
        j += 1
    i += 1
    try:
        if str(i)[-3:] == '000':
            print(i)
    except IndexError:
        pass

# print(ind_to_del)

toRemove = set(ind_to_del)
lexemes_new = [x.replace('PREP', 'PR').replace('SUM', 'NUM') for i, x in enumerate(lexemes) if i not in toRemove]
# for i in ind_to_del:
#     # print(i)
#     try:
#         lexemes.remove(i)
#     except ValueError:
#         print('Value error')
#         print(i)
nd.write('-lexeme\r\n' + '-lexeme\r\n'.join(lexemes_new))
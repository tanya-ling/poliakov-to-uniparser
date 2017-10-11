import codecs


def prepare_lemmas():
    sl = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\suppletiveLemmas.txt', 'r',
                     'utf-8')
    sla = {}
    for line in sl:
        line = line.rstrip().split('\t')
        sla[line[0]] = line[1]
    sl.close()
    return sla


def writing(lemma, forms, analysis):
    string = '-lexeme\r\n lex: ' + lemma + '\r\n stem: ' + forms + '\r\n gramm: ' + analysis + \
             '\r\n paradigm: unchangeable\r\n transl_ru: \r\n'
    fc.write(string)




def create_suppl(fvr):
    i = 0
    for line in fvr:
        line = line.rstrip().replace('<0>.', '')
        if 'paradigm' in line:
            lemmakey = line[11:]
            print(lemmakey)
            lemma = sla[lemmakey]
        else:
            if 'flex' in line:
                forms = line[8:].replace('//', './/') + '.'
                analysis = fvr[i + 1].rstrip()[9:]
                if lemmakey == 'быти':
                    analysis = 'V,' + analysis
                else:
                    analysis = 'SPRO,' + analysis
                writing(lemma, forms, analysis)
        i += 1

sla = prepare_lemmas()

fv = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\byti.txt', 'r',
                 'utf-8')
fp = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\all_pron_n.txt', 'r', 'utf-8')

fvr = fv.readlines()
fpr = fp.readlines()
fc = codecs.open('C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\ручные лексемы\\suppletive_lexemes.txt',
                 'w', 'utf-8')

create_suppl(fvr)
create_suppl(fpr)
#-*- coding: utf-8 -*-
import codecs

od = codecs.open('themain_d_for_parser2.txt', 'r', 'utf-8')
nd = codecs.open('themain_d_for_parser3.txt', 'w', 'utf-8')

fc = codecs.open('C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\ручные лексемы\\suppletive_lexemes.txt',
                 'r', 'utf-8')

nt = od.read() + fc.read()

nd.write(nt)

nd.close()
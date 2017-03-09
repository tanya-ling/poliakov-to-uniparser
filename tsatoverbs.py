#-*- coding: utf-8 -*-
import re
import codecs
import sys

f = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\paradigm_tagging\\глагфлексии.txt', 'r', 'utf-8')

f2 = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\глагдляпарсера.txt', 'w', 'utf-8')

for line in f:
    if line[:8] == u' -flex: ':
        line = line.rstrip()
        infl = []
        inflexions = line[8:].split('//')
        for inflexion in inflexions:
            inflexion =  re.sub(u'([йцкнгшщзхфвпрлджчсмтб])(ь|ъ)([йцкнгшщзхфвпрлджчсмтб])', u'\\1\\3', inflexion)
            inflexion = inflexion.replace(u'йъ', u'й')
            infl.append(inflexion)
            new = inflexion + u'ся'
            new2 = inflexion + u'сь'
            new = re.sub(u'([йцкнгшщзхфвпрлджчсмтб])(ь|ъ)([йцкнгшщзхфвпрлджчсмтб])', u'\\1\\3', new)
            new2 = re.sub(u'([йцкнгшщзхфвпрлджчсмтб])(ь|ъ)([йцкнгшщзхфвпрлджчсмтб])', u'\\1\\3', new2)
            infl.append(re.sub(u'т[ьъ]?ся', u'ца', new))
            infl.append(re.sub(u'т[ьъ]?ся', u'ца', new2))
        inflexions = '//'.join(set(infl))
        f2.write(u' -flex: ' + inflexions + '\r\n')
    else:
        f2.write(line)

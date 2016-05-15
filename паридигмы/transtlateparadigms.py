#-*- coding: utf-8 -*-
import re
import codecs

r = re.compile(u'([йцкнгшщзхфвпрлджчсмтб])ъ', flags=re.U)
r2 = re.compile(u'([йцкнгшщзхфвпрлджчсмтб])([йцкнгшщзхфвпрлджчсмтб])', flags=re.U)
r3 = re.compile(u'(<.>\.)тс(.)', flags=re.U)
r4 = re.compile(u'(<.>\.)тьс(.)', flags=re.U)

def flexline(line):
    q1 =0
    line = line.rstrip()
    # print u'flexline'
    line = line[8:]
   # print line, u'line -8:'
    linesplit = line.split(u'//')
    if line == u'<1>.ъ//<0>.ы':
        q1 = 1
    gramemy = []
    for gramema in linesplit:
        # print gramema, u'gramema'
        # print gramemy, u'gramemy'
        gramemy.append(gramema)
        if q1 == 1:
            print gramema
        gramemy = flexgram(gramema, gramemy)
        if q1 == 1:
            for gr in gramemy:
                print gr
    gramemy = set(gramemy)
    if q1 == 1:
        for q2 in gramemy:
            print q2
    gramemy = u'//'.join(gramemy)
    line = u' -flex: ' + gramemy + u'\r\n'
    return line

def yat_add(gramema, gramemy):
    if u'ѣ' in gramema:
        gramema2 = gramema.replace(u'ѣ', u'е')
        gramemy.append(gramema2)
    return gramemy

def flexgram(gramema, gramemy):
    # gramemy = letters(gramema, gramemy)
    gramemy = er_del(gramema, gramemy)
    gramemyo = gramemy[:]
    for gramema in gramemyo:
        if r3.search(gramema) or r4.search(gramema):
            s3 = r3.search(gramema)
            if s3 == None:
                s3 = r4.search(gramema)
            fl = s3.group(1) + u'ц' + s3.group(2)
            gramemy.append(fl)
            fl = s3.group(1) + u'тьс' + s3.group(2)
            gramemy.append(fl)
            fl = s3.group(1) + u'тц' + s3.group(2)
            gramemy.append(fl)
            fl = s3.group(1) + u'тс' + s3.group(2)
            gramemy.append(fl)
    gramemyo3 = gramemy[:]
    for gramema in gramemyo3:
        gramemy = er_add(gramema, gramemy)
    # print gramemy, u'flexgram gramemy'
    gramemyo2 = gramemy[:]
    for gramema in gramemyo2:
        gramemy = yat_add(gramema, gramemy)
    if u'.ъ' in gramemy:
        gramemy.append(u'.')
    if u'<1>.ъ' in gramemy:
        gramemy.append(u'<1>.')
    if u'<2>.ъ' in gramemy:
        gramemy.append(u'<2>.')
    if u'<3>.ъ' in gramemy:
        gramemy.append(u'<3>.')
    if u'<4>.ъ' in gramemy:
        gramemy.append(u'<4>.')
    return gramemy

def er_del(gramema, gramemy):
    if r.search(gramema):
        gramema2 = r.sub(u'\\1', gramema)
        gramemy.append(gramema2)
        # gramemy = letters(gramema2, gramemy)
    return gramemy

def er_add(gramema, gramemy):
    if r2.search(gramema):
        gramema2 = r2.sub(u'\\1ъ\\2', gramema)
        gramemy.append(gramema2)
        if r2.search(gramema2):
            # print gramema2
            gramemy = er_add(gramema2, gramemy)
        # gramemy = letters(gramema2, gramemy)
    return gramemy

def flexgrameasier(gramema, gramemy):
    # gramemy = letters(gramema, gramemy)
    gramemy = er_del(gramema, gramemy)
    gramemyo = gramemy[:]
    gramemyo3 = gramemy[:]
    for gramema in gramemyo3:
        gramemy = er_add(gramema, gramemy)
    # print gramemy, u'flexgram gramemy'
    gramemyo2 = gramemy[:]
    for gramema in gramemyo2:
        gramemy = yat_add(gramema, gramemy)
    if u'.ъ' in gramemy:
        gramemy.append(u'.')
    if u'<1>.ъ' in gramemy:
        gramemy.append(u'<1>.')
    if u'<2>.ъ' in gramemy:
        gramemy.append(u'<2>.')
    if u'<3>.ъ' in gramemy:
        gramemy.append(u'<3>.')
    if u'<4>.ъ' in gramemy:
        gramemy.append(u'<4>.')
    return gramemy

nazv = u'VARIANT_PARADIGMS_23.txt'

op = codecs.open(nazv, "r", "utf-8")
np = codecs.open(u'VARIANT_PARADIGMS_1012.txt', u'w', u'utf-8')

j = 0

np.write(u'0_start\r\n')
for line in op:
    j += 1
    print u'line №', j
    try:
        if line[:8] == u' -flex: ':
            line = flexline(line)
            line = line.replace(u'.<', u'<')
        np.write(line)
    except:
        if line[:8] == u' -flex: ':
            line = flexlineeasier(line)
            line = line.replace(u'.<', u'<')
        np.write(line)

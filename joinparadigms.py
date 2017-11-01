import codecs


def combain_paradigms():
    fn = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\paradigm_tagging\\сущфлексии.txt', 'r', 'utf-8')
    fa = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\paradigm_tagging\\прилфлексии011117.txt', 'r', 'utf-8')
    fv = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\глагдляпарсера.txt', 'r', 'utf-8')
    fp = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\all_pron_n.txt', 'r', 'utf-8')
    fb = codecs.open(u'C:\\Users\\Tatiana\\Documents\\GitHub\\poliakov-to-uniparser\\флексии\\byti.txt', 'r', 'utf-8')
    fnr = fn.read()
    far = fa.read()
    fvr = fv.read()
    fpr = fp.read()
    fbr = fb.read()
    fcr = fnr + far + fvr + fpr + fbr + '\r\n-paradigm: unchangeable\r\n -flex: .\r\n  gramm: \r\n'
    fc = codecs.open('conjoined_paradigms.txt', 'w', 'utf-8')
    fc.write(fcr.replace('﻿', ''))
    fc.close()

combain_paradigms()
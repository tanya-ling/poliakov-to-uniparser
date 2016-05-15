#-*- coding: utf-8 -*-
import re
import codecs

def moreproblemsadj(word):
    words = []
    if word[-2:] == u'ск':
        print word
        word1 = word[:-2] + u'т'
        words.append(word1)
    words = u'.//'.join(words)
    return words

def moreproblemsnou(word):
    words = []
    if u'жд' in word:
        print word
        word1 = word.replace(u'жд', u'ж')
        words.append(word1)
    words = u'.//'.join(words)
    return words

def moreproblems1(word):
    words = []
    if word[-5:] == u'еческ':
        print word, u'еческ'
        word1 = word.replace(u'еческ', u'ецк')
        words.append(word1)
        word2 = word.replace(u'еческ', u'етск')
        words.append(word2)
    words = u'.//'.join(words)
    return words

def moreproblems2(word):
    words = []
    if re.search(u'[уеыаоэяиюѣ]г[уеыаоэяиюѣ]', word):
        print word
        word1 = re.sub(u'([уеыаоэяиюѣ])г([уеыаоэяиюѣ])', u'\\1\\2', word)
        words.append(word1)
        words = u'.//'.join(words)
    return words

def moreproblems(word):
    words = []
    print word
    word1 = moreproblems1(word)
    words.append(word1)
    word2 = moreproblems2(word1)
    words.append(word2)
    words = u'.//'.join(words)
    return words

def problem(stems, gramm): # на самом деле так не все косвенные основы порождаются, потому что нужно же порождать варианты от порожденных, и уже слишком сложно, АААААААААА
    if u'|' in stems:
        print u'| in stems'
        stems1 = stems.split(u'|')
        stems1a = []
        for stems1e in stems1:
            if u'//' in stems1e:
                stems2 = stems1e.split(u'//')
                stems2a = []
                for stems2e in stems2:
                    stems2a.append(stems2e)
                    stems2en = moreproblems(stems2e)
                    stems2a.append(stems2en)
                    if gramm[0] == u'N':
                        stems2en = moreproblemsnou(stems2e)
                        stems2a.append(stems2en)
                    elif gramm == u'A':
                        stems2en = moreproblemsadj(stems2e)
                        stems2a.append(stems2en)
                stems2 = u'//'.join(stems2a)
                stem1a.append(stems2)
            else:
                stems1a.append(stems1e)
                stems1en = moreproblems(stems1e)
                stems1a.append(stems1en)
                if gramm[0] == u'N':
                    stems1en = moreproblemsnou(stems1e)
                    stems1a.append(stems1en)
                elif gramm == u'A':
                    stems1en = moreproblemsadj(stems1e)
                    stems1a.append(stems1en)
        stems1 = u'.|'.join(stems1a)
    else:
        print u'no | in stems'
        if u'//' in stems:
            print u'// in stems'
            stems1 = stems.split(u'//')
            stems1a = []
            for stems1e in stems1:
                stems1a.append(stems1e)
                stems1en = moreproblems(stems1e)
                stems1a.append(stems1en)
                if gramm[0] == u'N':
                    stems1en = moreproblemsnou(stems1e)
                    stems1a.append(stems1en)
                elif gramm == u'A':
                    stems1en = moreproblemsadj(stems1e)
                    stems1a.append(stems1en)
            stems1 = u'//'.join(stems1a)
        else:
            print u'no // in stems'
            stemsa = []
            stemsa.append(stems)
            stemsen = moreproblems(stems)
            stemsa.append(stemsen)
            if gramm[0] == u'N':
                stemsen = moreproblemsnou(stems)
                stemsa.append(stemsen)
            elif gramm == u'A' or gramm == u'A,poss':
                stemsen = moreproblemsadj(stems)
                stemsa.append(stemsen)
            stems1 = u'//'.join(stemsa)
    return stems1

print problem(u'котик', u'N')
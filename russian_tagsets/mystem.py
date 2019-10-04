# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters
from russian_tagsets.utils import invert_mapping
import re

MYSTEM_TO_OPENCORPORA= {'неод': 'inan',
 'од': 'anim',
 'несов': 'impf',
 'сов': 'perf',
 'вин': 'accs',
 'дат': 'datv',
 'зват': 'voct',
 'им': 'nomn',
 'местн': 'loc2',
 'парт': 'gen2',
 'пр': 'loct',
 'род': 'gent',
 'твор': 'ablt',
 'жен': 'femn',
 'муж': 'masc',
 'сред': 'neut',
 'изъяв': 'indc',
 'пов': 'imper',
 'ед': 'sing',
 'мн': 'plur',
 '1-л': '1per',
 '2-л': '2per',
 '3-л': '3per',
 'A': 'ADJF',
 'ADV': 'ADVB',
 'ADVPRO': 'ADVB',
 'ANUM': 'NUMR',
 'APRO': 'ADJF',
 'COM': 'COMP',
 'CONJ': 'CONJ',
 'INTJ': 'INTJ',
 'NUM': 'NUMR',
 'PART': 'PRCL',
 'PR': 'PREP',
 'S': 'NOUN',
 'SPRO': 'NPRO',
 'V': 'VERB',
 'глагол': 'V',
 'междометие': 'INTJ',
 'местоимение-прилагательное': 'APRO',
 'местоимение-существительное': 'SPRO',
 'местоименное наречие': 'ADVPRO',
 'наречие': 'ADV',
 'предлог': 'PR',
 'прилагательное': 'A',
 'союз': 'CONJ',
 'существительное': 'S',
 'частица': 'PART',
 'часть композита - сложного слова': 'COM',
 'числительное': 'NUM',
 'числительное-прилагательное': 'ANUM',
 'наст': 'pres',
 'непрош': 'futr',
 'прош': 'past',
 'нп': 'intr',
 'пе': 'tran',
 'действ': 'actv',
 'страд': 'pssv'}

OPENCORPORA_TO_MYSTEM = invert_mapping(MYSTEM_TO_OPENCORPORA)

def mystem_to_opencorpora(mystem_tag, word=None):
    open_tags=[]
    
    for tag in mystem_tag.split('='):
        r=re.findall('\((.*)\)',tag)
        tag = r[0].split('|')[0] if len(r) > 0 else tag
        for grammeme in tag.split(','):
            if grammeme in MYSTEM_TO_OPENCORPORA:
                open_tags.append(MYSTEM_TO_OPENCORPORA[grammeme])
    return ','.join(open_tags)

def opencorpora_to_mystem(open_tag, word=None):
    mystem_tags=[]
    
    for tag in open_tag.split(','):
        if tag in OPENCORPORA_TO_MYSTEM:
            mystem_tags.append(OPENCORPORA_TO_MYSTEM[tag])
    return ','.join(mystem_tags)


converters.add('mystem', 'opencorpora-int', mystem_to_opencorpora)
converters.add('opencorpora-int','mystem', opencorpora_to_mystem)
# -*- coding: utf-8 -*-
"""
Conversion between OpenCorpora.org (http://opencorpora.org/dict.php?act=gram)
tagset and other tagsets.
"""
from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters, positional, aot
from russian_tagsets.utils import invert_mapping

GRAM_TABLE = [ # num, internal tag, external tag, description, parent
    ['1', 'POST', 'ЧР', 'часть речи', '—'],
    ['2', 'NOUN', 'СУЩ', 'имя существительное', 'POST'],
    ['3', 'ADJF', 'ПРИЛ', 'имя прилагательное (полное)', 'POST'],
    ['4', 'ADJS', 'КР_ПРИЛ', 'имя прилагательное (краткое)', 'POST'],
    ['5', 'COMP', 'КОМП', 'компаратив', 'POST'],
    ['6', 'VERB', 'ГЛ', 'глагол (личная форма)', 'POST'],
    ['7', 'INFN', 'ИНФ', 'глагол (инфинитив)', 'POST'],
    ['8', 'PRTF', 'ПРИЧ', 'причастие (полное)', 'POST'],
    ['10', 'PRTS', 'КР_ПРИЧ', 'причастие (краткое)', 'POST'],
    ['11', 'GRND', 'ДЕЕПР', 'деепричастие', 'POST'],
    ['12', 'NUMR', 'ЧИСЛ', 'числительное', 'POST'],
    ['13', 'ADVB', 'Н', 'наречие', 'POST'],
    ['14', 'NPRO', 'МС', 'местоимение-существительное', 'POST'],
    ['15', 'PRED', 'ПРЕДК', 'предикатив', 'POST'],
    ['16', 'PREP', 'ПР', 'предлог', 'POST'],
    ['17', 'CONJ', 'СОЮЗ', 'союз', 'POST'],
    ['18', 'PRCL', 'ЧАСТ', 'частица', 'POST'],
    ['19', 'INTJ', 'МЕЖД', 'междометие', 'POST'],

    ['21', 'ANim', 'Од-неод', 'одушевлённость / одушевлённость не выражена', '—'],
    ['22', 'anim', 'од', 'одушевлённое', 'ANim'],
    ['23', 'inan', 'неод', 'неодушевлённое', 'ANim'],

    ['24', 'GNdr', 'хр', 'род / род не выражен', '—'],
    ['25', 'masc', 'мр', 'мужской род', 'GNdr'],
    ['26', 'femn', 'жр', 'женский род', 'GNdr'],
    ['27', 'neut', 'ср', 'средний род', 'GNdr'],
    ['28', 'Ms-f', 'ор', 'общий род', '—'],

    ['29', 'NMbr', 'Число', 'число', '—'],
    ['30', 'sing', 'ед', 'единственное число', 'NMbr'],
    ['31', 'plur', 'мн', 'множественное число', 'NMbr'],
    ['32', 'Sgtm', 'sg', 'singularia tantum', '—'],
    ['33', 'Pltm', 'pl', 'pluralia tantum', '—'],
    ['36', 'Fixd', '0', 'неизменяемое', '—'],

    ['37', 'CAse', 'Падеж', 'категория падежа', '—'],
    ['38', 'nomn', 'им', 'именительный падеж', 'CAse'],
    ['39', 'gent', 'рд', 'родительный падеж', 'CAse'],
    ['40', 'datv', 'дт', 'дательный падеж', 'CAse'],
    ['41', 'accs', 'вн', 'винительный падеж', 'CAse'],
    ['42', 'ablt', 'тв', 'творительный падеж', 'CAse'],
    ['43', 'loct', 'пр', 'предложный падеж', 'CAse'],
    ['44', 'voct', 'зв', 'звательный падеж', 'nomn'],
    ['45', 'gen1', 'рд1', 'первый родительный падеж', 'gent'],
    ['46', 'gen2', 'рд2', 'второй родительный (частичный) падеж', 'gent'],
    ['47', 'acc2', 'вн2', 'второй винительный падеж', 'accs'],
    ['48', 'loc1', 'пр1', 'первый предложный падеж', 'loct'],
    ['49', 'loc2', 'пр2', 'второй предложный (местный) падеж', 'loct'],

    ['50', 'Abbr', 'аббр', 'аббревиатура', '—'],
    ['51', 'Name', 'имя', 'имя', '—'],
    ['52', 'Surn', 'фам', 'фамилия', '—'],
    ['53', 'Patr', 'отч', 'отчество', '—'],
    ['54', 'Geox', 'гео', 'топоним', '—'],
    ['55', 'Orgn', 'орг', 'организация', '—'],
    ['56', 'Trad', 'tm', 'торговая марка', '—'],
    ['57', 'Subx', 'субст?', 'возможна субстантивация', '—'],
    ['58', 'Supr', 'превосх', 'превосходная степень', '—'],
    ['59', 'Qual', 'кач', 'качественное', '—'],
    ['60', 'Apro', 'мест-п', 'местоименное', '—'],
    ['61', 'Anum', 'числ-п', 'порядковое', '—'],
    ['62', 'Poss', 'притяж', 'притяжательное', '—'],
    ['63', 'V-ey', '*ею', 'форма на -ею', '—'],
    ['64', 'V-oy', '*ою', 'форма на -ою', '—'],
    ['65', 'Cmp2', 'сравн2', 'сравнительная степень на по-', '—'],
    ['66', 'V-ej', '*ей', 'форма компаратива на -ей', '—'],

    ['67', 'ASpc', 'Вид', 'категория вида', '—'],
    ['68', 'perf', 'сов', 'совершенный вид', 'ASpc'],
    ['69', 'impf', 'несов', 'несовершенный вид', 'ASpc'],

    ['70', 'TRns', 'Перех', 'категория переходности', '—'],
    ['71', 'tran', 'перех', 'переходный', 'TRns'],
    ['72', 'intr', 'неперех', 'непереходный', 'TRns'],

    ['73', 'Impe', 'безл', 'безличный', '—'],
    ['74', 'Uimp', 'безл-у', 'безличное употребление', '—'],
    ['75', 'Mult', 'мног', 'многократный', '—'],
    ['76', 'Refl', 'возвр', 'возвратный', '—'],

    ['77', 'PErs', 'Лицо', 'категория лица', '—'],
    ['78', '1per', '1л', '1 лицо', 'PErs'],
    ['79', '2per', '2л', '2 лицо', 'PErs'],
    ['80', '3per', '3л', '3 лицо', 'PErs'],

    ['81', 'TEns', 'Время', 'категория времени', '—'],
    ['82', 'pres', 'наст', 'настоящее время', 'TEns'],
    ['83', 'past', 'прош', 'прошедшее время', 'TEns'],
    ['84', 'futr', 'буд', 'будущее время', 'TEns'],

    ['85', 'MOod', 'Накл', 'категория наклонения', '—'],
    ['86', 'indc', 'изъяв', 'изъявительное наклонение', 'MOod'],
    ['87', 'impr', 'повел', 'повелительное наклонение', 'MOod'],

    ['88', 'INvl', 'Совм', 'категория совместности', '—'],
    ['89', 'incl', 'вкл', 'говорящий включён в действие', 'INvl'],
    ['90', 'excl', 'выкл', 'говорящий не включён в действие', 'INvl'],

    ['91', 'VOic', 'Залог', 'категория залога', '—'],
    ['92', 'actv', 'действ', 'действительный залог', 'VOic'],
    ['93', 'pssv', 'страд', 'страдательный залог', 'VOic'],

    ['94', 'Infr', 'разг', 'разговорное', '—'],
    ['95', 'Slng', 'жарг', 'жаргонное', '—'],
    ['96', 'Arch', 'арх', 'устаревшее', '—'],
    ['97', 'Litr', 'лит', 'литературный вариант', '—'],
    ['98', 'Erro', 'опеч', 'опечатка', '—'],
    ['99', 'Dist', 'искаж', 'искажение', '—'],
    ['100', 'Ques', 'вопр', 'вопросительное', '—'],
    ['101', 'Dmns', 'указ', 'указательное', '—'],
    ['103', 'Prnt', 'вводн', 'вводное слово', '—'],
    ['104', 'V-be', '*ье', 'форма на -ье', '—'],
    ['105', 'V-en', '*енен', 'форма на -енен', '—'],
    ['106', 'V-ie', '*ие', 'отчество через -ие-', '—'],
    ['107', 'V-bi', '*ьи', 'форма на -ьи', '—'],
    ['108', 'Fimp', '*несов', 'деепричастие от глагола несовершенного вида', '—'],
    ['109', 'Prdx', 'предк?', 'может выступать в роли предикатива', '—'],
    ['110', 'Coun', 'счетн', 'счётная форма', '—'],
    ['111', 'Coll', 'собир', 'собирательное числительное', '—'],
    ['112', 'V-sh', '*ши', 'деепричастие на -ши', '—'],
    ['113', 'Af-p', '*предл', 'форма после предлога', '—']
]

INTERNAL_TO_EXTERNAL = dict((item[1], item[2]) for item in GRAM_TABLE)
EXTERNAL_TO_INTERNAL = invert_mapping(INTERNAL_TO_EXTERNAL)

def external_to_internal(external_tag):
    return ",".join(EXTERNAL_TO_INTERNAL[tok].strip() for tok in external_tag.split(','))

def internal_to_external(internal_tag):
    return ",".join(INTERNAL_TO_EXTERNAL[tok].strip() for tok in internal_tag.split(','))


def to_aot(open_tag):
    pass

def from_aot(aot_tag):
    pass


#def to_positional(open_tag):
#    pass
#
#def from_positional(open_tag):
#    pass

converters.add('opencorpora-int', 'opencorpora', internal_to_external)
converters.add('opencorpora', 'opencorpora-int', external_to_internal)
converters.add('opencorpora', 'aot', to_aot)
converters.add('aot', 'opencorpora', from_aot)

import re
from random import uniform
from collections import defaultdict
#буду делать 3грамы чтобы  предложения были более осмысленные 
r_alphabet = re.compile(u'[а-яА-Я0-9-]+|[.,:;?!]+')#рассматривается только русские буквы и цифры

def gen_lines(corpus):#преобразовываем текст в строки, используем yield для уменьшения памяти
    data = open(corpus,  "r",  encoding='utf-8')
    for line in data:
        yield line.lower()

def gen_tokens(lines):#создаем из строк слова
    for line in lines:
        for token in r_alphabet.findall(line):
            yield token




        





def gen_trigrams(tokens):#
    t0, t1 = '$', '$'
    for t2 in tokens:
        yield t0, t1, t2
        if t2 in '.!?':
            yield t1, t2, '$'
            yield t2, '$','$'
            t0, t1 = '$', '$'
        else:
            t0, t1 = t1, t2

class text(object):
    def __init__(self, corpus, number):
        self.corpus = corpus
        self.number = int(number)
        
        
        
    def train(self):
        lines = gen_lines(self.corpus)
        tokens = gen_tokens(lines)
        trigrams = gen_trigrams(tokens)
    
        bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)
    
        for t0, t1, t2 in trigrams:
            bi[t0, t1] += 1
            tri[t0, t1, t2] += 1
        model = {}
        for (t0, t1, t2), freq in iter(tri.items()):
            if (t0, t1) in model:
                model[t0, t1].append((t2, freq/bi[t0, t1]))
            else:
                model[t0, t1] = [(t2, freq/bi[t0, t1])]
        return model

    def generate_sentence(self):
        phrase = ''
        t0, t1 = '$', '$'
        while 1:
            t0, t1 = t1, unirand(text.train(self)[t0, t1])
            if t1 == '$': break
            if t1 in ('.!?,;:') or t0 == '$':
                phrase += t1
            else:
                phrase += ' ' + t1
        
        return phrase.capitalize()
    def hel(self):
        for j in range(self.number):
            print( text.generate_sentence(self))
        return 0


def unirand(seq):#делает предожения рандомными 
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token
print ('Введите количество предложений')
i = input()
#print (t2)
tols = text('text.txt', i)     

tols.hel()
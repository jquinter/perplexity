#!/usr/bin/env python

import os, operator
from decimal import *
from math    import *

source_annot  = "annot_prop.txt"
source_vocab  = "vocab.txt"
source_reque  = "req.txt"

dic_annot = []
dic_vocab = []
dic_reque = []
dic_resul = []

with open(source_annot) as c: [dic_annot.append(e.split()) for e in c]
with open(source_vocab) as a: [dic_vocab.append([(index), e.rstrip()]) for index, e in enumerate(a)]
with open(source_reque) as b: [[dic_reque.append(i) for i in e.split()]  for index, e in enumerate(b)]
indexes = [item for sublist in [[x[0] for x in dic_vocab if x[1] == e] for e in dic_reque] for item in sublist]

output_score = open("score.txt", "w")
output_score_ind = open("score_last.txt", "w")

for e in map(list, zip(*dic_annot)):
  reduced = reduce(operator.mul, [Decimal(e[_]) for _ in indexes], 1)
  output_score.write(str(reduced) + "\n")
  dic_resul.append(reduced)
  
score_ind = [x for x in sorted([[index, e] for index, e in enumerate(dic_resul)], key = lambda e: e[1], reverse = True)]
output_score_ind.write(" ".join([str(Decimal(e[0])+1) for e in score_ind]))
output_score_ind.write("\n")

output_score.close()
output_score_ind.close()

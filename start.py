#!/usr/bin/env python

import os
from decimal import *

source_beta  = "beta"
source_theta = "theta"

data_beta   = []
data_theta  = []
data_result = []

with open(source_beta) as beta: [data_beta.append(e.split()) for index, e in enumerate(beta)]
with open(source_theta) as theta: [data_theta.append(e.split()) for index, e in enumerate(theta)]
    
i = 0
for e in data_theta:
  pre = []
  for index, _ in enumerate(data_beta[0]):
    pre.append(sum([(Decimal(e_) * Decimal(data_beta[index_][index])) for index_, e_ in enumerate(e)]))
    print (str(i) + "@" + str(len(data_theta)))
    i = i + 1
  data_result.append(pre)

with open('annot_prop.txt', 'w') as output:
  for index, _ in enumerate(data_beta[0]):
    output.write(" ".join([str(x[index]) for x in data_result]))
    output.write("\n")
  output.close()

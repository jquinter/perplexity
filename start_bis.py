#!/usr/bin/env python

import os
from decimal import *

source_result  = "annot_prop.txt"

with open(source_result) as a:
  data = [[[index, Decimal(b)] for index_, b in enumerate(e.split())] for index, e in enumerate(a)]
  with open("annot.txt", "w") as output:
    for index, _  in enumerate(data[0]):
      to_sort = [[x for x in data[index_][index]] for index_, _ in enumerate(data)]
      output.write(" ".join([str(x[0]) for x in sorted(to_sort, key = lambda e: e[1], reverse = True)]))
      output.write("\n")
      
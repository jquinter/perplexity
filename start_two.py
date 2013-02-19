#!/usr/bin/env python

import os
import heapq

from decimal import *
from math    import *

source_result  = "annot_prop.txt"
dic_annot = []

with open(source_result) as a: [dic_annot.append(e.split()) for e in a]
n = input('Please enter the # of values to take : ')
l = [heapq.nlargest(n, _) for _ in map(list, zip(*dic_annot))]
c = sum([sum([log(Decimal(_), 10) for _ in e if (Decimal(_) != 0)]) for e in l])
c = exp(-1 * (Decimal(c) / Decimal(len(l) * len(l[0]))))

with open("perp.txt", "w") as d: d.write(str(c) + "\n")

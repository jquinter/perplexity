#!/usr/bin/env python

import os
from decimal import *
from math    import *

source_result  = "annot_prop.txt"
source_beta    = "beta"

with open(source_result) as a:
  with open(source_beta) as b: beta = len([x.split() for x in b][0])
  c = log(sum([sum([Decimal(_) for _ in e.split() if (Decimal(_) != 0)]) for e in a]))
  c = exp(-1 * (Decimal(c) / Decimal(beta)))
  with open("perp.txt", "w") as d: d.write(str(c) + "\n")

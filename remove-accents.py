#!/usr/bin/env python

import sys
import string
import unicodedata

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r') as fin:
    contents = fin.read()
    
with open(outfile, 'w') as fout:
    newcontents = unicodedata.normalize("NFKD", contents).translate({ord(c): None for c in "̓̔́̀͂ͅ"})
    fout.write(newcontents)

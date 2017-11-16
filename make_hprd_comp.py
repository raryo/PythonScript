#!/usr/bin/python
import sys

#
# input  : HPRD/PROTEIN_COMPLEX.dat as STD
# output : hprd_comp_list.dat
#

complex = {}
for l in sys.stdin.readlines():
    cols = l.split()
    id   = cols[0]
    gene = cols[2]
    if not id in complex:
        complex[id] = []
    complex[id] += [gene]

for id in complex:
    genes = ';'.join(sorted(list(set(complex[id]))))
    print(id, genes)

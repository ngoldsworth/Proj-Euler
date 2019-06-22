#!/usr/bin/env python3

nl = open('022names.txt', 'r').read().split(',')
nl.sort()

def name_subscore(n: str):
    n = list(n.lower())
    subscore = 0
    for char in n:
        subscore = subscore + ord(char) - 96
    return subscore

def name_tot_score(namelist: list, name: str):
    totscore = (namelist.index(name) + 1) * name_subscore(name) # since arrays start at zero
    return totscore

print(name_tot_score(nl, 'COLIN'))

grand_tot = 0
for name in nl:
    addendum = name_tot_score(nl, name)
    grand_tot = grand_tot + addendum
    print(name, addendum)

print(grand_tot)

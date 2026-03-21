"""
src: https://www.codewars.com/kata/5254ca2719453dcc0b00027d
"""

import itertools


def permutations(s):
    perms = itertools.permutations(s)
    permutations = ["".join(p) for p in perms]
    return set(permutations)

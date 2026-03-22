"""
src: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
"""


def duplicate_encode(word):
    word = word.lower()
    dic = {}
    sol = ""
    for c in word:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    for c in word:
        if dic[c] == 1:
            sol += "("
        else:
            sol += ")"
    return sol

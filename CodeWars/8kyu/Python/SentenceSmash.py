"""
src: https://www.codewars.com/kata/53dc23c68a0c93699800041d
"""


def smash(words):
    sol = ""
    for w in range(len(words)):
        sol += words[w]
        if w != len(words) - 1:
            sol += " "
    return sol

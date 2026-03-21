"""
src:https://www.codewars.com/kata/546e2562b03326a88e000020
"""


def square_digits(num):
    s = str(num)
    sol = []
    for c in s:
        n = str(int(c) ** 2)
        sol.append(n)
    return int("".join(sol))

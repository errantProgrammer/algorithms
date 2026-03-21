"""
src: https://www.codewars.com/kata/563cf89eb4747c5fb100001b
"""


def remove_smallest(numbers):
    if not numbers:
        return []
    res = numbers.copy()
    i = min(res)
    res.remove(i)
    return res

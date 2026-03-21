"""
src: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
"""


def duplicate_count(text):
    unique = set()
    duplicate = set()
    text = text.lower()
    sol = 0
    for c in text:
        if c in unique:
            if c in duplicate:
                continue
            else:
                duplicate.add(c)
                sol += 1
        else:
            unique.add(c)
    return sol


"""
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
"""

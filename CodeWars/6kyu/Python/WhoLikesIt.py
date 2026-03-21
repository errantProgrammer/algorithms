"""
src: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""


def likes(names):
    size = len(names)
    if size == 0:
        return "no one likes this"
    elif size == 1:
        return names[0] + " likes this"
    elif size == 2:
        return names[0] + " and " + names[1] + " like this"
    elif size == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return (
            names[0] + ", " + names[1] + " and " + str(size - 2) + " others like this"
        )

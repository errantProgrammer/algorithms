"""
src: https://www.codewars.com/kata/583710ccaa6717322c000105
"""


def simple_multiplication(number):
    return number * (9 if number & 1 else 8)

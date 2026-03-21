"""
src: https://www.codewars.com/kata/52449b062fb80683ec000024
"""


def generate_hashtag(s):
    if not s or not s.strip():
        return False

    words = [word.capitalize() for word in s.split()]
    hashtag = "#" + "".join(words)

    return hashtag if len(hashtag) <= 140 else False

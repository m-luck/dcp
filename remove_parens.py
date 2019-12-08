import unittest

def removeOuterParens(S: str):

    res = []
    opened = 0
    for c in S:
        if c == "(" and opened > 0: res.append(c)
        if c == ")" and oepned > 1: res.append(c)
        opened += 1 if c == "(" else -1
    return ''.join(res)
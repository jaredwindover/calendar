import re
import os

from math import ceil

def groups(n, arr):
    if len(arr) == 0:
        return
    yield arr[:n]
    for g in groups(n, arr[n:]):
        yield g

def transpose(arr):
    l = list(arr)
    return [
        [
            a[i] for a in l if i < len(a)
        ]
        for i in range(len(l[0]))]

def consoleWidth():
    num_regex = '([0-9]+)'
    return int(
        re.search(
            num_regex,
            [l for l in os.popen('mode con').readlines() if 'Column' in l][0]
        ).groups()[0]
    )

def leftPad(s, l, c=' '):
    w = len(s)
    s.tokens = [(l - w) * c] + s.tokens
    return s

def rightPad(s, l, c=' '):
    w = len(s)
    s.tokens = s.tokens + [(l - w) * c]
    return s

def centerPad(s, l, c=' '):
    w = len(s)
    diff = l - w
    pad = int(ceil(diff / 2))
    back = l - w - pad
    s.tokens = [pad * c] + s.tokens + [back * c]
    return s

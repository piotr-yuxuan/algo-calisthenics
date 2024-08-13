import argparse
from typing import Counter
import argcomplete


def solution(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    d = dict()
    for i in s1:
        d[i] = d.get(i, 0) + 1
    for i in s2:
        d[i] = d.get(i, 0) - 1
        if d[i] == 0:
            d.pop(i)
    return not d


def solution_with_counters(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def solution_with_sorted(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def solution_constant_space_sum(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sum(map(ord, s1)) == sum(map(ord, s2))


def solution_constant_space_xor(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    acc = 0
    for c1, c2 in zip(s1, s2):
        acc ^= ord(c1)
        acc ^= ord(c2)
    return acc == 0

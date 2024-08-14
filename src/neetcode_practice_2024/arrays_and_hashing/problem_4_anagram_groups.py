#!/usr/bin/env python

import argparse
import argcomplete

from typing import Dict, Generic, List, Optional, TypeVar
import functools
from collections import defaultdict


def solution_naive(input: List[str]):
    acc = defaultdict(list)
    for s in input:
        acc["".join(sorted(s))].append(s)
    return list(acc.values())


def solution_character_counting(input: List[str]):
    acc = defaultdict(list)
    for s in input:
        a = [0] * 26
        for i in s:
            if not ord("a") <= ord(i) <= ord("z"):
                raise ValueError(
                    f"Unexpected character {i} with integer value of {ord(i)}."
                )
            a[ord(i) - ord("a")] += 1
        acc[tuple(a)].append(s)
    return list(acc.values())


K = TypeVar("K")
V = TypeVar("V")


class Node(Generic[K, V]):
    def __init__(self):
        self.children: Dict[K, "Node[K, V]"] = defaultdict(Node)
        self.values: List[V] = list()

    def __repr__(self) -> str:
        default_repr = object.__repr__(self)
        return f"{default_repr} {{children: {self.children.keys()}, values: {self.values}}}"


class Trie(Generic[K, V]):
    def __init__(self):
        self.root: Node[K, V] = Node()

    def node_at(self, path: List[K]) -> Node[K, V]:
        return functools.reduce(lambda node, k: node.children[k], path, self.root)

    def insert(self, path: List[K], value: V):
        self.node_at(path).values.append(value)

    def values_at(self, path: List[K]) -> List[V]:
        return self.node_at(path).values

    def values_under(self, path: List[K]):
        result: List[V] = []
        self._traverse(self.node_at(path), result)
        return result

    def _traverse(self, node: Node[K, V], result: List[V]):
        if node.values:  # not empty
            result.append(node.values)
        for _, n in node.children.items():
            self._traverse(n, result)


def solution_trie_based(input: List[str]):
    t = Trie()
    for s in input:
        t.insert(sorted(s), s)
    return t.values_under([])


def solution(input: List[str]):
    seen = dict()
    acc = []

    def hash_agg(a, b):
        return a * ord(b)

    for s in input:
        x = functools.reduce(hash_agg, s, 1)
        if x not in seen:
            seen[x] = len(acc)
            acc.append([])  # at index i
        i = seen[x]
        acc[i].append(s)
    return acc


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and hashing, problem 4 anagram groups."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda x: list(x.split(",")),
        required=True,
        help="XXX",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)

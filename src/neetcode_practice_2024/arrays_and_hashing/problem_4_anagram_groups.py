#!/usr/bin/env python

import argparse
import argcomplete

from typing import List
import functools


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

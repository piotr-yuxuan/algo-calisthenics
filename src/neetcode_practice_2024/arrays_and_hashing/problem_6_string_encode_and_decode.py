#!/usr/bin/env python

import argparse
import argcomplete

from typing import List
from enum import Enum


class Action(Enum):
    ENCODE = "encode"
    DECODE = "decode"


DELIMITER = ":"


def encode(input) -> str:
    return "".join([f"{len(s)}{DELIMITER}{s}" for s in input])


def decode(s: str) -> List[str]:
    ret = []
    tag_start = 0
    while tag_start < len(s):
        tag_end = s.find(DELIMITER, tag_start)
        word_length = int(s[tag_start:tag_end])
        ret.append(s[slice(tag_end + 1, tag_end + 1 + word_length)])
        tag_start = tag_end + word_length + 1
    return ret


def main(args):
    if args.action == Action.ENCODE:
        return encode(args.input)
    elif args.action == Action.DECODE:
        return decode(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and hashing, problem 6 string encode and decode."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda s: [int(i) for i in s.split(",")],
        required=True,
        help="The input array as a comma-separated list of strings: `aze, zer, ert`.",
    )

    parser.add_argument(
        "--action",
        "-a",
        type=Action,
        choices=list(Action),
        required=True,
        help="The action to perform: `encode` or `decode`.",
    )
    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)

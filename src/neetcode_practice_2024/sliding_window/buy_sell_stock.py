#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_intuitive(input: List[int]) -> int:
    n = len(input)

    if n < 2:
        return 0

    def calculate_profit(min_price, max_price):
        return max_price - min_price

    # Keep track of these values:
    min_price = input[0]
    # We could keep track of `max_price` but it is not useful to this
    # specific problem where we can only sell stocks after we have
    # bought them.
    max_profit = calculate_profit(min_price, min_price)

    for sell_day in range(1, n):
        price = input[sell_day]

        min_price = min(min_price, price)
        max_profit = max(
            max_profit,
            calculate_profit(
                min_price,
                price,
            ),
        )

    return max_profit


def solution_brute_force(input: List[int]) -> int:
    n = len(input)

    if n < 2:
        return 0

    def calculate_profit(
        input: List[int],
        buy_day: int,
        sell_day: int,
    ) -> int:
        return input[sell_day] - input[buy_day]

    return max(
        [
            calculate_profit(input, buy_day, sell_day)
            for buy_day in range(n - 1)
            for sell_day in range(buy_day + 1, n)
        ]
        + [0]
    )


def solution(input):
    return solution_intuitive(input)


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=", ".join(
            "Neetcode 2024",
            "sliding window",
            "problem 1 best time to buy and sell stock.",
        )
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda s: [int(i) for i in s.split(",")],
        required=True,
        help="The input array as a comma-separated list of integers: `1,2,3`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)

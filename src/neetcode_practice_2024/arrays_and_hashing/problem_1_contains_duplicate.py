import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar


class Comparable(Protocol):
    def __le__(self, other: "Comparable") -> bool: ...


T = TypeVar("T")
U = TypeVar("U", bound=Comparable)
KeyFunc = Callable[[T], U]


# It would be more idiomatic to have this function nested under a
# parent merge function, but as it is reused let's extract it.
def merge(
    left: List[T],
    right: List[T],
    key: KeyFunc = None,
) -> List[T]:
    merged: List[T] = list()
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(
    l: List[T],
    key: Optional[KeyFunc] = None,
) -> List[T]:
    """Implement merge sort on a list `l` of any item type, provided
    that there are comparable or convertible to a comparable type with
    the `key` function.

    Top-down, divide-and-conquer approach.
    """
    if key is None:
        key: KeyFunc = lambda x: x

    if len(l) <= 1:
        return l

    left = merge_sort(l[: len(l) // 2], key=key)
    right = merge_sort(l[len(l) // 2 :], key=key)

    return merge(left, right, key=key)


def solution_not_optimal(
    l: List[T],
    key: Optional[KeyFunc] = None,
) -> bool:
    if key is None:
        key: KeyFunc = lambda x: x

    sorted_list = merge_sort(l, key)
    for i in range(len(l) - 1):
        if key(sorted_list[i]) == key(sorted_list[i + 1]):
            return False
    return True


def solution(
    l: List[T],
) -> bool:
    seen = set()
    for i in l:
        if i in seen:
            return False
        else:
            seen.add(i)
    return True


def merge_sort_bottom_up(
    l: List[T],
    key: Optional[KeyFunc] = None,
) -> List[T]:
    """Merge sort, bottom-up approach. Here we rely on previous steps
    walked through previous computations to built the arguments sent
    to `merge`.

    Bottom-up, divide-and-conquer approach.
    """
    if key is None:
        key: KeyFunc = lambda x: x
    width = 1
    while width < len(l):
        for i in range(0, len(l), 2 * width):
            l[i : min(i + 2 * width, len(l))] = merge(
                l[i : i + width],
                l[i + width : min(i + 2 * width, len(l))],
                key=key,
            )
        width *= 2
    return l


def merge_sort_dynamic_programming_tabulation(
    l: List[T],
    key: Optional[KeyFunc] = None,
) -> List[T]:
    """It is a contrived implementation because merge sort as an
    algorithm has no overlapping problems, but it is to help the
    reader to better understand on a known algorithm.

    Tabulated dynamic programming approach.
    """
    if key is None:
        key: KeyFunc = lambda x: x

    dp = [[x] for x in l]
    size = 1
    while size < len(l):
        for i in range(0, len(l), 2 * size):
            dp[i : min(i + 2 * size, len(l))] = [
                merge(
                    l[i : i + size],
                    l[i + size : min(i + 2 * size, len(l))],
                    key=key,
                )
            ]
        size *= 2
    return dp[0]


def main(args):
    return solution(args.integer_array)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and string, problem 1: contains duplicate."
    )
    parser.add_argument(
        "--integer_array",
        "-i",
        type=lambda x: list(map(int, x.split(","))),
        required=True,
        help="input integer array.",
    )
    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)

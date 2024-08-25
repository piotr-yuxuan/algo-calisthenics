#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, Counter, Dict, List, Optional, Protocol, Tuple, TypeVar
import collections
import heapq

solution_stdlib: Callable[[List[int], int], List[int]] = lambda input, k: [
    tuple[0] for tuple in Counter(input).most_common(k)
]


def solution_std_minheap(
    input: List[int],
    n: int,
) -> List[int]:
    frequencies = collections.defaultdict(int)
    for i in input:
        frequencies[i] += 1
    heap = []
    for k, freq in frequencies.items():
        heapq.heappush(heap, (freq, k))
        if n < len(heap):
            heapq.heappop(heap)
    return [tuple[1] for tuple in heap]


class LeComparable(Protocol):
    def __le__(self, other: "LeComparable") -> bool: ...


K = TypeVar("K", bound=LeComparable)

# Stylistic note: I choose to express the invariant always in the same
# textbook form, with `<=`.


def heap_insert(heap: List[K], v: K):
    """The algorithm is quite simple: add the new element as the
    rightmost element at the lowest level. Most likely is breaks the
    heap invariant, then restore it by swapping with its parent as
    necessary. At most we go from lowest level to top tree level,
    which has a height of $\\mathcal{O}(\\log n)$, so this is the time
    complexity.

    """
    # Break the invariant:
    heap.append(v)

    # Restore the invariant by moving the new element up in the tree.
    current_position = len(heap) - 1
    while 0 < current_position:
        parent_position = (current_position - 1) // 2
        if heap[parent_position] <= heap[current_position]:
            break

        heap[parent_position], heap[current_position] = (
            heap[current_position],
            heap[parent_position],
        )
        current_position = parent_position


def heap_extract(heap: List[K]) -> Optional[K]:
    """The algorithm is quite simple: swap heap[-1] and heap[0], which
    clearly breaks the invariant, then then restore it by swapping the
    parent with its smallest child until it is no longer necessary. At
    most we go from top tree level to lowest level, which has a height
    of $\\mathcal{O}(\\log n)$, so this is the time complexity.

    """
    if len(heap) == 0:
        return None

    # Extract the root element (smallest element in a min-heap).
    ret = heap[0]

    # Break the invariant:
    heap[0] = heap[-1]
    heap.pop()

    # Restore the invariant:
    parent_position = 0
    while True:
        smallest_element_position = parent_position
        left_position, right_position = 2 * parent_position + 1, 2 * parent_position + 2

        # Position of min(min(parent, left_child), right_child).
        if left_position < len(heap) and not (
            heap[smallest_element_position] <= heap[left_position]
        ):
            smallest_element_position = left_position

        if right_position < len(heap) and not (
            heap[smallest_element_position] <= heap[right_position]
        ):
            smallest_element_position = right_position

        if smallest_element_position == parent_position:
            break

        (
            heap[parent_position],
            heap[smallest_element_position],
        ) = (
            heap[smallest_element_position],
            heap[parent_position],
        )

        parent_position = smallest_element_position

    return ret


def solution(input, k):
    frequencies: Dict[int, int] = collections.defaultdict(int)
    for i in input:
        frequencies[i] += 1
    heap: List[Tuple[int, int]] = []
    for i, freq in frequencies.items():
        if k == len(heap) and (freq, i) <= heap[0]:
            # Equivalent of an insert immediately followed by an
            # extract to maintain the partial sort.
            continue
        heap_insert(heap, (freq, i))
        if k < len(heap):
            heap_extract(heap)
    return [tuple[1] for tuple in heap]


def solution_bucket_sort(input: List[int], k: int) -> List[int]:
    frequencies: Dict[int, int] = collections.defaultdict(int)
    for i in input:
        frequencies[i] += 1
    buckets = collections.defaultdict(list)
    for i, frequency in frequencies.items():
        buckets[frequency].append(i)
    result = []
    for frequency in range(len(input), 0, -1):
        if frequency in buckets:
            result.extend(buckets[frequency])
        if k <= len(result):
            break
    return result[:k]


def main(args):
    return solution(args.input, args.k_most)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, arrays and hashing, problem 5 top k elements in list."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda s: [int(i) for i in s.split(",")],
        required=True,
        help="The input array as a comma-separated list of integers: `1,2,3`.",
    )
    parser.add_argument(
        "--k-most",
        "-k",
        type=int,
        required=True,
        help="The width of partial count.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)

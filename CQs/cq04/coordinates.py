"""CQ04 coordinates file."""

__author__ = "730672220"


def get_coords(xs: str, ys: str) -> None:
    index1 = 0
    while index1 <= len(xs) - 1:
        index2 = 0
        while index2 <= len(ys) - 1:
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index1 += 1

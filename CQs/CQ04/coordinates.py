"""Importing and Scope Challenge Question"""

__author__ = "730466510"


def get_coords(xs: str, ys: str) -> None:
    idx_x: int = 0
    while idx_x < len(xs):
        idx_y: int = 0
        while idx_y < len(ys):
            print(f"({xs[idx_x]}, {ys[idx_y]})")
            idx_y += 1
        idx_x += 1

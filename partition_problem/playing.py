from copy import copy

def _rec(arr, n, m):
    if n < 1:
        return

    yield from _rec(arr, n-1, m)

    for i in range(1,m):
        arr_loop = copy(arr)
        arr_loop[n-1] = i
        yield arr_loop
        yield from _rec(arr_loop, n-1, m)


def main(n, m):

    arr = [0]*n

    yield arr
    yield from _rec(arr, n-1, m)

    for i in range(1,m):
        arr_loop = copy(arr)
        arr_loop[n-1] = i
        yield arr_loop
        yield from _rec(arr_loop, n-1, m)


if __name__ == "__main__":
    for arr in main(4, 3):
        print(arr)


def lookup_table(func):
    table = {}

    def wrapped_function(n):
        if n not in table:
            table[n] = func(n)

        return table[n]

    return wrapped_function


@lookup_table
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(15):
        print(fib(i))


if __name__ == "__main__":
    main()

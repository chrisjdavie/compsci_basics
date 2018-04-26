from memory_profiler import profile


def generator_cached(generator_fn, *args, **kwargs):

    previous_values = []
    gen = generator_fn(*args, **kwargs)

    def generator_from_cache():
        
        for val in previous_values:
            yield val

        for val in gen:
            previous_values.append(val)
            yield val

    return generator_from_cache



def wrapper(N):
    for i in generate_primes(510510):
        pass
@profile
def generate_primes(N = 1000):
    # N is the loop limit

    D = {}

    for q in range(2, N):
        if q not in D:
            # is a prime
            #yield q
            # add to the sieve at the square
            # - first time it's the sole prime factor
            D[q*q] = [q]
        else:
            # shift all the primes for D[q] up to the
            # next time 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q] # free up some memory
    return



if __name__ == "__main__":
    import timeit

    #print(timeit.timeit("for i in generate_primes(510510): pass", number=1, globals=globals()))
    generate_primes(100000)

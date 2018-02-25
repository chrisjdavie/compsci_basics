I redid the tabulation for two reasons

- I forgot to think about corner cases (specifically index 0 and zero length arrays, but that is not in the specification)
- my tabulation solution is O(M*N) in time and O(M) in memory (where M is the largest element in the the array, and N is the length of the array), and often M >> N, it could easily be a O(N**2) in time and O(N) in memory solution, though it needs a little more code (and the best case is the same as the worst case, whereas with the tabulation solution the best case is O(1) in both, for sequences of a single number).

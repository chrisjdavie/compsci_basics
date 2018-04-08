Length of array - N, target value, K

The simplest solution, to use Python's sort and return the kth value, is somewhere between O(N) and O(NlnN), as that's the range for Timsort.

The heap solution is expected O(NlnK), and requires not much extra code. The quick search solution is best average O(N), but has a worst case O(N**2). Also requires quite a lot of code, and actually runs more slowly (probably) on the test solutions.

There is a quite painfully complex O(N) version, I read it and understood it but it is reported as being impractical due to the heavy cost of each calculation.

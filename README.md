# Compsci Basics

I'm from a Physics background, so computer science fundamentals are still a weak point. And therefore I learn.

## Subject 1 - Dynamic Programming

I'm not too bad at this, but my formal understanding is pretty limited. So, start from here

| Problem   | Link  | Solutions  |
| --------- | ----- | ---------- |
| Fibonacci  | https://www.geeksforgeeks.org/?p=12635  | Recursive, memoization, tabulation, sensible  |
| Longest Common Subsequence  | https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0  | Recursive, memoization, tabulation  |
| Longest Increasing Subsequence  | https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0  | Tabulation, recursive, memoization  |
| Edit Distance  | https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/  | Recursive, memoization, tabulation  |
| Partition problem  | https://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/  | Recursive, tabulation, queue  |
| Minimum Sum Partition  | https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/  | Recursive, Queue  |
| Path in Matrix  | https://practice.geeksforgeeks.org/problems/path-in-matrix/0  | Recursive, memoization  |
| Subset Sum  | https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/  | Recursive, tabulation  |

### Redo

Wasn't happy with how I performed on these

| Problem  | Solution  | Notes  |
| -------- | --------- | ------ |
| Longest Increasing Subsequence  | Recursive  | I couldn't figure out the recursive solution without a hint  |
| Partition problem  | Recursive  | I got slow, working solutions because I didn't know about recursive combination generation  |
| Minimum Sum Partition  | Queue  | Made far too many typos when building solution  |
| Path in Matrix  | Recursive, tabulation  | Had real issues with columns and row in the right order, which is unusual  |
| Subset Sum  | Tabulation  | Column, row issues, typos  |

### Thoughts

* Tabulation works when there's a clear indexing
* Memoization works when there's a unique representation of a subproblem that gets repeatedly solved
* Tabulation and memoization works when there's a depth-first solution, filling in the blanks
* Queue solutions don't reduce the complexity of the problem, but do reduce the recursion
* Queue solutions don't seem to have much benefits over tabulation for backwards filling - except perhaps in the sense of decoupling the logic of the problem from the logic of the iteration
  * I wonder if there is a problem class that uses cacheing (as per memoization) over multiple problem types - some ranges of function that produces stateless answers, and has the inputs regularly reused

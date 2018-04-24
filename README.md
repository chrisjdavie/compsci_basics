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
| Minimum Sum Partition  | https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/  | Recursive, queue, tabulation  |
| Path in Matrix  | https://practice.geeksforgeeks.org/problems/path-in-matrix/0  | Recursive, memoization  |
| Subset Sum  | https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/  | Recursive, tabulation, queue  |
| Tom and Jerry  | https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/  | Recursive, memoization, simple  |
| Pick from top or bottom  | https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/  | Recursive, memoization, tabulation  |
| 0-1 knapsack problem  | https://www.geeksforgeeks.org/knapsack-problem/  | Recursive, tabulation  |
| Boolean Parenthesization Problem  | https://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/  | Recursive, memoization, tabulation  |


### Redo

Wasn't happy with how I performed on these

| Problem  | Solution  | Notes  |
| -------- | --------- | ------ |
| Longest Increasing Subsequence  | Recursive  | I couldn't figure out the recursive solution without a hint  |
| Partition problem  | Recursive  | I got slow, working solutions because I didn't know about recursive combination generation  |
| Minimum Sum Partition  | Queue, tabulation  | Made far too many typos when building solution  |
| Path in Matrix  | Recursive, tabulation  | Had real issues with columns and row in the right order, which is unusual  |
| Subset Sum  | Tabulation. Queue  | Column, row issues, typos. Made off-by one error in indexing  |
| Pick from top or bottom  | Didn't get the code expression of the algorithm correct first time  | Tabulation  |
| Boolean Parenthesization Problem  | Indexing wrong all over the place, typos  | Memoization, Tabulation  |

### Thoughts

* Tabulation works when there's a clear indexing
* Memoization works when there's a unique representation of a subproblem that gets repeatedly solved
* Tabulation and memoization works when there's a depth-first solution, filling in the blanks
* Queue solutions don't reduce the complexity of the problem, but do reduce the recursion
* Queue solutions don't seem to have much benefits over tabulation for backwards filling - except perhaps in the sense of decoupling the logic of the problem from the logic of the iteration
  * I wonder if there is a problem class that uses cacheing (as per memoization) over multiple problem types - some ranges of function that produces stateless answers, and has the inputs regularly reused
* Probably ought to watch more videos with how people talk/think about this, some gaps in my head
* Need to think more about indicies before I implement these - even though I have the pattern, translating that into the indicies isn't something I do well atm

## Subject 2 - Sorting and searching

| Problem   | Link  | Solutions  |
| --------- | ----- | ---------- |
| Binary search  | https://www.geeksforgeeks.org/binary-search/  | Iterative, recursive  |
| Bitonic array  | https://practice.geeksforgeeks.org/problems/finding-number/0  | Recursive, iterative  |
| Bubble sort  | https://www.geeksforgeeks.org/bubble-sort/  | Iterative  |
| Insertion sort  | https://www.geeksforgeeks.org/insertion-sort/  | Iterative  |
| Merge sort  | https://www.geeksforgeeks.org/merge-sort/  | Recursive  |
| Heap sort  | https://www.geeksforgeeks.org/heap-sort/  | Iterative  |
| Quick sort  | https://www.geeksforgeeks.org/quick-sort/  | Recursive  |
| Interpolation Search  | https://www.geeksforgeeks.org/interpolation-search/  | Iterative  |
| Kth smallest  | https://practice.geeksforgeeks.org/problems/kth-smallest-element/0 | Heap, Quick Search  |
| Key pair  | https://practice.geeksforgeeks.org/problems/key-pair/0  | O(N)  |


### Redo

Wasn't happy with how I performed on these

| Problem  | Solution  | Notes  |
| -------- | --------- | ------ |
| Binary search  | Iterative  | Messed up on the midpoint calculation  |
| Bitonic array  | Recursive  | Lots of small errors, around recursion and indexing. I'm having consistent issues with getting indexing correctly, I need to more carefully build the algorithm? Proper TDD would help, exploring every route through the code, though that's not 100% what I'm here for  |
|  Merge sort  | Recursive  | I got the formula wrong the first time, though did come up with a cool generator solution  |
| Heap sort  | Iterative  | Wrong formula first time, issues with the sort part 2nd time  |
| Quick sort  | Recursive  | Did pretty well, just very slow  |

### Thoughts

Python doesn't use any of these, it uses Timsort, which "is a hybrid stable sorting algorithm, derived from merge sort and insertion sort" (Wiki!). https://bugs.python.org/file4451/timsort.txt. Prior to that it used "samplesort". 

Ultimately, for most data sizes I'm going to use sorting isn't going to be a thing I'll be implementing on my own, and if I do have to, I'll have to read up a lot on existing solutions. This has been solved before, by lots of people.

## Subject 3 - Trees

| Problem   | Link  | Solutions  |
| --------- | ----- | ---------- |
| Find Minimum Depth of a Binary Tree |  https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/  | BFS  |
| Maximum path sum of a binary tree |  https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/  | DFS post-order  |
| Can an array represent preorder traversal of a binary tree  |  https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/  | Tree, stack  |
| Postorder to preorder representation of a binary tree  |  https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/  | Stack  |
| Check if full binary tree  | https://practice.geeksforgeeks.org/problems/full-binary-tree/1  | Stack, recursive  |
| Bottom view of a binary tree  | https://www.geeksforgeeks.org/bottom-view-binary-tree/  | Stack, recursive  |
| Top view of a binary tree  | https://www.geeksforgeeks.org/bottom-view-binary-tree/  | Queue  |
| Remove nodes below min root to leaf path  | https://www.geeksforgeeks.org/remove-nodes-root-leaf-paths-length-k/  | Recursive, iterative (stack and queue)  |
| Lowest common ancestor in a binary search tree  | https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/  | Recursive, stack  |
| Reverse alternate levels of a perfect binary tree  | https://practice.geeksforgeeks.org/problems/reverse-alternate-levels-of-a-perfect-binary-tree/1  | Recursive, queue  |

### Redo

Wasn't happy with how I performed on these

| Problem  | Solution  | Notes  |
| -------- | --------- | ------ |
| Can an array represent preorder traversal of a binary tree  | Stack  | I hadn't really considered the connection between stacks and binary search trees  |
| Postorder to preorder representation of a binary tree  | Stack  | This required two stacks, which I hadn't considered and took me waaaay too long because of that (and not really having an intuition for problems like this it turns out)  |
| Bottom view of a binary  | Recursive  | Missed a subltey wrt to order and depth in the initial algorithm  |
| Remove nodes below min root to leaf path  | Recursive  | My initial solution wasn't ideal  | 
| Lowest common ancestor in a binary search tree  | Recursive  | My initial solution was O(N), when there's an O(logN) solution  |
| Reverse alternate levels of a perfect binary tree  | Queue  | Took me way too long to figure out, overcomplicated the testing, I instinctively rejected the simplest solution  |

## Subject 4 - Number theory

| Problem   | Link  | Solutions  |
| --------- | ----- | ---------- |
| Calculate powers  | https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/  | Recursive, iterative  |
| Modular exponentiation  | https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/  | Recursive, iterative  |

### Redo

Wasn't happy with how I performed on these

| Problem  | Solution  | Notes  |
| -------- | --------- | ------ |
| Calculate powers  | Both  | I had way more issues than I should have. Possibly I was tired  |
| Modular exponentiation  | Both  | Still a little confused (less than above)  |

## Miscellaneous

These are because I was diving into some side subjects for greater clarity on whatever I was solving

| Problem   | Link  | Solutions  | Notes  |
| --------- | ----- | ---------- | ------ |
| Next greater element  | https://practice.geeksforgeeks.org/problems/next-larger-element/0  | Naive, heap, stack  |

## TODO

I need to learn bitwise operations, I don't know this

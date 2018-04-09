Here, I implemented a BFS algorithm - there is a simpler, pre-order DFS version, but the BFS search should be faster typically as it only explores the layers until it finds a leaf and terminates. The simple DFS cannot terminate, though a global "min depth" could be passed around, allowing it to truncate some solutions.

It is implied by the question that the tree hasn't been filled in memory in a left to right, filling each layer approach. (This probably has a name...)



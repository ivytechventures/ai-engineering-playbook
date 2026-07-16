# Algorithm Problem-Solving Framework

The biggest mistake beginners make is jumping straight into code. This is the checklist to run through *before* writing any code — turning problem-solving into a repeatable process instead of trial-and-error. Most algorithm problems aren't hard because of the code; they're hard because it's easy to start coding before actually understanding the problem.

Running example throughout: **Two Sum** — given a list of integers and a target, return the indices of the two numbers that sum to the target.

## 1. Restate

Rewrite the problem in your own words. If you can't explain it simply, you don't understand it yet.

> Two Sum: given a list of integers and a target number, return the indices of the two numbers whose sum equals the target.

## 2. Assumptions

Pin down the guarantees and constraints — they often determine the right algorithm:

- Is there always a solution?
- Can there be duplicates?
- Can the input be modified?
- Are negative numbers allowed?
- Is the input sorted?
- Can extra memory be used?
- What happens if no solution exists?

> Two Sum: exactly one solution exists, the same element can't be used twice, return indices (not values).

## 3. Input / Output

What's given, and what exactly should come back? Be precise about the *shape* of the output — indices, values, a count, a boolean, a modified array, a new structure. `nums = [2,7,11,15], target = 9` → `[0,1]`, not `[2,7]`.

## 4. Looking For

What are you actually searching for? This is usually the fastest route to identifying the pattern.

- Two Sum → two numbers that add up to the target
- Binary Search → one value inside a sorted array
- DFS → a path through a graph
- Sliding Window → a best/optimal subarray

## 5. Remember

What information needs to persist while solving this? This question tends to point straight at the right data structure.

| Need to remember | Data structure |
|---|---|
| Seen values | HashMap / Set |
| Ordered data | Heap |
| Call history | Stack |
| Fast lookup | Dictionary |
| FIFO processing | Queue |

> Two Sum: previously seen numbers → HashMap.

## 6. Move

How will the solution traverse the data? Left→right, right→left, two pointers, sliding window, binary search, DFS, BFS, recursion.

> Two Sum: scan left to right, once.

## 7. Check / Update

At each step: what gets checked, and what gets updated?

- **Two Sum** — check: has the complement been seen? update: store the current number and its index.
- **Sliding window** — check: is the window still valid? update: expand or shrink it.
- **BFS** — check: has this node been visited? update: add its neighbors to the queue.

## 8. Initialization

What variables exist before the loop starts? This is often where bugs are born, so it's worth being deliberate here rather than declaring things ad hoc mid-function.

```python
seen = {}
left, right = 0, 0
max_sum = 0
queue = deque()
visited = set()
```

## 9. Brute Force First

Don't optimize immediately. What's the simplest solution that works? It gives you a working baseline, a complexity to beat, and — in an interview — shows the interviewer your thought process before you jump to the clever version.

## 10. Pattern Recognition

Most interview questions are variations on a small set of patterns. Spotting the pattern is usually harder than writing the code once you have it.

| Clue | Pattern |
|---|---|
| Previously seen values | HashMap |
| Sorted array | Binary Search / Two Pointers |
| Largest or smallest | Heap |
| Shortest path | BFS |
| All possible paths | DFS / Backtracking |
| Continuous subarray | Sliding Window |
| Optimization over choices | Dynamic Programming |

## 11. Complexity

How many times is each element visited? How much extra memory is used? Always state both time and space complexity explicitly — don't leave it implied.

---

## The full checklist

1. Restate
2. Assumptions
3. Input / Output
4. Looking For
5. Remember
6. Move
7. Check / Update
8. Initialization
9. Brute Force
10. Pattern
11. Complexity

Only after working through this does the code get written. Slowing down to answer these questions first is what makes the actual solution obvious — the framework turns "trial and error" into something structured and repeatable.
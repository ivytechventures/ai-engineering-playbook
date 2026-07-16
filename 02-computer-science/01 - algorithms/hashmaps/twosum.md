# Two Sum

**Difficulty:** Easy

**Pattern:** HashMap / Fast Lookup

📄 **Source Code:** `algorithms/hashmaps/code/twosum.py`

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers whose sum equals the target.

## Understand the Problem

**Restate:** given a list of integers and a target sum, return the indices of the two numbers whose values add up to the target.

**Assumptions:**
- Exactly one valid answer exists.
- The same element cannot be used twice.
- Return the **indices**, not the values.
- The order of the returned indices doesn't matter unless otherwise specified.

```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]   (nums[0] + nums[1] = 2 + 7 = 9)
```

**Input:** `nums` (list of integers), `target` (integer).
**Output:** `[0, 1]` — the indices of the two numbers whose sum equals the target.

## Looking For

Find two numbers whose sum equals the target and return **their indices**.

This problem is asking for:

- the indices
- only one valid pair
- not the numbers themselves

## Remember

While scanning, remember every number already seen and the index it was found at, stored as `number → index` (e.g. `{2: 0, 7: 1}`). A dictionary is ideal here since it gives fast lookups.

## Move

Scan the array left to right, visiting each element exactly once. For every number: compute its complement, check whether that complement has already been seen, return the indices if so, otherwise store the current number.

## Check / Update

**Check:** calculate the number needed to reach the target (`pair = target - num`), and ask whether it's already been seen.
**Update:** if not, store the current number and its index (`seen[num] = i`).

## Initialization

```python
seen = {}
```

A dictionary is used because both the number *and* its index need to be remembered — a set alone wouldn't be enough (more on this under Common Mistakes).

## Brute Force

The simplest solution compares every pair:

```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

Time: `O(n²)` — Space: `O(1)`. It works, but repeatedly re-scans the array.

## Key Insight

Instead of asking "does this number have a partner?", ask "what number do I need to reach the target?"

```
current = 7, target = 9 → needed = 9 - 7 = 2
```

If `2` has already been seen, the answer's found. This turns repeated searches into single dictionary lookups.

## Algorithm

1. Initialize an empty dictionary `seen`.
2. Iterate through the array.
3. Compute the complement.
4. If the complement exists in `seen`, return both indices.
5. Otherwise, store the current number and continue.

## Dry Run

```python
nums = [2, 7, 11, 15]
target = 9
# seen = {}
```
Start

seen = {}

↓

Current = 2

Need = 7

Found?

No

Store

{
2 : 0
}

↓

Current = 7

Need = 2

Found?

Yes

Return

[0,1]


## Solution

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        pair = target - num
        if pair in seen:
            return [seen[pair], i]
        seen[num] = i
    return []
```

## Complexity

- **Time:** `O(n)` — the array is scanned once; dictionary lookup is `O(1)` on average.
- **Space:** `O(n)` — worst case, every element gets stored before a match is found.

## Common Mistakes

**Returning values instead of indices**

Incorrect: `return [pair, num]`

Correct: `return [seen[pair], i]`

**Storing before checking**
Incorrect: inserting `seen[num] = i` before checking `if pair in seen` — this risks matching a number with itself. Always check first, then store.

**Using a set instead of a dictionary**
A set only remembers *whether* a number exists. The index is also needed, so a dictionary is required, not a set.

## Pattern Recognition

This is the **HashMap for Fast Lookup** pattern. Whenever a problem asks to find a pair, a complement, a duplicate, or whether a value has already been seen — think HashMap. It trades extra memory for faster lookups, turning repeated `O(n)` array searches into `O(1)` dictionary lookups.

## Related Problems

Two Sum II · Three Sum · Four Sum · Contains Duplicate · Group Anagrams · Happy Number · Longest Consecutive Sequence

## Interview Tips

Concise explanation to give out loud: the brute-force solution compares every pair, giving `O(n²)` time. To optimize, use a HashMap that stores previously seen numbers and their indices. For each number, compute its complement (`target - num`) and check whether it already exists in the HashMap — if so, return the stored index and the current index; if not, store the current number and continue. This reduces time complexity to `O(n)` at the cost of `O(n)` additional space.

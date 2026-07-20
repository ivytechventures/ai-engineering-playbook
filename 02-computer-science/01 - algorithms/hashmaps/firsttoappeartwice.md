# First Letter to Appear Twice

**Difficulty:** Easy

**Pattern:** HashMap / Frequency Counting

**Leetcode # 2351**

📄 **Source Code:** `algorithms/hashmaps/code/first_letter_to_appear_twice.py`

Given a string `s`, return the **first letter that appears twice**.

## Understand the Problem

**Restate:** Scan the string from left to right and return the first character whose **second occurrence** is encountered.

**Assumptions:**
- The string contains at least one repeated character.
- Return the character itself.
- Stop immediately once a character is seen for the second time.

```python
s = "abccbaacz"

# Output:
"c"
```

**Input:** `s` (string)

**Output:** A character.

---

## Looking For

Find the **first character whose frequency becomes 2** while scanning from left to right.

Notice this is **not** asking for:

- the character with the highest frequency
- the first repeated character after counting everything

Instead, it asks for the **first character that reaches its second occurrence**.

---

## Remember

While scanning the string, remember how many times each character has appeared.

Store:

```
character → frequency
```

Example:

```python
{
    'a': 1,
    'b': 1,
    'c': 2
}
```

A dictionary is ideal because frequency updates are **O(1)**.

---

## Move

Scan the string one character at a time.

For each character:

1. Increase its frequency.
2. If its frequency becomes **2**, return it immediately.

---

## Check / Update

**Check**

```python
if freq[ch] == 2:
```

**Update**

```python
freq[ch] = freq.get(ch, 0) + 1
```

---

## Initialization

```python
freq = {}
```

Initially, no characters have been seen.

---

## Brute Force

For every character, count how many times it appears by scanning the rest of the string.

```python
def appear_twice_brute(s):
    for i in range(len(s)):
        count = 0
        for j in range(i, len(s)):
            if s[i] == s[j]:
                count += 1
                if count == 2:
                    return s[i]
```

Time: **O(n²)**

Space: **O(1)**

This repeatedly scans the string.

---

## Key Insight

Instead of recounting every character repeatedly, remember the frequency as you scan.

The moment a character's count reaches **2**, you've found the answer.

There's no reason to continue scanning.

---

## Algorithm

1. Create an empty dictionary.
2. Scan the string.
3. Increment the character's frequency.
4. If the frequency becomes **2**, return the character.
5. Otherwise continue scanning.

---

## Dry Run

```python
s = "abccbaacz"

freq = {}
```

| Character | Frequency | Return? |
|-----------|----------:|---------|
| a | 1 | No |
| b | 1 | No |
| c | 1 | No |
| c | 2 | ✅ Return `"c"` |

---

## Solution

```python
def appeartwice(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

        if freq[ch] == 2:
            return ch

    return None
```

---

## Complexity

- **Time:** `O(n)` — each character is processed once.
- **Space:** `O(n)` — in the worst case, every character is unique before the duplicate appears.

---

## Common Mistakes

### Updating after checking

Incorrect:

```python
if freq[ch] == 2:
    return ch

freq[ch] += 1
```

The count hasn't been incremented yet.

Always update first.

---

### Forgetting the default value

Incorrect:

```python
freq[ch] += 1
```

This raises a `KeyError` the first time a character appears.

Use:

```python
freq[ch] = freq.get(ch, 0) + 1
```

---

### Counting the whole string first

Many people build the entire frequency map before answering.

That works for other problems, but **this problem specifically wants the first character whose second occurrence happens while scanning**, so return immediately when the count reaches 2.

---

## Pattern Recognition

This is the **HashMap Frequency Counting** pattern.

Whenever a problem asks:

- count occurrences
- detect duplicates
- find the first repeated element
- track frequencies

think **HashMap**.

---

## Related Problems

Contains Duplicate · Valid Anagram · First Unique Character · Majority Element · Top K Frequent Elements · Ransom Note

---

## Interview Tips

Explain that the brute-force solution repeatedly counts characters, resulting in `O(n²)` time. A HashMap lets you maintain the running frequency of each character while scanning once. As soon as a character's frequency reaches two, return it immediately. This reduces the runtime to `O(n)` with `O(n)` extra space.
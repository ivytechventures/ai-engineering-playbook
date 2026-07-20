# Sliding Window

## Definition

Sliding window is an algorithmic pattern used to process a contiguous section
of an array or string.

Instead of recalculating every group from the beginning, the window moves
through the data while updating only what entered and left the window.

## When to use it

Look for sliding window when a problem involves:

- contiguous subarrays
- contiguous substrings
- maximum or minimum range
- a fixed-size group
- a condition that changes as elements enter or leave

## Example

Find the maximum sum of three consecutive numbers:

```text
[2, 1, 5, 1, 3, 2]
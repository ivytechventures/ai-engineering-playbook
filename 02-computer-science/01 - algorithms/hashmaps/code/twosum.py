def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums): 
        pair = target - num
        if pair in seen:
            print(f"pair that made {target}: {pair} + {num} at indices {seen[pair]} and {i}")
            return [seen[pair], i]
        seen[num] = i

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9

# # O(n) time complexity, O(n) space complexity

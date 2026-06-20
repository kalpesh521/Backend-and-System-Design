"""
3Sum — complete logic in one read:

Problem: Find all unique triplets [a, b, c] where a + b + c = 0.

Approach: Sort array, then fix one number and use two pointers for the rest.
  1. Sort nums so duplicates are adjacent and we can skip them easily.
  2. Loop i from 0 to n-3 — nums[i] is the fixed first element of the triplet.
  3. Skip duplicate nums[i] (same value as nums[i-1]) to avoid repeated triplets.
  4. Set l = i+1, r = n-1 — two pointers on the remaining subarray.
  5. While l < r:
       s = nums[i] + nums[l] + nums[r]
       s == 0 → record triplet, skip duplicate l/r values, then l++, r--
       s < 0  → sum too small, need bigger value → l++
       s > 0  → sum too big, need smaller value → r--

Why sorting helps: two pointers only work on a sorted array; duplicates become easy to skip.

Time: O(n²) — O(n log n) sort + O(n) two-pointer pass per i
Space: O(1) extra (excluding output and sort overhead)
"""


def threesum(nums):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        # Skip duplicate first elements — same triplet would be found again
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1  # search pair (l, r) such that nums[i]+nums[l]+nums[r] == 0

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:
                res.append([nums[i], nums[l], nums[r]])

                # Skip duplicate second/third values before moving pointers inward
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1
            elif s < 0:
                l += 1   # sum too small — move left pointer right for a larger value
            else:
                r -= 1   # sum too large — move right pointer left for a smaller value

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threesum(nums))  # [[-1, -1, 2], [-1, 0, 1]]

"""
Sort Colors (Dutch National Flag) — complete logic in one read:

Problem: Sort array of 0s, 1s, and 2s in-place in one pass.
         Final order: all 0s | all 1s | all 2s

Three pointers divide the array into four zones:
  [0 ... low-1]   → already sorted 0s
  [low ... mid-1] → already sorted 1s
  [mid ... high]  → unknown / not yet processed
  [high+1 ... n-1] → already sorted 2s

Algorithm (while mid <= high):
  nums[mid] == 0 → swap with low zone, expand 0s (low++, mid++)
  nums[mid] == 1 → already in middle zone, just scan ahead (mid++)
  nums[mid] == 2 → swap with high zone, shrink unknown from right (high--)
                   (mid stays — swapped value at mid is unprocessed)

Time: O(n) | Space: O(1) | Single pass, in-place swaps only.
"""


def sortColors(nums):
    n = len(nums)
    low = 0          # boundary: next slot for 0
    mid = 0          # current element under inspection
    high = n - 1     # boundary: next slot for 2 (from the right)

    while mid <= high:
        if nums[mid] == 0:
            # 0 belongs in the left zone — swap into [low], advance both pointers
            nums[mid] = nums[low]
            nums[low] = 0
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is already in the correct middle zone — move on
            mid += 1
        else:
            # nums[mid] == 2 — push to right zone; don't advance mid (check swapped value)
            nums[mid] = nums[high]
            nums[high] = 2
            high -= 1

    return nums


nums = [1, 2, 1, 0, 2, 0]
print(sortColors(nums))  # [0, 0, 1, 1, 2, 2]

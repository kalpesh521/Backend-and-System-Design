"""
Move Zeroes — complete logic in one read:

Problem: Move all 0s to the end of the array in-place, keep non-zero order unchanged.

Approach: Two pointers — left (write position) and right (scanner).
  - left  → next slot where a non-zero should go
  - right → scans every index from 0 to n-1

  For each nums[right] != 0:
    Swap nums[left] with nums[right], then left++.
  Non-zeros get packed to the front in original order; zeros drift to the back.

Why swapping works:
  When right finds a non-zero, it swaps into the left slot (which is either
  already correct or holds a zero), then left advances past the placed value.

Time: O(n) | Space: O(1) | Single pass, in-place.
"""


def moveZeroes(nums):
    n = len(nums)
    left = 0  # next index to write a non-zero value

    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


nums = [2, 0, 4, 0, 3]
print(moveZeroes(nums))  # [2, 4, 3, 0, 0]

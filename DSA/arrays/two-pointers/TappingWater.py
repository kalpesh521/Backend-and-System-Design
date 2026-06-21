"""
Trapping Rain Water — complete logic in one read:

Problem: Given elevation map height[], compute total water trapped after rain.
  Water at index i = min(max_left, max_right) - height[i]  (if positive)

Approach: Two pointers from opposite ends + running max on each side.
  left_max  = tallest wall seen from the left so far
  right_max = tallest wall seen from the right so far

  While left < right:
    Process the side with the SMALLER max (that side's water level is bounded by its own max):
      - If left_max < right_max:
          left++
          left_max = max(left_max, height[left])
          water += left_max - height[left]
      - Else:
          right--
          right_max = max(right_max, height[right])
          water += right_max - height[right]

Why process the smaller-max side?
  If left_max < right_max, water at left is limited by left_max only
  (right side already has a taller wall — right_max guarantees enough support).
  Safe to compute trapped water at left without knowing the full right skyline.
  Same logic in reverse when right_max is smaller.

Example: height = [4, 2, 0, 3, 2, 5]
  At index 1 (h=2): left_max=4 → trapped = 4-2 = 2
  At index 2 (h=0): left_max=4 → trapped = 4-0 = 4
  At index 3 (h=3): left_max=4 → trapped = 4-3 = 1
  At index 4 (h=2): left_max=4 → trapped = 4-2 = 2
  Total = 9

Time: O(n) | Space: O(1)
Pattern: Opposite ends (converging pointers) — see Patterns.txt
"""


def trap(height):
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


height = [4, 2, 0, 3, 2, 5]
print(trap(height))  # 9

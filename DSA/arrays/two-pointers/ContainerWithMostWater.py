"""
Container With Most Water — complete logic in one read:

Problem: Given heights of vertical lines, pick two lines to form a container.
  Area = min(height[left], height[right]) * (right - left)
  Return the maximum possible area.

Approach: Two pointers at opposite ends (left = 0, right = n - 1).
  While left < right:
    1. Compute area using the shorter of the two heights (water level is limited by the shorter wall).
    2. Update max_area if this area is larger.
    3. Move the pointer at the SHORTER line inward:
       - If height[left] < height[right]  → left++
       - Else                              → right--

Why move the shorter line?
  Area is limited by min(height[left], height[right]).
  Keeping the shorter line and shrinking width can never beat the current area.
  Moving the shorter line might find a taller wall and a larger area.
  Moving the taller line only reduces width with no height gain — safe to skip.

Example: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Start: left=0 (h=1), right=8 (h=7) → area = 1 * 8 = 8  → move left (shorter)
  ... eventually left=1 (h=8), right=8 (h=7) → area = 7 * 7 = 49  ← answer

Time: O(n) | Space: O(1)
Pattern: Opposite ends (converging pointers) — see Patterns.txt
"""


def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        length = min(height[left], height[right])
        width = right - left
        area = length * width
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1   # shorter left wall — try a taller one
        else:
            right -= 1  # shorter or equal right wall — try a taller one

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # 49

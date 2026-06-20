"""
Two Sum (Two Pointers) — complete logic in one read:

Problem: Find indices [i, j] where num[i] + num[j] == target.
Note: Array must be SORTED for this two-pointer approach to work.

Approach: Place one pointer at the start (i) and one at the end (j).
  While i < j:
    sum = num[i] + num[j]
    sum == target → found pair, return [i, j]
    sum > target  → sum too big, need smaller value → j-- (move right pointer left)
    sum < target  → sum too small, need bigger value → i++ (move left pointer right)

Why it works on sorted array:
  Moving j left always decreases the sum; moving i right always increases it.
  So we never miss the answer by shrinking the search space in one direction.

Time: O(n) | Space: O(1)
(For unsorted arrays, use a hash map instead — O(n) time, O(n) space.)
"""


def two_sum(num, target):
    i = 0
    j = len(num) - 1

    while i < j:
        current_sum = num[i] + num[j]

        if current_sum == target:
            return [i, j]
        elif current_sum > target:
            j -= 1   # sum too large — try a smaller value from the right
        else:
            i += 1   # sum too small — try a larger value from the left

    return []  # no pair found


num = [2, 7, 11, 15]
target = 9
print(two_sum(num, target))  # [0, 1]  → 2 + 7 = 9

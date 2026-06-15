def two_sum(num, target):
  i = 0
  j = len(num) - 1

  while i < j:
    if num[i] + num[j] == target:
      return [i, j]
    elif num[i] + num[j] > target:
      j -= 1
    else:
      i += 1

  return []


num = [2, 7, 11, 15]
target = 9
print(two_sum(num, target))

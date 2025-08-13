arr = [1, 4, 20, 3, 10, 5]
target = 33
curr_sum, start = 0, 0

for end in range(len(arr)):
    curr_sum += arr[end]
    while curr_sum > target:
        curr_sum -= arr[start]
        start += 1
    if curr_sum == target:
        print("Found between indexes", start, "and", end)
        break

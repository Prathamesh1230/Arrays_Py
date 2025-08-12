arr = [3, 3, 4, 2, 3, 3, 5]
candidate, count = None, 0
for num in arr:
    if count == 0:
        candidate, count = num, 1
    elif num == candidate:
        count += 1
    else:
        count -= 1
print("Majority Element:", candidate)

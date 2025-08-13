arr = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print("Second Largest:", second)

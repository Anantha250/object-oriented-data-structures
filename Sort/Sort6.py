def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)
    return merged, inv_left + inv_right + inv_split

def merge(left, right):
    result = []
    i = j = inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv

n = int(input())
arr = list(map(int, input().split()))
_, inversion_count = merge_sort(arr)
print(inversion_count)
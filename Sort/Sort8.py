class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        res = [0] * n
        arr = list(enumerate(nums))
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    right_count += 1
                    merged.append(right[j])
                    j += 1
                else:
                    res[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1
            
            while i < len(left):
                res[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(arr)
        return res
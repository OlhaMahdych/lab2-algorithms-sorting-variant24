def merge_sort_iterative(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            merged = []
            li = ri = 0
            while li < len(left) and ri < len(right):
                comparisons += 1
                if left[li] <= right[ri]:
                    merged.append(left[li])
                    assignments += 1
                    li += 1
                else:
                    merged.append(right[ri])
                    assignments += 1
                    ri += 1
            while li < len(left):
                merged.append(left[li])
                assignments += 1
                li += 1
            while ri < len(right):
                merged.append(right[ri])
                assignments += 1
                ri += 1
            arr[i:i + len(merged)] = merged
        width *= 2
    return arr, comparisons, assignments

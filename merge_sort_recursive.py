def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0

    def merge(left, right):
        nonlocal comparisons, assignments
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                assignments += 1
                i += 1
            else:
                result.append(right[j])
                assignments += 1
                j += 1
        while i < len(left):
            result.append(left[i])
            assignments += 1
            i += 1
        while j < len(right):
            result.append(right[j])
            assignments += 1
            j += 1
        return result

    if len(arr) <= 1:
        return arr, comparisons, assignments
    mid = len(arr) // 2
    left_sorted, _, _ = merge_sort_recursive(arr[:mid])
    right_sorted, _, _ = merge_sort_recursive(arr[mid:])
    merged = merge(left_sorted, right_sorted)
    return merged, comparisons, assignments

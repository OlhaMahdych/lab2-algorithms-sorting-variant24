def partition(a, l, r):
    pivot = a[l]
    i = l - 1
    j = r + 1
    comparisons = 0
    assignments = 0
    while True:
        i += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
        comparisons += 1
        j -= 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
        comparisons += 1
        if i >= j:
            return j, comparisons, assignments
        a[i], a[j] = a[j], a[i]
        assignments += 3

def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    if l < r:
        q, c, a_count = partition(a, l, r)
        comparisons += c
        assignments += a_count
        c1, a1 = quicksort(a, l, q)
        c2, a2 = quicksort(a, q + 1, r)
        comparisons += c1 + c2
        assignments += a1 + a2
    return comparisons, assignments

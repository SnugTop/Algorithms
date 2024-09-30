def SmallestMissing(A, left, right):
    if left > right:
        return left
    mid = (left + right) // 2
    if A[mid] == mid:
        return SmallestMissing(A, mid + 1, right)
    else:
        return SmallestMissing(A, left, mid - 1)

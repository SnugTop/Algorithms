def merge(nums1, m, nums2, n):
    # Set up pointers for nums1 and nums2
    p1 = m - 1  # Pointer for the last element in the initial part of nums1
    p2 = n - 1  # Pointer for the last element in nums2
    p = m + n - 1  # Pointer for the last element in nums1 (including the extra space)

    # Merge in reverse order
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are still elements in nums2, copy them
    nums1[:p2+1] = nums2[:p2+1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

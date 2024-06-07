# Instructions
# Given two sorted arrays num1 and num2 of size m and n respectively, return the median of the two sorted arrays after
# they are merged.
# The overall runtime complexity should be O(log(m+n).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution:
    def __init__(self, num1, num2):
        self.array1 = num1
        self.array2 = num2
        self.sol = self.find_median_sorted_arrays()

    def find_median_sorted_arrays(self):
        array = self.array1 + self.array2
        array.sort()
        if len(array) % 2 == 0:
            return (array[int((len(array)/2) - 1)] + array[int(len(array)/2)])/2
        else:
            return array[round(len(array)/2)]


sol = Solution([1, 2], [3, 4])
print(sol.sol)

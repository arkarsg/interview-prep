#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

from typing import List

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            # O(m + n) solution
            # nums1 = [a_1 ... a_m]
            # nums2 = [b_1 ... b_n]
            res = []
            i, j = 0, 0
            m = len(nums1)
            n = len(nums2)

            while i < m or j < n:
                if i >= m:
                    res.append(nums2[j])
                    j += 1
                    continue
                if j >= n:
                    res.append(nums1[i])
                    i += 1
                    continue

                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            if len(res) % 2 != 0:
                return res[len(res) // 2]
            else:
                mid = int(len(res) / 2)
                return (res[mid] + res[mid-1]) / 2

# A =   [a_1 ... a_m]
# B =   [b_1    ...     b_n]

# total_length = m + n
# let's say the total_length is odd
# median is the (total_length // 2)-th element of a merged array

# Find median of A (m_a) with index i_a and median of B (m_b) at index i_b
# Suppose m_a < m_b
#   1. ignore the right partition of B
#   2. Only need to consider A[i_a:], B[0:i_b]
#   3. Recurse
# Else
#   1. Ignore the right partition of A
#   2. Only need to consider A[0:i_a], B[i_b:]
#   3. Recurse

# A = [1, 2, 3, 5, 6, 7]    median=4
# B = [4]                   median=4

# A = [1, 2, 3]             median=2
# B = [4]                   median=4

# A = [2, 3]                median=2.5
# B = [4]                   median=4



 

# @lc code=end


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
        

# @lc code=end


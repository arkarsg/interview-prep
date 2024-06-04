#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse at pivot
        curr = slow.next
        prev, slow.next = None, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # After reversing the linked list,
        # prev is pointing to the last element of the original linked list
        # Or, in other words, the first element of the reversed linked list
        curr, reversed_curr = head, prev
        # merge
        while reversed_curr:
            tmp_curr = curr.next
            r_tmp_curr = reversed_curr.next
            curr.next = reversed_curr
            reversed_curr.next = tmp_curr
            curr = tmp_curr
            reversed_curr = r_tmp_curr
            
        
# @lc code=end


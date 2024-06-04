#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        if head.next is None:
            return head
 
        curr_node = head
        prev_node = None
        next_node = None

        while curr_node is not None:
            # update node.next
            next_node = curr_node.next
            curr_node.next = prev_node
            # update pointers
            prev_node = curr_node
            curr_node = next_node

        return prev_node

# @lc code=end


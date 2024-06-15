#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        has_carry = False

        node_1 = l1
        node_2 = l2
        
        val = node_1.val + node_2.val
        if val >= 10:
            has_carry = True
        res_head = ListNode(val=val % 10)
        node_ptr = res_head
        
        node_1 = node_1.next
        node_2 = node_2.next
        
        while node_1 or node_2:
            if node_1 and node_2:
                val = node_1.val + node_2.val
                node_1 = node_1.next
                node_2 = node_2.next
            elif node_1 and not node_2:
                val = node_1.val
                node_1 = node_1.next
            else:
                val = node_2.val
                node_2 = node_2.next
                
            if has_carry:
                val += 1
                
            if val >= 10:
                has_carry = True
            else:
                has_carry = False
                
            node_ptr.next = ListNode(val=val % 10)
            node_ptr = node_ptr.next
            
        if has_carry:
            node_ptr.next = ListNode(val=1)
            
        return res_head
        
# @lc code=end


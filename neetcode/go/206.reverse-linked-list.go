/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	currNode := head
	var prevNode *ListNode
	var nextNode *ListNode

	for currNode != nil {
		nextNode = currNode.Next
		currNode.Next = prevNode
		prevNode = currNode
		currNode = nextNode
	}
	return prevNode
}

// @lc code=end


/*
 * @lc app=leetcode id=42 lang=golang
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
func trap(height []int) int {
	n := len(height) - 1
	left := 0
	right := n
	leftMax := height[left]
	rightMax := height[right]
	res := 0

	for left < right {
		if leftMax < rightMax {
			left++
			if height[left] > leftMax {
				leftMax = height[left]
			}
			res += leftMax - height[left]
		} else {
			right--
			if height[right] > rightMax {
				rightMax = height[right]
			}
			res += rightMax - height[right]
		}
	}

	return res
}

// @lc code=end


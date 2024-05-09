/*
 * @lc app=leetcode id=11 lang=golang
 *
 * [11] Container With Most Water
 */

// @lc code=start
func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	maxSoFar := calculateArea(height[left], height[right], right-left)

	for left < right {
		if height[left] < height[right] {
			left++
		} else {
			right--
		}

		if newArea := calculateArea(height[left], height[right], right-left); newArea > maxSoFar {
			maxSoFar = newArea
		}
	}
	return maxSoFar
}

func calculateArea(height1 int, height2 int, length int) int {
	if height1 <= height2 {
		ret := height1 * length
		return ret
	}
	ret := height2 * length
	return ret
}

// @lc code=end


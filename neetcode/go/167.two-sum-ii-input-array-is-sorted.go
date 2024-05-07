/*
 * @lc app=leetcode id=167 lang=golang
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
func twoSum(numbers []int, target int) []int {
	left_ptr, right_ptr := 0, len(numbers)-1

	for left_ptr < right_ptr {
		if numbers[left_ptr]+numbers[right_ptr] == target {
			return []int{left_ptr + 1, right_ptr + 1}
		} else if numbers[left_ptr]+numbers[right_ptr] > target {
			right_ptr--
		} else {
			left_ptr++
		}
	}
	return nil
}

// @lc code=end


/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	hm := make(map[int]int)
	for i, num := range nums {
		remainder := target - num
		if remainder_index, ok := hm[remainder]; ok {
			return []int{i, remainder_index}
		}
		hm[num] = i
	}
	return []int{}
}

// @lc code=end


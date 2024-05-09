/*
 * @lc app=leetcode id=15 lang=golang
 *
 * [15] 3Sum
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	res := [][]int{}
	sort.Ints(nums)

	for i := 0; i < len(nums)-2; i++ {
		if i == 0 || (i > 0 && nums[i] != nums[i-1]) {
			start := i + 1
			end := len(nums) - 1
			target := -1 * nums[i]

			for start < end {
				if nums[start]+nums[end] == target {
					res = append(res, []int{nums[i], nums[start], nums[end]})

					for start < end && nums[start] == nums[start+1] {
						start++
					}
					for start < end && nums[end] == nums[end-1] {
						end--
					}
					start++
					end--
				} else if nums[start]+nums[end] > target {
					end--
				} else {
					start++
				}
			}
		}
	}
	return res
}

// @lc code=end


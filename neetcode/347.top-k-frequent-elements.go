/*
 * @lc app=leetcode id=347 lang=golang
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
import "sort"

func topKFrequent(nums []int, k int) []int {
	hm := make(map[int]int, len(nums))
	res := make([]int, 0, k)
	// create key : count map
	for _, num := range nums {
		hm[num]++
	}

	counts := make([]int, 0, len(hm))
	for _, c := range hm {
		counts = append(counts, c)
	}

	sort.Ints(counts)
	min := counts[len(counts)-k]
	for num, count := range hm {
		if count >= min {
			res = append(res, num)
		}
	}
	return res
	//
}

// @lc code=end


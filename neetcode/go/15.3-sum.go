/*
 * @lc app=leetcode id=15 lang=golang
 *
 * [15] 3Sum
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	res := [][]int{}
	numMap := make(map[[3]int]bool)
	positives := make([]int, 0, len(nums))
	negatives := make([]int, 0, len(nums))
	zeroes := make([]int, 0, len(nums))

	for _, num := range nums {
		if num < 0 {
			negatives = append(negatives, num)
		} else if num > 0 {
			positives = append(positives, num)
		} else {
			zeroes = append(zeroes, num)
		}
	}

	p_lookup := make(map[int]bool)
	n_lookup := make(map[int]bool)

	for _, num := range positives {
		p_lookup[num] = true
	}

	for _, num := range negatives {
		n_lookup[num] = true
	}

	if len(zeroes) > 0 {
		if len(zeroes) >= 3 {
			res = append(res, []int{0, 0, 0})
		}

		for num, _ := range p_lookup {
			negNum := -1 * num
			if _, ok := n_lookup[negNum]; ok {
				res = append(res, []int{negNum, 0, num})
			}
		}
	}

	sort.Ints(negatives)

	for i := 0; i < len(negatives); i++ {
		for j := i + 1; j < len(negatives); j++ {
			posNum := -1 * (negatives[i] + negatives[j])
			if _, ok := p_lookup[posNum]; ok {
				sum := []int{negatives[i], negatives[j], posNum}
				sort.Ints(sum)
				numMap[[3]int{sum[0], sum[1], sum[2]}] = true
			}

		}
	}

	sort.Ints(positives)

	for i := 0; i < len(positives); i++ {
		for j := i + 1; j < len(positives); j++ {
			negNum := -1 * (positives[i] + positives[j])
			if _, ok := n_lookup[negNum]; ok {
				sum := []int{negNum, positives[i], positives[j]}
				sort.Ints(sum)
				numMap[[3]int{sum[0], sum[1], sum[2]}] = true
			}
		}
	}

	for k, _ := range numMap {
		res = append(res, []int{k[0], k[1], k[2]})
	}

	return res
}

// @lc code=end


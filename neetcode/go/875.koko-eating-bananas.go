/*
 * @lc app=leetcode id=875 lang=golang
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
func minEatingSpeed(piles []int, h int) int {
	CanFinish := func(speed int) bool {
		timeTaken := 0
		for _, numBananas := range piles {
			if numBananas%speed != 0 {
				timeTaken += (numBananas / speed) + 1
			} else {
				timeTaken += numBananas / speed
			}
		}
		return timeTaken <= h
	}

	low := 1
	high := slices.Max(piles)

	for low < high {
		mid := low + (high-low)/2
		if CanFinish(mid) {
			high = mid
		} else {
			low = mid + 1
		}
	}

	return high
}

// @lc code=end


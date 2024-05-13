/*
 * @lc app=leetcode id=853 lang=golang
 *
 * [853] Car Fleet
 */

// @lc code=start
func carFleet(target int, position []int, speed []int) int {
	positionSpeedMap := make(map[int]int, len(position))
	for i := 0; i < len(position); i++ {
		positionSpeedMap[position[i]] = speed[i]
	}

	sort.Slice(position, func(i, j int) bool {
		return position[i] > position[j]
	})

	var stack = []float64{}

	for _, pos := range position {
		timeTaken := float64(target-pos) / float64(positionSpeedMap[pos])
		n := len(stack)
		if n == 0 || stack[n-1] < timeTaken {
			stack = append(stack, timeTaken)
		}
	}
	return len(stack)
}

// @lc code=end
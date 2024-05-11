/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {
	parenPair := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}

	stack := []rune{}
	for _, paren := range s {
		if _, ok := parenPair[paren]; ok {
			stack = append(stack, paren)
			continue
		}

		last := len(stack) - 1
		if last < 0 || paren != parenPair[stack[last]] {
			return false
		}
		stack = stack[:last]
	}
	return len(stack) == 0
}

// @lc code=end


/*
 * @lc app=leetcode id=22 lang=golang
 *
 * [22] Generate Parentheses
 */

// @lc code=start
func dfs(openers int, closers int, valid string, res *[]string) {
	if openers == 0 && closers == 0 {
		*res = append(*res, valid)
		return
	}

	if openers > 0 {
		dfs(openers-1, closers, valid+"(", res)
	}

	if closers > openers {
		dfs(openers, closers-1, valid+")", res)
	}
}

func generateParenthesis(n int) []string {
	openers := n
	closers := n
	var res []string

	dfs(openers, closers, "", &res)
	return res
}

// @lc code=end


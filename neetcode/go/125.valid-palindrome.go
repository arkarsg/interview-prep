/*
 * @lc app=leetcode id=125 lang=golang
 *
 * [125] Valid Palindrome
 */

// @lc code=start
import (
	str "strings"
	r "regexp"
)

func isPalindrome(s string) bool {
	alnum := r.MustCompile("^[a-z0-9]*$")

	isAlnum := func(char rune) bool {
		return alnum.MatchString(string(char))
	}

	filter := func(ss string, predicate func(rune) bool) string {
		var sb str.Builder
		for _, s := range ss {
			if predicate(s) {
				sb.WriteRune(s)
			}
		}
		return sb.String()
	}

	s = str.ToLower(s)
	s = filter(s, isAlnum)
	leftPtr := 0
	rightPtr := len(s) - 1
	for leftPtr < rightPtr {
		if s[leftPtr] == s[rightPtr] {
			leftPtr++
			rightPtr--
			continue
		} else {
			return false
		}
	}
	return true
}

// @lc code=end


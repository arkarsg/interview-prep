/*
 * @lc app=leetcode id=155 lang=golang
 *
 * [155] Min Stack
 */

// @lc code=start
type MinStack struct {
	stack []int
	aux   []int
}

func Constructor() MinStack {
	minStack := MinStack{
		stack: []int{},
		aux:   []int{},
	}
	return minStack
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	nAux := len(this.aux)
	if nAux == 0 || val <= this.GetMin() {
		this.aux = append(this.aux, val)
	}
}

func (this *MinStack) Pop() {
	n := len(this.stack)
	nAux := len(this.aux)
	popped := this.stack[n-1]
	if popped == this.aux[nAux-1] {
		this.aux = this.aux[:nAux-1]
	}
	this.stack = this.stack[:n-1]
}

func (this *MinStack) Top() int {
	n := len(this.stack)
	return this.stack[n-1]
}

func (this *MinStack) GetMin() int {
	n := len(this.aux)
	return this.aux[n-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end


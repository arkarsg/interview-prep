package twitter

import "container/heap"

var TIMESTAMP int = 0

type Tweet struct {
	ID    int
	Time  int
	Next  *Tweet
	index int
}

type User struct {
	ID        int
	Following map[int]bool
	Head      *Tweet
}

func CreateUser(id int) User {
	u := User{
		ID:        id,
		Following: make(map[int]bool),
		Head:      nil,
	}
	u.follow(id)
	return u
}

func (u *User) follow(userId int) {
	u.Following[userId] = true
	return
}

func (u *User) unfollow(userId int) {
	// a user is not allowed to unfollow him/herself
	if userId != u.ID {
		delete(u.Following, userId)
	}
}

func (u *User) createPost(postId int) {
	tweet := Tweet{
		ID:   postId,
		Time: TIMESTAMP,
	}
	TIMESTAMP++

	tweet.Next = u.Head
	u.Head = &tweet
}

type Twitter struct {
	users map[int]*User
}

func Constructor() Twitter {
	return Twitter{
		users: make(map[int]*User),
	}
}

func (this *Twitter) createUserIfNotExists(userId int) {
	if _, ok := this.users[userId]; !ok {
		u := CreateUser(userId)
		this.users[userId] = &u
	}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
	this.createUserIfNotExists(userId)
	usr, _ := this.users[userId]
	usr.createPost(tweetId)
}

func (this *Twitter) Follow(followerId int, followeeId int) {
	this.createUserIfNotExists(followerId)
	this.createUserIfNotExists(followeeId)

	this.users[followerId].follow(followeeId)
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
	if usr, ok := this.users[followerId]; ok {
		usr.unfollow(followeeId)
	}
}

func (this *Twitter) GetNewsFeed(userId int) []int {
	var res []int
	var feedUser User

	if user, ok := this.users[userId]; ok {
		feedUser = *user
	} else {
		return []int{}
	}
	users := feedUser.Following
	pq := make(TweetPriorityQueue, 0, len(users))
	heap.Init(&pq)

	for k := range users {
		tweetHead := this.users[k].Head
		if tweetHead == nil {
			continue
		}
		heap.Push(&pq, tweetHead)
	}

	for pq.Len() > 0 {
		if len(res) >= 10 {
			break
		}
		twt := heap.Pop(&pq).(*Tweet)
		res = append(res, twt.ID)
		if twt.Next != nil {
			heap.Push(&pq, twt.Next)
		}
	}
	return res
}

type TweetPriorityQueue []*Tweet

func (pq TweetPriorityQueue) Len() int { return len(pq) }

func (pq TweetPriorityQueue) Less(i, j int) bool {
	return pq[i].Time > pq[j].Time
}

func (pq TweetPriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *TweetPriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Tweet)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *TweetPriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

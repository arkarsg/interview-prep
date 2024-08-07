package twitter

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */
func TestLeetCodeTestCase(t *testing.T) {
	twitter := constructTwitter(t)
	twitter.PostTweet(1, 5)
	feed := twitter.GetNewsFeed(1)
	assert.Equal(t, []int{5}, feed)

	twitter.Follow(1, 2)
	twitter.PostTweet(2, 6)
	feed = twitter.GetNewsFeed(1)
	assert.Equal(t, []int{6, 5}, feed)

	twitter.Unfollow(1, 2)
	feed = twitter.GetNewsFeed(1)
	assert.Equal(t, []int{5}, feed)
}
func constructTwitter(t *testing.T) Twitter {
	return Constructor()
}

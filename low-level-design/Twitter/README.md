# Design Twitter
Leetcode #355

**Key skills**
- OOP
- Linked Lists
- Priority Queue

---

**Requirements**
- Users should be able to follow/unfollow other users
- Users should be able to see their own posts
- Users should be able to see posts of users they are following
  - In **sorted** descending order by time of post

---

**Datastructure help**
- Store each user's own tweets in a linked list sorted by timestamp
- If some user follows *k* other users, combine the *k* ordered linked list.
- Maintain the sorted order with a priority queue.

---

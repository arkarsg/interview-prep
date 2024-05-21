package org.arkar.cache;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

public class LruEviction<Key> {
    // data structure
    private final Set<Key> set;
    private final Deque<Key> dq;
    // update key

    public LruEviction() {
        this.set = new HashSet<>();
        this.dq = new ArrayDeque<>();
    }
    public void updateKey(Key key) {
        if (!set.contains(key)) {
            set.add(key);
            dq.addLast(key);
        } else {
            dq.remove(key);
            dq.addLast(key);
        }
    }
    // evict key
    public Key evictKey() {
        if (this.dq.size() == 0) {
            return null;
        }
        Key evicted = dq.getFirst();
        dq.removeFirst();
        return evicted;
    }

    public void displayEvictionOrder() {
        dq.forEach(System.out::println);
    }
}

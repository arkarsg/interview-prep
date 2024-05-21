package org.arkar.cache;

import org.arkar.cache.exceptions.KeyNotFoundException;
import org.arkar.cache.exceptions.StorageFullException;


public class Cache<Key, Value> {
    private final Storage<Key, Value> storage;
    private final LruEviction<Key> policy;

    public Cache(Storage<Key, Value> storage) {
        this.storage = storage;
        this.policy = new LruEviction<>();
    }

    public void set(Key key, Value value) {
        try {
            this.storage.add(key, value);
            this.policy.updateKey(key);
        } catch (StorageFullException e) {
            Key evicted = this.policy.evictKey();
            this.storage.remove(evicted);
            this.set(key, value);
        }
    }

    public Value get(Key key) {
        // get from storage if exists, then update key
        try {
            Value value = this.storage.get(key);
            this.policy.updateKey(key);
            return value;
        } catch (KeyNotFoundException e) {
            return null;
        }
    }

    public void display() {
        this.policy.displayEvictionOrder();
    }
}

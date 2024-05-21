package org.arkar.cache;

import org.arkar.cache.exceptions.KeyNotFoundException;
import org.arkar.cache.exceptions.StorageFullException;

import java.util.HashMap;
import java.util.Map;

public class KeyValueStorage<Key, Value> implements Storage<Key, Value> {
    private final Map<Key, Value> storage;
    private final Integer capacity;

    public KeyValueStorage(Integer capacity) {
        this.capacity = capacity;
        storage = new HashMap<>();
    }

    private boolean isStorageFull() {
        return this.storage.size() == this.capacity;
    }
    @Override
    public void add(Key key, Value value) {
        if (!this.isStorageFull()) {
            this.storage.put(key, value);
        } else {
            throw new StorageFullException("Storage is full");
        }
    }

    @Override
    public void remove(Key key) {
        if (this.storage.containsKey(key)) {
            this.storage.remove(key);
        } else {
            throw new KeyNotFoundException("Key does not exist in storage");
        }

    }

    @Override
    public Value get(Key key) {
        if (this.storage.containsKey(key)) {
            return this.storage.get(key);
        } else {
            throw new KeyNotFoundException("Key does not exist in storage");
        }
    }

    @Override
    public void display() {
        this.storage.forEach((key, value) -> {
            System.out.println("Key=" + key + ", Value=" + value);
        });
    }
}

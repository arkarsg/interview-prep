package org.arkar.cache;

import org.arkar.cache.exceptions.KeyNotFoundException;
import org.arkar.cache.exceptions.StorageFullException;

public interface Storage<Key, Value> {
    public void add(Key key, Value value) throws StorageFullException;
    void remove(Key key) throws KeyNotFoundException;
    Value get(Key key) throws KeyNotFoundException;
    void display();
}

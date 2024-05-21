package org.arkar;

import org.arkar.cache.Cache;
import org.arkar.cache.KeyValueStorage;
import org.arkar.cache.Storage;

public class Main {
    public static void main(String[] args) {
        Integer capacity = 4;
        Storage<Integer, String> storage = new KeyValueStorage<>(capacity);
        Cache<Integer, String> lruCache = new Cache<>(storage);

        System.out.println("Initialising cache with 4 elements: Capacity:" + capacity);
        lruCache.set(1, "a");
        lruCache.set(2, "b");
        lruCache.set(3, "c");
        lruCache.set(4, "d");
        lruCache.display();

        System.out.println("Adding to full storage. Capacity:" + capacity);
        lruCache.set(5, "e");
        lruCache.display();

        System.out.println("Updating key in cache. Capacity:" + capacity);
        lruCache.get(2);
        lruCache.display();
    }
}
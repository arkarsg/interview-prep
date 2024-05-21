package org.arkar.cache;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LruEvictionTest {

    private LruEviction<String> lruEviction;

    @BeforeEach
    void setUp() {
        lruEviction = new LruEviction<>();
    }

    @Test
    void testUpdateKeyNewKey() {
        lruEviction.updateKey("key1");
        lruEviction.updateKey("key2");
        lruEviction.updateKey("key3");

        // The deque should contain key1, key2, key3 in order
        assertEquals("key1", lruEviction.evictKey());
        assertEquals("key2", lruEviction.evictKey());
        assertEquals("key3", lruEviction.evictKey());
    }

    @Test
    void testUpdateKeyExistingKey() {
        lruEviction.updateKey("key1");
        lruEviction.updateKey("key2");
        lruEviction.updateKey("key3");
        lruEviction.updateKey("key2"); // key2 should move to the end

        // The deque should contain key1, key3, key2 in order
        assertEquals("key1", lruEviction.evictKey());
        assertEquals("key3", lruEviction.evictKey());
        assertEquals("key2", lruEviction.evictKey());
    }

    @Test
    void testEvictKey() {
        lruEviction.updateKey("key1");
        lruEviction.updateKey("key2");
        lruEviction.updateKey("key3");

        // Evict the keys and check the order
        assertEquals("key1", lruEviction.evictKey());
        assertEquals("key2", lruEviction.evictKey());
        assertEquals("key3", lruEviction.evictKey());
    }

    @Test
    void testEvictKeyFromEmptyDeque() {
        assertNull(lruEviction.evictKey());
    }

    @Test
    void testUpdateKeyOrder() {
        lruEviction.updateKey("key1");
        lruEviction.updateKey("key2");
        lruEviction.updateKey("key3");
        lruEviction.updateKey("key1"); // key1 should move to the end
        lruEviction.updateKey("key2"); // key2 should move to the end

        // The deque should contain key3, key1, key2 in order
        assertEquals("key3", lruEviction.evictKey());
        assertEquals("key1", lruEviction.evictKey());
        assertEquals("key2", lruEviction.evictKey());
    }
}

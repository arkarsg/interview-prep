package org.arkar.cache;

import org.arkar.cache.exceptions.KeyNotFoundException;
import org.arkar.cache.exceptions.StorageFullException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.*;

import static org.junit.jupiter.api.Assertions.*;

class CacheTest {
    private Storage<String, String> s;
    private Cache<String, String> c;

    @BeforeEach
    void setUp() {
        s = mock(Storage.class);
        c = new Cache<>(s);
    }

    @Test
    void testSetAndGetKey() {
        doNothing().when(s).add("hello", "world");
        when(s.get("hello")).thenReturn("world");

        c.set("hello", "world");
        assertEquals("world", c.get("hello"));
        verify(s, times(1)).add("hello", "world");
        verify(s, times(1)).get("hello");
    }

    @Test
    void testGetKeyNotFound() {
        when(s.get("key1")).thenThrow(new KeyNotFoundException("Key not found"));

        assertNull(c.get("key1"));
        verify(s, times(1)).get("key1");
    }
}
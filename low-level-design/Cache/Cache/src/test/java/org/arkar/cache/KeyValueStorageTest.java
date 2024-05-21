package org.arkar.cache;

import java.security.Key;

import static org.junit.jupiter.api.Assertions.*;

class KeyValueStorageTest {

    private KeyValueStorage<Integer, Integer> sut;
    @org.junit.jupiter.api.BeforeEach
    void setUp() {
        sut = new KeyValueStorage<Integer, Integer>(3);
    }

    @org.junit.jupiter.api.Test
    void testAddElement() {
        sut.add(1, 1);
        assertEquals(1, sut.get(1));
    }

    @org.junit.jupiter.api.Test
    void testAddElementWhenFull() {
        sut.add(1, 1);
        sut.add(2, 2);
        sut.add(3, 3);
        sut.add(4, 4);
        assertNull(sut.get(4));
    }

    @org.junit.jupiter.api.Test
    void testRemove() {
        sut.add(1, 1);
        sut.remove(1);
        assertNull(sut.get(1));
    }

    @org.junit.jupiter.api.Test
    void testGet() {
        sut.add(1, 1);
        assertEquals(1, sut.get(1));
    }
}
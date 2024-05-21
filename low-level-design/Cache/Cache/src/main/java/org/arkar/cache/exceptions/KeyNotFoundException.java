package org.arkar.cache.exceptions;

public class KeyNotFoundException extends RuntimeException {
    public KeyNotFoundException(String msg) {
        super(msg);
    }
}

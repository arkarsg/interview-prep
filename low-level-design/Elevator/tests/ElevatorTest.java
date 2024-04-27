import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ElevatorTest {
    private Elevator elevator;
    private final int LOWEST_FLOOR = -1;
    private final int HIGHEST_FLOOR = 5;

    @BeforeEach
    public void setUp() {
        elevator = new Elevator(LOWEST_FLOOR, HIGHEST_FLOOR);
    }

    @Test
    public void testElevatorMovesUp() {
        elevator.move(3);
        assertEquals(elevator.getCurrentFloor(), 3);
    }

    @Test
    public void testElevatorDoesNotMoveBeyondMax() {
        assertThrows(IllegalArgumentException.class, () -> elevator.move(HIGHEST_FLOOR + 1));
    }
}
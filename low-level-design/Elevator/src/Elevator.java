public class Elevator {
    private int currentFloor;
    private final int lowestFloor;
    private final int maxFloor;

    public Elevator(int lowestFloor, int maxFloor) {
        this.currentFloor = lowestFloor;
        this.lowestFloor = lowestFloor;
        this.maxFloor = maxFloor;
    }

    public int getCurrentFloor() {
        return this.currentFloor;
    }

    public void move(int destinationFloor) throws IllegalArgumentException {
        if (destinationFloor < this.lowestFloor || destinationFloor > this.maxFloor) {
            throw new IllegalArgumentException();
        }
        this.currentFloor = destinationFloor;
    }
}

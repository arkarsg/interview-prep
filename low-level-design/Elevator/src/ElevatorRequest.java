public class ElevatorRequest {
    private int requestFloor;
    private int destinationFloor;
    private Direction direction;


    private ElevatorRequest(int requestFloor, int destinationFloor, Direction direction) {
        this.requestFloor = requestFloor;
        this.destinationFloor = destinationFloor;
        this.direction = direction;
    }

    public ElevatorRequest makeRequest(int requestFloor, int destinationFloor) {
        Direction direction = destinationFloor > requestFloor ? Direction.UP : Direction.DOWN;
        return new ElevatorRequest(requestFloor, destinationFloor, direction);
    }
}

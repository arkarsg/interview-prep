public class ElevatorController {
    private Elevator model;
    private ElevatorRequest[] requests;

    public ElevatorController(Elevator model) {
        this.model = model;
        this.requests = new ElevatorRequest[10];
    }

    public void runElevator() {
        for (int i = 0; i < requests.length; i++) {
            ElevatorRequest request = requests[i];

        }
    }
}

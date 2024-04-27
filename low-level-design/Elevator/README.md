A typical lift has buttons(Elevator buttons) inside the cabin to let the user who got in the lift to select his/her desired floor.

Similarly each floor has buttons (Floor buttons) to summon the lift to go floors above and floor below respectively.

## Use cases
### Elevator
- Moves up/down as per instruction
- Each button press results in an elevator request which has to be served.
- Each of these requests is tracked at a global place.
- `ElevatorRequests`, the class which stores elevator requests can use different strategies to schedule the elevator requests
- The elevator is controlled by a controller class which we call `ElevatorController`

The elevator controller instructs the elevator what to do and also can shutdown/start up the elevator of the building. The elevator controller reads the next elevator request to be processed and serves it.

from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
from typing import List

class ServoPosition:
    def __init__(self, servo_id: int, position: int):
        self.servo_id = servo_id
        self.position = position

class ServoBus:
    """Class to control an entire servo bus at once."""

    def __init__(
            self,
            port: str,
            leader_id: int,
            pre_existing_servo_ids: List[int],
    ):
        """
        :param leader_id: The id of the leader servo.
        :param pre_existing_servo_ids: The ids of the servos in the bus.
        """
        self.leader_id = leader_id
        self.servo_ids = pre_existing_servo_ids
        self.port = port

# TODO: create a connection for the servo bus, handle connection and teardown gracefully


    def get_bus_position(self, servo_bus: ServoBusCommunication) -> List[ServoPosition]:
        """Return the list of the servo positions."""
        positions = []
        for servo in self.servo_ids:
            servo_pos = servo_bus.pos_read(servo)
            positions.append(ServoPosition(servo, servo_pos))
        return positions
    

    def set_bus_position(self, positions: List[ServoPosition], servo_bus: ServoBusCommunication) -> None:
        """Set the position for all the servos in the bus."""
        for servo in self.servo_ids:
            servo_bus.pos_set(servo, positions[servo])

    




        

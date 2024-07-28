from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
from typing import List, Dict

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


    def get_bus_position(self, servo_bus: ServoBusCommunication) -> Dict[int, int]:
        """
        Return the list of the servo positions.

        :return: A dictionary containing user information. keys are servo_id, values are position.
        :rtype: dict
        """
        positions = {}
        for servo in self.servo_ids:
            servo_pos = servo_bus.pos_read(servo)
            positions[servo] = servo_pos
        return positions
    

    def set_bus_position(self, positions: List[ServoPosition], servo_bus: ServoBusCommunication, time_s: int) -> None:
        """Set the position for all the servos in the bus."""
        for desired_position in positions:
            servo_bus.pos_set(desired_position.servo_id, desired_position.position, time_s)

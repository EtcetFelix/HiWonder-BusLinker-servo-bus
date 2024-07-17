from lewansoul_servo_bus import ServoBusCommunication
from typing import List

class ServoPosition:
    servo_id: int
    position: int

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


    def get_bus_position(self) -> List[ServoPosition]:
        """Return the list of the servo positions."""
        positions = []
        with ServoBusCommunication(port=self.port, on_enter_power_on=True) as servo_bus:
            for servo in self.servo_ids:
                positions.append(servo_bus.pos_read(servo))
        return positions


    




        

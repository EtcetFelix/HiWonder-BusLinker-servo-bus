import pytest

from hiwonderbuslinker.bus_control import ServoBus, ServoPosition

@pytest.fixture
def bus():
    return ServoBus('COM5', 1, [1, 2, 3])

def test_class_instantiation(bus):
    assert bus.leader_id == 1
    assert bus.servo_ids == [1, 2, 3]
    assert bus.port == 'COM5'

def test_servo_position_instantiation():
    position = ServoPosition(servo_id=1, position=10)
    assert position.servo_id == 1
    assert position.position == 10

def test_get_bus_position_returns_dictionary_object(bus, mocker):
    mock_servo_bus = mocker.Mock()
    mock_servo_bus.pos_read.return_value = 200

    positions = bus.get_bus_position(mock_servo_bus)
    assert isinstance(positions, dict)
    for servo_id in positions:
        assert isinstance(positions[servo_id], int)


def test_get_bus_position_returns_correct_length_of_position_objects(bus, mocker):
    mock_servo_bus = mocker.Mock()
    mock_servo_bus.pos_read.return_value = 200
    positions = bus.get_bus_position(mock_servo_bus)
    assert len(positions) == 3

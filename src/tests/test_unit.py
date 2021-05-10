import pytest
from characters import unit


@pytest.fixture
def create_unit():
    tester = unit.Unit()
    tester.move_speed = 1
    tester.x_pos = 5
    tester.y_pos = 5
    return tester


def test_set_destination(create_unit):
    create_unit.set_destination((4,6))
    assert create_unit.dest[0][0] == 4
    assert create_unit.dest[0][1] == 6


def test_move_none(create_unit):
    # Test No Movement
    create_unit.set_destination((5,5))
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 5

def test_move_square(create_unit):
    # Test Directly Up
    create_unit.set_destination((5,3))
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 4
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 3

    # Test Directly Down
    create_unit.set_destination((5,6))
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 4
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 5
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 6

    # Test Directly Left
    create_unit.set_destination((3,6))
    create_unit.move()
    assert create_unit.x_pos == 4
    assert create_unit.y_pos == 6
    create_unit.move()
    assert create_unit.x_pos == 3
    assert create_unit.y_pos == 6

    # Test Directly Right
    create_unit.set_destination((6,6))
    create_unit.move()
    assert create_unit.x_pos == 4
    assert create_unit.y_pos == 6
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 6
    create_unit.move()
    assert create_unit.x_pos == 6
    assert create_unit.y_pos == 6


def test_move_diag(create_unit):
    create_unit.set_destination((7,7))
    create_unit.move()
    assert create_unit.x_pos < 7
    assert create_unit.y_pos < 7
    assert create_unit.x_pos > 5
    assert create_unit.y_pos > 5
    create_unit.move()
    assert create_unit.x_pos < 7
    assert create_unit.y_pos < 7
    assert create_unit.x_pos > 5
    assert create_unit.y_pos > 5
    create_unit.move()
    assert create_unit.x_pos == 7
    assert create_unit.y_pos == 7


def test_move_sequence(create_unit):
    create_unit.set_destination((5,6))
    create_unit.set_destination((6,6))
    create_unit.set_destination((6,7))
    create_unit.set_destination((3,7))
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 6
    create_unit.move()
    assert create_unit.x_pos == 6
    assert create_unit.y_pos == 6
    create_unit.move()
    assert create_unit.x_pos == 6
    assert create_unit.y_pos == 7
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 7
    create_unit.move()
    assert create_unit.x_pos == 4
    assert create_unit.y_pos == 7
    create_unit.move()
    assert create_unit.x_pos == 3
    assert create_unit.y_pos == 7
    create_unit.move()
    assert create_unit.x_pos == 3
    assert create_unit.y_pos == 7

def test_move_short(create_unit):
    create_unit.set_destination((5,5.1))
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 5.1

def test_clear_dest(create_unit):
    create_unit.set_destination((7,2))
    create_unit.set_destination((9,4))
    create_unit.clear_destination()
    create_unit.move()
    assert create_unit.x_pos == 5
    assert create_unit.y_pos == 5

import pytest

# тесты tuple
def test_tuple_length():
    t = (1, 2, 3, 4)
    assert len(t) == 4

def test_tuple_access():
    t = (1, 2, 3, 4)
    assert t[0] == 1
    assert t[1] == 2
    assert t[2] == 3
    assert t[3] == 4

@pytest.mark.parametrize("input_data", [(1, 2, 3, 4), ("a", "b", "c"), (True, False, False)])
def test_create_tuple(input_data):
    t = input_data
    assert isinstance(t, tuple)


# тесты set
def test_set_add():
    s = {1, 2, 3}
    s.add(4)
    assert 4 in s

def test_set_intersection():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    assert s1.intersection(s2) == {3}

def test_set_contains_empty():
    s = set()
    try:
        assert 1 in s
    except AssertionError:
        pass



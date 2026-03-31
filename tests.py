import pytest
from heroes import get_tallest_hero

@pytest.mark.parametrize(
    'gender, work',
    [
        ('Male', True),
        ('Male', False),
        ('Female', True),
        ('Female', False),
        ('-', True),
        ('-', False)
    ]
)
def test_valid_inputs(gender, work):
    result = get_tallest_hero(gender, work)
    assert isinstance(result, str)
    assert result.split()[1] == 'cm'


@pytest.mark.parametrize(
    'gender, work',
    [
        ('', True),
        ('', ''),
        ('Female', 123),
        (123, True),
        ('FEMALE', False),
        ('female', False),
        ('female', 'female'),
        ('Male ', True),
        (' Male', True),
        ('123', True),
        ([123,123], {'key': 'value'}),
        ({'key': 'value'}, [123,123]),
        (False, False),
        (True, True)
    ]
)
def test_invalid_inputs(gender, work):
    with pytest.raises(KeyError):
        result = get_tallest_hero(gender, work)

def test_int_as_bool():
    with pytest.raises(KeyError):
        get_tallest_hero('Male', 1)
        get_tallest_hero('Male', 0)

def test_missing_arguments():
    with pytest.raises(TypeError):
        get_tallest_hero('Male')

def test_extra_arguments():
    with pytest.raises(TypeError):
        get_tallest_hero('Male', True, 123)
    



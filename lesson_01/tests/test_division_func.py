from lesson_01.utils import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (10, 5, 2),
                                                   ])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('a, b, expected_result', [(10, 0, 5),
                                                   ])
def test_zero_division(a, b, expected_result):
    with pytest.raises(ZeroDivisionError):
        division(a, b)


@pytest.mark.parametrize('a, b, expected_result', [(10, 'a', 5),
                                                   ])
def test_type_error(a, b, expected_result):
    with pytest.raises(TypeError):
        division(a, b)


@pytest.mark.parametrize('expected_error, devider, divisionable', [(ZeroDivisionError, 0, 10),
                                                                   (TypeError, 'b', 20)
                                                                   ])
def test_division_with_error(expected_error, devider, divisionable):
    with pytest.raises(expected_error):
        division(divisionable, devider)

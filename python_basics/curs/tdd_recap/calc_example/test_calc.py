import pytest

from calc import Calc

# test pentru metoda add
def test_add():
    calc = Calc(10, 5)
    assert calc.add() == 15

# test pentru metoda sub, cu reverse=False
def test_sub_normal():
    calc = Calc(10, 5)
    assert calc.sub() == 5

# test pentru metoda sub, cu reverse=True
def test_sub_reverse():
    calc = Calc(10, 5)
    assert calc.sub(reverse=True) == -5

@pytest.mark.parametrize(
    "a, b, reverse, expected",
    [
        (10, 5, False, 5),  # normal subtraction: 10 - 5
        (10, 5, True, -5),  # reverse subtraction: 5 - 10
        (7, 2, False, 5),  # normal subtraction: 7 - 2
        (7, 2, True, -5),  # reverse subtraction: 2 - 7
    ]
)
def test_sub_parametrized(a, b, reverse, expected):
    calc = Calc(a, b)
    assert calc.sub(reverse=reverse) == expected

# test pentru metoda mul
def test_mul():
    calc = Calc(10, 5)
    assert calc.mul() == 50

# test pentru div, reverse=False
def test_div_normal():
    calc = Calc(10, 5)
    assert calc.div() == 2

# test pentru div, reverse=True
def test_div_reverse():
    calc = Calc(10, 5)
    assert calc.div(reverse=True) == 0.5

# test pentru div in cazul in care impartim la 0
# -> vrem sa testam ca apare exepctia ZeroDivisionError
def test_div_by_zero():
    calc = Calc(10, 0)
    with pytest.raises(ZeroDivisionError):
        calc.div()

    calc_rev = Calc(0, 10)
    with pytest.raises(ZeroDivisionError):
        calc_rev.div(reverse=True)

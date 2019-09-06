# flake8: noqa

def my_sum(first, second):
    return first + second


def my_mult(first, second):
    return first * second


def my_div(first, second):
    return first / second


def test_sum():
    assert my_sum(1, 2) == 3
    assert round(my_sum(2.1, 4.2), 2) == 6.3


def test_mult():
    assert my_mult(2, 2) == 4
    assert my_mult(1, 1) == 1
    assert my_mult(197, 0) == 0
    assert my_mult(6, 4) == 24
    assert my_mult(-6, 4) == -24
    assert my_mult(6, -4) == -24
    assert my_mult(-6, -4) == 24
    assert my_mult(float('nan'), 1)


def test_div():
    assert my_div(1, 1) == 1.0
    assert isinstance(my_div(1, 1), float)
    assert my_div(5, 2) == 2.5
    assert my_div(6, 2) == 3.0

    try:
        my_div(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False


if __name__ == '__main__':
    tests = [
        globals()[variable]
        for variable in globals()
        if variable.startswith('test_')
    ]
    for test in tests:
        try:
            test()
        except AssertionError:
            print('Failed test: ', test.__name__)
            raise

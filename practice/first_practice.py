def is_positive(input_function=input):
    return int(
        input_function('Your number:')
    ) > 0


def test_is_positive():
    assert is_positive(lambda _: 1)
    assert is_positive(lambda _: -1) is False

if __name__ == '__main__':
    test_is_positive()

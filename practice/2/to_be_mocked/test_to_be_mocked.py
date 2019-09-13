# -*- coding: utf-8 -*-

import to_be_mocked


def _fake_input(to_return: str):
    def factory(text_to_show: str) -> str:
        return to_return
    return factory


def _fake_print(ensure_printed: str):
    def factory(username, *args, **kwargs):
        assert username == ensure_printed
    return factory


def test_main():
    """Tests that our main function works correctly."""
    to_be_mocked.input = _fake_input('Nikita')  # Ugly!
    to_be_mocked.print = _fake_print('Nikita')
    to_be_mocked.main()


if __name__ == '__main__':
    test_main()
    print('Done!')  # noqa: T001

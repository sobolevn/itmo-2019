# -*- coding: utf-8 -*-

from dependency_inversion import main


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
    main(
        _fake_input('Nikita'),
        _fake_print('Nikita'),
    )


if __name__ == '__main__':
    test_main()
    print('Done!')  # noqa: T001

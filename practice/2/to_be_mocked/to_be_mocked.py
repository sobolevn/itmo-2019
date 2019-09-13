# -*- coding: utf-8 -*-


def main():
    """Asks and prints the user's name."""
    # Running phase:
    username = input('What is your name?')  # noqa: WPS421, S322
    print(username)  # noqa: T002


if __name__ == '__main__':
    # No build phase :(
    main()

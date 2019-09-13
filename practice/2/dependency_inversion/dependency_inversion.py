# -*- coding: utf-8 -*-


def main(input_function, print_function):
    """Asks and prints the user's name."""
    # Running phase:
    username = input_function('What is your name?')
    print_function(username)


if __name__ == '__main__':
    # Build phase:
    main(input, print)  # noqa: T002

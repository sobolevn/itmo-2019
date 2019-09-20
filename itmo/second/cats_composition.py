# -*- coding: utf-8 -*-

# We reuse implementation from the direct version:
from itmo.second.cats_direct import (
    create_parser,
    fetch_cat_fact,
    fetch_cat_image,
    save_cat,
    one_more_name,
)


class CatProcessor(object):
    """
    Knows exactly how to process cats.

    Only uses composition.
    """

    def __init__(
        self,
        fetch_text,
        fetch_image,
        process_text_and_image,
    ):
        """Saves dependencies into internal state."""
        self._fetch_text = fetch_text
        self._fetch_image = fetch_image
        self._process_text_and_image = process_text_and_image

    def __call__(self, index):
        """Runs the process of cat downloading."""
        return self._process_text_and_image(
            index,
            self._fetch_text(),
            self._fetch_image(),
        )


def main(
    cats_to_fetch,
    *,
    process_cat,
    show_information,
):
    """Fetches cats and saves the into temp folder."""
    if not cats_to_fetch:
        show_information('No cats :(')
        return

    for cat_index in range(1, cats_to_fetch + 1):
        process_cat(cat_index)
    show_information('Cats downloaded!')


if __name__ == '__main__':
    # Building dependencies:
    cat_processor = CatProcessor(fetch_cat_fact, fetch_cat_image, save_cat)

    # Building our main:
    main(
        create_parser().parse_args().count,
        process_cat=cat_processor,
        show_information=print,  # noqa: T002
    )

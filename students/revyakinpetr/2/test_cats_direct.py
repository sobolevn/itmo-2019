# -*- coding: utf-8 -*-

import unittest

from urllib3.response import HTTPResponse

from itmo.second.cats_direct import (
    create_parser,
    fetch_cat_fact,
    fetch_cat_image,
    save_cat,
)


class TestCatsDirect(unittest.TestCase):
    """Unittest class for cats_direct."""

    def test_parse_args(self):
        """Test parse arguments."""
        test_args = ['--count', '4']
        parse_result = create_parser().parse_args(test_args)
        self.assertEqual(parse_result.count, int(test_args[1]))

    def test_fetch_cat_fact(self):
        """Test fatch cat fact."""
        try:
            cats_fact = fetch_cat_fact()
        except Exception:
            self.fail('HTTP fail')

        self.assertIsInstance(cats_fact, str)
        self.assertGreater(len(cats_fact), 0)

    def test_fetch_cat_image(self):
        """Test fatch cat image."""
        image_formats = ['jpg', 'jpeg', 'gif', 'png']
        try:
            cat_image = fetch_cat_image()
        except Exception:
            self.fail('HTTP fail')

        self.assertEqual(len(cat_image), 2)
        self.assertTrue(cat_image[0] in image_formats)
        self.assertIsInstance(cat_image[1], HTTPResponse)

    def test_save_cat(self):  # noqa: WPS210
        """Test save cat fact and image."""
        test_index = 4
        test_fact = 'test fact'
        test_image_name = ['test_cat_image', 'jpg']
        format_image_path = 'students/revyakinpetr/2/{0}.{1}'
        test_image_path = format_image_path.format(*test_image_name)

        with open(test_image_path, 'rb') as test_image:
            save_cat(
                index=test_index,
                fact=test_fact,
                image=(test_image_name[1], test_image),
            )

        fact_path = 'temp/cat_{0}_fact.txt'.format(test_index)
        with open(fact_path, 'r') as fact:
            self.assertEqual(fact.read(), test_fact)

        image_path = 'temp/cat_{0}_image.{1}'.format(
            test_index,
            test_image_name[1],
        )
        with open(image_path, 'rb') as img:
            self.assertGreater(len(img.read()), 0)


if __name__ == '__main__':
    unittest.main()

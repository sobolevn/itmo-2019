# -*- coding: utf-8 -*-

import glob
import os
import unittest

import pytest

from itmo.second import cats_composition


class TestCatsComposition(unittest.TestCase):
    """Unittest class for cats composition."""

    @pytest.mark.xfail
    def test_main(self):
        """Test main function."""
        test_index = 1

        cat_processor = cats_composition.CatProcessor(
            fetch_text=cats_composition.fetch_cat_fact,
            fetch_image=cats_composition.fetch_cat_image,
            process_text_and_image=cats_composition.save_cat,
        )

        fact_path = 'temp/cat_{0}_fact.txt'.format(test_index)
        if os.path.exists(fact_path):
            os.remove(fact_path)

        image_path = 'temp/cat_{0}_image.*'.format(test_index)
        for image_file in glob.glob(image_path):
            os.remove(image_file)

        cats_composition.main(
            test_index,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(fact_path))
        self.assertEqual(len(glob.glob(image_path)), 1)


if __name__ == '__main__':
    unittest.main()

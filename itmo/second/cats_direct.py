# -*- coding: utf-8 -*-

import argparse
import shutil

import requests


def create_parser():
    """Creates parser for command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--count',
        type=int,
        help='Number of cats to fetch',
    )
    return parser


def fetch_cat_fact():
    """Fetches cat's fact."""
    response = requests.get('https://cat-fact.herokuapp.com/facts/random')
    response.raise_for_status()
    return response.json()['text']


def fetch_cat_image():
    """Fetches cat's image."""
    response = requests.get('https://aws.random.cat/meow')
    response.raise_for_status()

    image_url = response.json()['file']
    image_extension = image_url.split('.')[-1]
    image = requests.get(image_url, stream=True)
    return image_extension, image.raw


def save_cat(index, fact, image):
    """Saves cat's info to the disk."""
    fact_path = 'temp/cat_{0}_fact.txt'.format(index)
    image_path = 'temp/cat_{0}_image.{1}'.format(index, image[0])
    with open(fact_path, 'w+') as fact_file:
        fact_file.write(fact)

    with open(image_path, 'wb+') as image_file:
        shutil.copyfileobj(image[1], image_file)


def main():
    """Fetches cats and saves the into temp folder."""
    cats_to_fetch = create_parser().parse_args().count
    if not cats_to_fetch:
        print('No cats :(')  # noqa: T001
        return

    for cat_index in range(1, cats_to_fetch + 1):
        fact = fetch_cat_fact()
        image = fetch_cat_image()
        save_cat(cat_index, fact, image)
    print('Cats downloaded!')  # noqa: T001


if __name__ == '__main__':
    main()

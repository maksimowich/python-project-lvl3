#!/usr/bin/env python
import argparse
import os

from page_loader.page_loader import download

parser = argparse.ArgumentParser()

parser.add_argument('url')
parser.add_argument('-o', '--output', default=os.path.abspath(os.curdir))


def main():
    args = parser.parse_args()
    print(download(args.url, args.output))

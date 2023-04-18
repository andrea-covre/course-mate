import unittest
import argparse

from api.tests.base_test import BaseTestCase

if __name__ == '__main__':
    
    # Use default local address or address spcecifed by the user
    parser = argparse.ArgumentParser(description='Specify the base URL to use for non-local APIs testing')
    parser.add_argument('-p', '--public-url', type=str, default=None, help='Base URL')
    args = parser.parse_args()
    
    if args.public_url:
        print(args.public_url)
        BaseTestCase.BASE_URL = args.public_url + "/"

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('api/tests')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
import argparse
import os.path
import sys
import unittest


scriptDir = os.path.dirname(os.path.abspath(__file__))
# Add base module to python paths
sys.path.append(os.path.realpath(os.path.join(scriptDir, '..', '..')))

if __name__ == '__main__':

    if sys.version_info.major != 3 or sys.version_info.minor < 3:
        sys.stderr.write('Tests require at least python 3.3 to run\n')
        sys.exit()

    # Parse command line option (which is optional and positional)
    parser = argparse.ArgumentParser(description='Run tests')
    parser.add_argument('suite', nargs='?', type=str, help='system or module path to test suite to run, defaults to all tests', default=scriptDir)
    args = parser.parse_args()
    # Get all tests into suite
    tests = unittest.TestLoader().discover(args.suite, 'test*.py')
    # Run them
    unittest.TextTestRunner().run(tests)

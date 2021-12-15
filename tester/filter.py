from shutil import copyfile
from os import listdir, system
from os.path import isfile, join, abspath

import os
import sys

from run_test import run_test
from run_test import parse_tests

def fail_args():
    print("Missing arguments")
    print("python3 filter.py [input] [output] [tests]")
    sys.exit(-1)

def test_file(file: str, tests) -> bool:
    # Return True if at least one test fails
    for (id, input, ans) in tests:
        out = run_test(file, input)
        try:
            out_as_int = int(out)
            if ans != out_as_int:
                return True
        except ValueError:
            return True
    return False

def main():
    args = sys.argv

    if len(args) < 4:
        fail_args()

    input_folder = args[1]
    output_folder = args[2]
    tests_folder = args[3]

    input_files = [(join(input_folder, f), f) for f in listdir(input_folder) if isfile(join(input_folder, f))]
    tests = parse_tests(tests_folder)

    for path, file in input_files:
        if test_file(path, tests):
            copyfile(path, join(output_folder, file))

if __name__ == "__main__":
    main()
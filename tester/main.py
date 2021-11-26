import sys

from run_test import test_folder
from run_test import compile_codes

def fail_args():
    print("Missing arguments")
    print("python3 main.py [compile|test] [input] [tests|output] [results]")
    sys.exit(-1)

if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 1:
        fail_args()

    mode = args[1]
    if mode == "compile":
        if len(args) <= 3:
            fail_args()
        input_folder = args[2]
        output_folder = args[3]

        compile_codes(input_folder, output_folder)
    elif mode == "test":
        if len(args) <= 4:
            fail_args()
        input_folder = args[2]
        tests_folder = args[3]
        results = args[4]
        test_folder(input_folder, tests_folder, results)
    else:
        fail_args()
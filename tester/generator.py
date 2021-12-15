import sys

from itertools import permutations

from run_test import run_test

def fail_args():
    print("Missing arguments")
    print("python3 generator.py [n] [m] [output] [model solution]")
    sys.exit(-1)

perms = []
current = []

def run(n):
    global perms
    perms = list(permutations(range(1, n + 1)))

def form_tests(model):
    tests = []

    for p in perms:
        test_str = f"{len(p)}\n" # add first line that contains n.

        for x in list(p):
            test_str += str(x) + " "

        solution = int(run_test(model, test_str))

        tests.append((test_str, solution))

    return tests

def write_output(tests, output):
    for idx, (test, ans) in enumerate(tests):
        with open(f"{output}/{(idx + 1):05d}.in", "w") as f:
            f.write(test)
        
        with open(f"{output}/{(idx + 1):05d}.ans", "w") as f:
            f.write(str(ans))

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 5:
        fail_args()

    n = int(args[1])
    m = int(args[2])
    output = args[3]
    model = args[4]

    current = [0] * n

    run(n)

    tests = form_tests(model)

    write_output(tests, output)


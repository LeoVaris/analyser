import sys
import random

from run_test import run_test

def fail_args():
    print("Missing arguments")
    print("python3 main.py [n] [max] [count] [output] [model solution]")
    sys.exit(-1)

permutations = []

def run(n, m, cnt):
    for _ in range(cnt):
        lst = []
        for _ in range(n):
            lst.append(random.randint(1, m))
        permutations.append(lst)

def form_tests(model):
    tests = []

    for p in permutations:
        test_str = f"{len(p)}\n" # add first line that contains n.

        for x in p:
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

    if len(args) < 6:
        fail_args()

    n = int(args[1])
    m = int(args[2])
    cnt = int(args[3])
    output = args[4]
    model = args[5]

    run(n, m, cnt)

    tests = form_tests(model)

    write_output(tests, output)


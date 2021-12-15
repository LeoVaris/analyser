from os import listdir, system
from os.path import isfile, join, abspath
from subprocess import run, PIPE, DEVNULL, TimeoutExpired
from joblib import Parallel, delayed
import multiprocessing as mp
import tqdm

def run_test(file: str, input: str) -> str:
    try:
        p = run([abspath(file)], stdout=PIPE, stderr=DEVNULL, input=input, encoding='ascii', timeout=1, cwd='/tmp')
    except TimeoutExpired:
        return "TIME LIMIT EXCEEDED"
    except ValueError:
        return "RUNTIME ERROR"
    if p.returncode != 0:
        return "RUNTIME ERROR"
    return p.stdout

def compile_file(folder: str, file: str, output_folder: str) -> bool:
    p = run(["g++", "-std=c++17", "-O2", "-o", f"{output_folder}/{file[:-4]}", join(folder, file)], stdout=DEVNULL, stderr=DEVNULL)
    return p.returncode == 0

def compile_codes(input_folder: str, output_folder: str) -> None:
    paths = [(input_folder, f) for f in listdir(input_folder) if isfile(join(input_folder, f))]

    compiled = sum(Parallel(n_jobs=8)(delayed(compile_file)(folder, file, output_folder) for folder, file in paths))
    
    print(f"{compiled}/{len(paths)} compiled successfully. Binaries were saved to {output_folder}")

def parse_tests(tests_folder: str):
    input_files = [join(tests_folder, f) for f in listdir(tests_folder) if isfile(join(tests_folder, f)) and f[-2:] == "in"]
    result = []

    for file in input_files:
        with open(file, "r") as f:
            input = f.read()

        with open(file[:-2] + "ans", "r") as f:
            ans = int(f.read())

        result.append((file.split("/")[-1][:-3], input, ans))

    return result

def test_folder(folder: str, tests_folder: str, result_file: str) -> None:
    compiled = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]

    tests = parse_tests(tests_folder)

    print("Testing", len(compiled), "files with", len(tests), "tests.")

    #results = [[1] * len(tests) for _ in range(len(compiled))]

    increment = 0.01
    target_percent = increment
    
    def execute(file_idx, file):
        #global target_percent
        #if file_idx / len(compiled) >= target_percent:
        #    print(f"{round(file_idx / len(compiled) * 100, 2)}%")
        #    target_percent += increment
        result_lst = [1] * len(tests)
        for test_idx, (id, input, ans) in enumerate(tests):
            out = run_test(file, input)
            try:
                out_as_int = int(out)
                if ans == out_as_int:
                    result_lst[test_idx] = 0
            except ValueError:
                pass
        return result_lst

    #results = []
    #pool = mp.Pool(processes=2)

    #for result in tqdm.tqdm(pool.imap_unordered(execute, compiled), total=len(compiled)):
    #    results.append(result)

    results = Parallel(n_jobs=5)(delayed(execute)(file_idx, file) for file_idx, file in tqdm.tqdm(list(enumerate(compiled))))

    """
    for file_idx, file in enumerate(compiled):
        if file_idx / len(compiled) >= target_percent:
            print(f"{round(file_idx / len(compiled) * 100, 2)}%")
            target_percent += increment
        for test_idx, (id, input, ans) in enumerate(tests):
            out = run_test(file, input)
            try:
                out_as_int = int(out)
                if ans == out_as_int:
                    results[file_idx][test_idx] = 0
            except:
                pass
    """

    with open(result_file, "w") as f:
        f.write(";".join([id for id, _, _ in tests]) + "\n")

        for row in results:
            f.write(";".join([str(val) for val in row]) + "\n")
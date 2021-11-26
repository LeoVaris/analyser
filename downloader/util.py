

def get_hashes(file: str):
    result = []

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split(";")

            status = int(parts[4])
            score = int(parts[5])
            hash = parts[6]

            if status != 2 or score != 0:
                continue

            result.append(hash)

    return result
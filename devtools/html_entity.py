import json
import os.path


def main():
    with open("html_entity.txt") as f:
        lines = f.readlines()
    mapping = {}
    for line in lines:
        key, val = process_line(line)
        mapping[key] = val
    with open(os.path.join(os.path.dirname(__file__), "html_entity.json"), "wt") as f:
        print(json.dumps(mapping), file=f)


def process_line(line):
    res = line.split(" \t")
    key = None
    val = None
    i = 0
    while i < 5:
        x = res[i]
        if x:
            if i == 0:
                val = x
            if i == 3:
                key = chr(int(x[2:], 16))
            i += 1
    return key, val


if __name__ == "__main__":
    main()
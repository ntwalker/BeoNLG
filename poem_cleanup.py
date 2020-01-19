import os
import re
import time

path = 'data/'
datafiles = os.listdir(path)

if __name__ == "__main__":
    for filename in datafiles:
        with open(os.path.join(path, filename), "r", encoding="utf-8") as f:
            for line in f:
                if line == "\n":
                    continue
                print(re.sub(r"\s\s+", " ", line))
            break
        time.sleep(1)
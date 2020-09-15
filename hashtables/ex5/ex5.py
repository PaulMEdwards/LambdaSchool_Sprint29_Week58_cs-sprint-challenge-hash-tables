debug = False
writeFiles = False


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    lf = len(files)
    lq = len(queries)
    if debug:
        print(f"#  files={lf}")
        print(f"#queries={lq}")
    data = {}

    if debug or writeFiles: print() # blank line

    fd = 'files.txt'
    with open (fd, 'w') as filesOutput:
        if writeFiles: filesOutput.truncate(0)
        for f in files:
            t = f.split('/')
            last = t[len(t)-1]
            if debug: print(f"file:\t{last}")
            test = None
            try:
                test = data[last]
            except:
                pass
            if debug: print(f"test 0:\t{test}")
            if test is None:
                data[last] = [f]
            if test is not None:
                tl = len(test)
                if tl == 0:
                    data[last] = [f]
                elif tl > 0:
                    data[last].append(f)
            if debug: print(f"test 1:\t{data[last]}")
            if writeFiles: filesOutput.write(f"{f}\n")
    if writeFiles: print(f"Wrote files data to '{fd}'...")
    filesOutput.close()

    fq = 'queries.txt'
    with open (fq, 'w') as queriesOutput:
        if writeFiles: queriesOutput.truncate(0)
        for q in queries:
            if writeFiles: queriesOutput.write(f"{q}\n")
            test = None
            try:
                test = data[q]
                if debug and test is not None: print(f"query: {q}, result: {test}")
            except:
                pass
            if test is not None:
                tl = len(test)
                if tl > 0:
                    for t in test:
                        result.append(t)
    if writeFiles: print(f"Wrote queries data to '{fq}'...")
    queriesOutput.close()

    if writeFiles:
        fd = 'dict.txt'
        with open (fd, 'w') as filesDict:
            filesDict.truncate(0)
            print(data, file=filesDict)
        filesDict.close()
        print(f"Wrote Dictionary data to '{fd}'...")

    if debug or writeFiles: print() # blank line

    if debug or writeFiles: print(f"result:\t{result}")
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

debug = True

from hashtable import HashTable

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
    data = HashTable(lq)

    if debug: print() # blank line

    fd = 'files.txt'
    with open (fd, 'w') as filesOutput:
        filesOutput.truncate(0)
        for f in files:
            t = f.split('/')
            last = t[len(t)-1]
            data.put(last, f)
            if debug: filesOutput.write(f"{f}\n")
    if debug: print(f"Wrote files data to '{fd}'...")
    filesOutput.close()

    fq = 'queries.txt'
    with open (fq, 'w') as queriesOutput:
        queriesOutput.truncate(0)
        for q in queries:
            if debug: queriesOutput.write(f"{q}\n")
            test = None
            try:
                test = data.get(q)
                if debug and test is not None: print(f"query: {q}, result: {test}")
            except:
                pass
            if test is not None:
                result.append(test)
    if debug: print(f"Wrote queries data to '{fq}'...")
    queriesOutput.close()

    if debug:
        fh = 'ht.txt'
        with open (fh, 'w') as filesHashTable:
            filesHashTable.truncate(0)
            print(data, file=filesHashTable)
        filesHashTable.close()
        print(f"Wrote HashTable data to '{fh}'...")

    if debug: print() # blank line

    if debug: print(f"result:\t{result}")
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

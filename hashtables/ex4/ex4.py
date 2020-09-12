debug = False

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    pos_data = {}
    neg_data = {}

    if debug and len(a) < 30: print(f"\ninput\n{a}")

    for v in a:
        if v > 0:
            pos_data[v] = v
        elif v < 0:
            neg_data[abs(v)] = v

    if debug: print(f"pos_data\t{pos_data}\nneg_data\t{neg_data}")

    for k,v in neg_data.items():
        test = 0
        try:
            test = pos_data[k]
            if debug: print(f"k={k}, v={v}, test={test}")
            if test > 0:
                result.append(test)
                if debug: print(f"appended '{test}' to result: {result}")
        except:
            pass

    if debug: print(f"final result\n{result}")
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

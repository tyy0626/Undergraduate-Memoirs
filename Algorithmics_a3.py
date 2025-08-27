import sys

def read_ints(input_gen, need):
    out = []
    while len(out) < need:
        try:
            out.extend(map(int, next(input_gen)))
        except StopIteration:
            break
    return out[:need]

def process_case(input_gen):
    params = read_ints(input_gen, 3)
    if len(params) < 3:
        return False, None
    m, n, k = params
    if m == 0 and n == 0 and k == 0:
        return False, None


    mat_vals = read_ints(input_gen, m * n)
    if len(mat_vals) < m * n:
        return False, None

    queries = read_ints(input_gen, k)
    if len(queries) < k:
        return False, None

    query_set = set(queries)
    pos = {}


    for idx, val in enumerate(mat_vals):
        if val in query_set and val not in pos:
            r = idx // n
            c = idx % n
            pos[val] = (r, c)

            if len(pos) == len(query_set):
                break


    output = []
    for s in queries:
        if s in pos:
            r, c = pos[s]
            output.append(f"{r} {c}")
        else:
            output.append("None")

    return True, output

def main():
    input_gen = (line.split() for line in sys.stdin)
    out_all = []
    while True:
        ok, out = process_case(input_gen)
        if not ok:
            break
        if out is not None:
            out_all.extend(out)
    print("\n".join(out_all))

if __name__ == "__main__":
    main()

def c_gen(n, m):

    rang = [i for i in range(n)]
    start = rang[0 : m] # first combination
    end = rang[n - m : n] # last combination

    comb = start

    while True:
        yield comb
        pos = m - 1
        while True:
            if comb[pos] == end[pos]:
                pos -= 1

            else:
                break

        comb[pos] += 1
        for i in range(pos + 1, m, +1):
            comb[i] = comb[i - 1] + 1

        if comb == end:
            yield comb
            return


if __name__ == '__main__':
    n = 5
    m = 3
    for el in c_gen(n, m):
        print(el)
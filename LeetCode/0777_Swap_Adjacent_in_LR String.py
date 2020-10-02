if start.replace('X', '') != end.replace('X', ''):
        return False

    ctr = collections.Counter()
    for s, e in zip(start, end):
        ctr[s] += 1
        ctr[e] -= 1
        if ctr['L'] > 0 or ctr['R'] < 0:
            return False
    return True
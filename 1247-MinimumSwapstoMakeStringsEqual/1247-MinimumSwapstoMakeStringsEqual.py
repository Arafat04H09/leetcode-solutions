def minimumSwap(self, s1, s2):
    count = Counter([s1[i] + s2[i] for i in range(len(s1))])
    xy, yx = count['xy'], count['yx']
    return -1 if (xy + yx) % 2 else xy/2 + yx/2 + 2*(xy%2)
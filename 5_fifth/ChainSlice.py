from itertools import chain, islice

def chainslice(begin, end, *seq):
    return islice(chain(*seq), begin, end)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# entropy_functions.py
# (c) Jim Bagrow, Lewis Mitchell
# Last Modified: 2015-05-24

import math
import collections


def log2(x):
    return math.log(x,2)


def shannon_entropy(seq):
    """Plain old Shannon entropy (in bits)."""
    C, n = collections.Counter(seq), float(len(seq))
    return -sum( c/n * log2(c/n) for c in list(C.values()))


def entropy(seq, lambdas=False):
    """Estimate the entropy rate of the symbols encoded in `seq`, a list of
    strings.
    
    Kontoyiannis, I., Algoet, P. H., Suhov, Y. M., & Wyner, A. J. (1998).
    Nonparametric entropy estimation for stationary processes and random
    fields, with applications to English text. IEEE Transactions on Information
    Theory, 44(3), 1319-1327.
    """
    N = len(seq)
    L = []
    for i,w in enumerate(seq):
        seen = True
        prevSeq = " %s " % " ".join(seq[0:i])
        c = i
        while seen and c < N:
            c += 1
            seen = (" %s " % " ".join(seq[i:c])) in prevSeq
        l = c - i
        L.append(l)
    
    if lambdas:
        return L
    return (1.0*N/sum(L)) * log2(N)


def cross_entropy(W1, W2, PTs, lambdas=False):
    """Find the cross entropy H_cross(W2|W1), how many bits we would need to
    encode the data in W2 using the information in W1. W1 and W2 are lists of
    strings, PTs is a list of integers with the same length as W2 denoting the
    relative time ordering of W1 vs. W2. These integers tell us the position
    PTs[x] = i in W1 such that all symbols in W1[:i] occurred before the x-th
    word in W2.
    """
    
    lenW1 = len(W1)
    lenW2 = len(W2)
    L = []
    for j,(wj,i) in enumerate( zip(W2,PTs) ):
        seen = True
        prevW1 = " %s " % " ".join( W1[:i] )
        c = j
        while seen and c < lenW2:
            c += 1
            seen = (" %s " % " ".join(W2[j:c]) in prevW1 )
        l = c - j
        L.append(l)
    
    if lambdas:
        return L
    return (1.0*lenW2/sum(L)) * log2(lenW1)


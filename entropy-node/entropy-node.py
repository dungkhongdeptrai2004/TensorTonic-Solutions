import numpy as np
import math

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    d = {}
    a = [] # từng class
    if (len(y) == 0):
        return 0.0
    entropy = 0
    for v in y:
        if (d.get(v)):
            d[v] += 1
        else:
            d[v] = 1
            a.append(v)
    for c in a:
        entropy += d[c]/len(y)*math.log2(d[c]/len(y))
    return -entropy
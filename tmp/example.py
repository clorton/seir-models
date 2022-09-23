#! /usr/bin/env python3

import numpy as np
import pandas as pd

def system(t, a=1.0/512, b=0, c=-1.5, d=5):
    result = a*(t**3) + b*(t**2) + c*t + d
    return result

if __name__ == "__main__":
    ts = np.arange(0, 33)
    results = system(ts)
    print(results)

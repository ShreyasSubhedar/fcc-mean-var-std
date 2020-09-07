import numpy as np


def calculate(list):
    try:
        if len(list) != 9:
            raise ValueError
    except:
        raise ValueError("List must contain nine numbers.")

# Converting list element into 3*3 numpy array
    ds = np.array((list[0:3], list[3:6], list[6:]))

    d = {
        "mean": [
            ds.mean(axis=0).tolist(),
            ds.mean(axis=1).tolist(),
            ds.flatten().mean(axis=0)
        ],
        "variance": [
            ds.var(axis=0).tolist(),
            ds.var(axis=1).tolist(),
            ds.flatten().var(axis=0)
        ],
        "standard deviation": [
            ds.std(axis=0).tolist(),
            ds.std(axis=1).tolist(),
            ds.flatten().std(axis=0)
        ],
        "max": [
            ds.max(axis=0).tolist(),
            ds.max(axis=1).tolist(),
            ds.flatten().max(axis=0)
        ],
        "min": [
            ds.min(axis=0).tolist(),
            ds.min(axis=1).tolist(),
            ds.flatten().min(axis=0)
        ],
        "sum": [
            ds.sum(axis=0).tolist(),
            ds.sum(axis=1).tolist(),
            ds.flatten().sum(axis=0)
        ],
    }

    return d

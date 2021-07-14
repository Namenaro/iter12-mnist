import matplotlib.pyplot as plt
import numpy as np

def get_hist(values, nbins=10):
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                weights=np.ones_like(values) / len(values), range=(0, values.max()))
    return probs, bins
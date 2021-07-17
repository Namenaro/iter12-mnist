import matplotlib.pyplot as plt
import numpy as np
import json
import os.path

from data import *
from logger import *
from sensors import *


def get_hist(values, nbins=10):
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                weights=np.ones_like(values) / len(values), range=(0, values.max()))
    return probs, bins

def get_means(radius, pics):
    ymax = pics[0].shape[0]
    xmax = pics[0].shape[1]
    means = []
    for pic in pics:
        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                val = get_sensory_array(pic, centerx, centery, radius)
                means.append(np.mean(val))
    return means

def get_hist_for_radius(radius, pics, nbins):
    values = get_means(radius, pics)
    probs, bins = get_hist(np.array(values), nbins)
    return probs, bins

def count_hists_for_radiuses():
    nbins =20
    radiuses = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    npics=90
    pics = get_diverse_set_of_numbers(npics+1)[0:npics]
    data = {}
    for radius in radiuses:
        print("get stat for raduis " + str(radius))
        probs, bins = get_hist_for_radius(radius, pics, nbins)
        data[radius] = {'probs':probs.tolist(), 'bins':bins.tolist()}
    return data

def get_hists_for_sensradiuses():
    filename = "hists.json"
    if os.path.isfile(filename):
        with open(filename) as f:
            print("load json with naive stat...")
            data = json.load(f)
            return data
    print("gather naive stat...")
    data = count_hists_for_radiuses()
    with open(filename, 'w') as f:
        json.dump(data, f)
    return data

def get_hist_for_sensradius(sensor_field_radius):
    rad_data = get_hists_for_sensradiuses()[sensor_field_radius]
    probs = rad_data['probs']
    bins =  rad_data['bins']
    return probs, bins

if __name__ == "__main__":
    data = get_hists_for_sensradiuses()




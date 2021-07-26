import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from motif import *
from logger import *
from sensors import *
from create_motif import *
from init_motif import *
from data import *
import uuid

class Prediction:
    def __init__(self, dx, dy, u_radius, etalon_mean, sensor_field_radius, stat={}):
        self.dx = dx
        self.dy = dy
        self.u_radius = u_radius
        self.etalon_mean = etalon_mean
        self.sensor_field_radius = sensor_field_radius
        self.stat = stat

    def apply(self, pic, anchorx, anchory):
        X, Y = get_coords_less_or_eq_raduis(anchorx + self.dx, anchory+self.dy, self.u_radius)
        nearest_mean = make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon_mean) < abs(nearest_mean - self.etalon_mean):
                nearest_mean = mean
        return nearest_mean
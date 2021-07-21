from motif import *
from logger import *

def visualise_on_pic(motif, pic):
    full_sprouts = motif.apply_to_pic(pic, desired_num_of_full_sprouts=2)
    if full_sprouts is False:
        return
    # росток это последовательность записей вида "нода, фактическая координата гипотезы"



def get_points_with_full_sprouts(full_sprouts):
    pass

def plot_sprout(sprout, pic):
    pass


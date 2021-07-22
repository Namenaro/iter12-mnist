import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from motif import *
from logger import *
from sensors import *
from save_motif import *
from init_motif import *
from data import *

def visualise_on_pic(motif, pic, desired_num_of_full_sprouts, logger):
    # росток это последовательность записей вида "нода, фактическая координата гипотезы"
    dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic, desired_num_of_full_sprouts)

    # рисуем все точки, из которых удалось вырастатить ростки успешно
    fig, ax = plt.subplots()
    ax.imshow(pic, cmap='gray_r')
    for coord_pair in dict_coords_sprouts.keys():
        x = coord_pair[0]
        y= coord_pair[1]
        ax.scatter(x, y, s=100, c='red', marker='o', alpha=0.4)
    logger.add_fig(fig)

    # рисуем все ростки, из всех точек
    fig, ax = plt.subplots()
    for key in dict_coords_sprouts.keys():
        sprouts_from_point = dict_coords_sprouts[key]
        for sprout in sprouts_from_point:
            plot_sprout_with_radiuses(sprout, pic, ax)
    logger.add_fig(fig)


def plot_sprout(sprout, pic, ax):
    ax.imshow(pic, cmap='gray_r')
    X=[]
    Y=[]
    for triple in sprout:
        x= triple[1]
        y= triple[2]
        X.append(x)
        Y.append(y)

    ax.plot(X,Y, 'o-')

def plot_sprout_with_radiuses(sprout, pic, ax):
    ax.imshow(pic, cmap='gray_r')
    X=[]
    Y=[]
    for triple in sprout:
        x= triple[1]
        y= triple[2]
        X.append(x)
        Y.append(y)
        u_radius = triple[0].experiment.u_radius
        UX, UY = get_coords_less_or_eq_raduis(x, y, u_radius)
        plt.scatter(UX, UY, s=100, c='blue', marker='o', alpha=0.4)

        # sensor_field_radius = triple[0].experiment.sensor_field_radius
        # sensX, sensY = get_coords_less_or_eq_raduis(x, y, sensor_field_radius)
        # plt.scatter(sensX, sensY, s=100, c="#308040", marker='*', alpha=0.8)

    ax.plot(X,Y, 'o-')

def ONE_PIC_EXP():
    logger = HtmlLogger("EX2")
    motif = motif_from_json("motif3.json")
    # motif = init_motif_handly()
    pic = etalons_of3()[0]
    desired_num_of_full_sprouts = 2
    visualise_on_pic(motif, pic, desired_num_of_full_sprouts, logger)
    logger.close()

def MANY_PIC_EXP():
    logger = HtmlLogger("EX3")
    motif = motif_from_json("motif3.json")
    desired_num_of_full_sprouts = 3
    pics = etalons_of3()
    for pic in pics:
        dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic, desired_num_of_full_sprouts)
        # рисуем все ростки, из всех точек
        fig, ax = plt.subplots()
        for key in dict_coords_sprouts.keys():
            sprouts_from_point = dict_coords_sprouts[key]
            for sprout in sprouts_from_point:
                plot_sprout_with_radiuses(sprout, pic, ax)
        logger.add_fig(fig)
    logger.close()

if __name__ == "__main__":
    MANY_PIC_EXP()





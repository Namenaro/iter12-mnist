import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from motif import *
from logger import *

def visualise_on_pic(motif, pic, desired_num_of_full_sprouts, logger):
    # росток это последовательность записей вида "нода, фактическая координата гипотезы"
    dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic, desired_num_of_full_sprouts)

    fig, ax = plt.subplots()
    ax.imshow(pic, cmap='gray_r')
    for coord_pair in dict_coords_sprouts.keys():
        x = coord_pair[0]
        y= coord_pair[1]
        ax.scatter(x, y, s=100, c='red', marker='o', alpha=0.4)
    logger.add_fig(fig)

    key = list(dict_coords_sprouts.keys())[0]
    sprouts = dict_coords_sprouts[key]
    fig = plot_sprout(sprouts[0], pic)
    logger.add_fig(fig)




def plot_sprout(sprout, pic):
    fig, ax = plt.subplots()
    ax.imshow(pic, cmap='gray_r')
    X=[]
    Y=[]
    for triple in sprout:
        x= triple[1]
        y= triple[2]
        X.append(x)
        Y.append(y)
    ax.plot(X,Y, 'o-')
    return fig


if __name__ == "__main__":
    from save_motif import *
    from data import *

    logger = HtmlLogger("EX1")
    motif = motif_from_json("motif.json")
    pic = etalons_of3()[0]
    desired_num_of_full_sprouts=2
    visualise_on_pic(motif, pic, desired_num_of_full_sprouts, logger)
    logger.close()



import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plot_trajectories_on_pic(pic, Xes, Yes):
    num_trajectories = len(Xes)
    norm = mpl.colors.Normalize(vmin=0, vmax=num_trajectories)
    cmap = cm.hot
    mapper = cm.ScalarMappable(norm=norm, cmap=cmap)
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    for i in range(len(Xes)):
        trajX = Xes[i]
        trajY = Yes[i]
        plt.scatter(trajX[0], trajY[0], s=100, c='red', marker='o', alpha=0.4)
        plt.plot(trajX, trajY, color=mapper.to_rgba(i),  alpha=0.4)
    return fig

def plot_points_on_pic_first_red(pic, X,Y, colors=None):
    if colors is None:
        colors = 'green'
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c=colors, marker='o', alpha=0.4)
    return fig

def plot_hist_from_val(values, nbins=15):
    plt.clf()
    fig, ax = plt.subplots()
    values = np.array(values).flatten()
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                weights=np.ones_like(values) / len(values), range=(0, values.max()))
    return fig

def plot_probs_bins(probs, bins):
    fig, ax = plt.subplots()
    plt.bar(bins[:-1], probs, width=1)
    plt.ylim(0, 1)
    return fig

def plot_several_graphs(graphs, names):
    fig, axs = plt.subplots(len(graphs))
    for i in range(len(graphs)):
        axs[i].plot(graphs[i])
        axs[i].set_title(names[i])
    return fig

def plot_several_lines_pics_with_one_colorbar(pics_series):
    rows = len(pics_series)
    num_pics_in_seria = len(pics_series[0])
    fig, axs = plt.subplots(rows, num_pics_in_seria)
    MIN, MAX = np.array(pics_series).min(), np.array(pics_series).max()
    for row in range(rows):
        for col in range(num_pics_in_seria):
            im = axs[row, col].imshow(pics_series[row][col], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig

def plot_several_pics_with_one_colorbar(pics):
    num_pics_in_seria = len(pics)
    fig, axs = plt.subplots( ncols=num_pics_in_seria)
    MIN, MAX = np.array(pics).min(), np.array(pics).max()

    for i in range(num_pics_in_seria):
        im = axs[i].imshow(pics[i], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig
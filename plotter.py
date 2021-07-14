import matplotlib as plt
import matplotlib.cm as cm


def plot_trajectories_on_pic(pic, Xes, Yes):
    num_trajectories = len(Xes)
    norm = plt.colors.Normalize(vmin=0, vmax=num_trajectories)
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


from motif import *
from clicker import *
from data import *

from experiment import ExperimentLongTerm
from motif import Node, Motif
from sensors import *
from plotter import *
import uuid

# руками инициализируем мотив:
# (один или несколько кликов перемежаемых вводом сенсорного радиуса из консоли + вводом припуска на событие)
def init_node(node_id, dx, dy, u_radius, sensor_field_radius, ed_min, ed_max):
    experiment = ExperimentLongTerm(dx, dy, u_radius, sensor_field_radius, ed_min, ed_max)
    node = Node(experiment, node_id)
    return node

def make_node_from_info_dict(node_id, lastx, lasty, x, y, info_dict, pic):
    u_radius = 0
    if 'u_radius' in info_dict.keys():
        u_radius = int(info_dict['u_radius'])

    event_diameter = 0
    if 'event_diameter' in info_dict.keys():
        event_diameter = float(info_dict['event_diameter'])

    sensor_field_radius = 0
    if 'sensor_field_radius' in info_dict.keys():
        sensor_field_radius = int(info_dict['sensor_field_radius'])

    mean = make_measurement(pic, centerx=x, centery=y, radius=sensor_field_radius)
    ed_min = mean - event_diameter / 2
    ed_max = ed_min + event_diameter

    dx = None
    dy = None
    if lastx is None:
        dx = 0
        dy = 0
    else:
        dx = x - lastx
        dy = y - lasty
    node = init_node(node_id=node_id, dx=dx, dy=dy, u_radius=u_radius,
                     sensor_field_radius=sensor_field_radius, ed_min=ed_min, ed_max=ed_max)
    return node


def init_motif_handly(keys=["sensor_field_radius", "event_diameter", 'u_radius' ]):

    pic = etalons_of3()[0]
    X, Y, info_dicts = select_coord_on_pic(pic,keys )
    #---
    plot_points_on_pic_first_red(pic, X, Y)
    plt.savefig("poiints.png")
    print("X=" + str(X))
    print("Y=" + str(Y))
    #----
    nodes = []
    first_node = make_node_from_info_dict(node_id=str(uuid.uuid4()), lastx=None, lasty=None,
                                          x=X[0], y=Y[0],info_dict=info_dicts[0], pic=pic)
    for i in range(1, len(X)):
        node = make_node_from_info_dict(node_id=str(uuid.uuid4()), lastx=X[i-1], lasty=Y[i-1],
                                          x=X[i], y=Y[i],info_dict=info_dicts[i], pic=pic)
        nodes.append(node)
    if len(nodes)>0:
        first_node.next_node = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next_node = nodes[i+1]


    motif = Motif(first_node)
    init_coords = [X[0], Y[0]]
    return motif, init_coords



if __name__ == "__main__":
    motif = init_motif_handly()
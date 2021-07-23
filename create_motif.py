import json
import os.path

from experiment import *
from motif import *

def motif_to_json(json_name, motif, xy_in3): # xy_in3 это массив из двух чисел, координаты инициализирующего клика
    nodes_dicts = {}
    node = motif.first_node
    init_coords = xy_in3
    while node is not None:
        next_node_id = None
        if node.next_node is not None:
            next_node_id = node.next_node.node_id

        nodes_dicts[node.node_id] = { "node_experiment": vars(node.experiment),
                                      "next_node_id" : next_node_id,
                                      "init_coords" : init_coords }
        if init_coords is not None:
           init_coords = None
        node = node.next_node
    with open(json_name, 'w') as f:
        json.dump(nodes_dicts, f)


def motif_from_json(json_name):
    init_coords = None
    if os.path.isfile(json_name):
        with open(json_name) as f:
            nodes_dicts = json.load(f)
            first_node = None
            for node_id in nodes_dicts.keys():
                if nodes_dicts[node_id]["init_coords"] is not None:
                    experiment = ExperimentLongTerm(**nodes_dicts[node_id]["node_experiment"])
                    first_node = Node(experiment, node_id)
                    init_coords = nodes_dicts[node_id]["init_coords"]
                    break
            current_node= first_node
            while True:
                next_node_id = nodes_dicts[current_node.node_id]["next_node_id"]
                if next_node_id is None:
                    break
                next_experiment = ExperimentLongTerm(**nodes_dicts[next_node_id]["node_experiment"])
                next_node = Node(next_experiment, next_node_id)
                current_node.next_node = next_node
                current_node = next_node
            motif = Motif(first_node)
            return motif, init_coords



if __name__ == "__main__":
    from init_motif import *
    motif, init_coords = init_motif_handly()
    motif_to_json("simplest.motif", motif, init_coords)
    #motif, init_coords = motif_from_json("motif2.json")
class Node:
    def __init__(self, experimentLT):
        self.experiment = experimentLT
        self.next_experiment = None
        self.predictions = []


class Motif:
    def __init__(self, first_node):
        self.first_node = first_node

    def apply_to_pic(self,pic, xstart, ystart):
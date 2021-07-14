class Node:
    def __init__(self, experimentLT, node_id):
        self.node_id = node_id
        self.experiment = experimentLT
        self.next_node = None
        self.predictions = []


class Motif:
    def __init__(self, first_node):
        self.first_node = first_node

    def apply_to_pic(self,pic):
        ymax = pic.shape[0]
        xmax = pic.shape[1]

        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                best_branch = self.try_grow_from_point(pic, centerx, centery)
                if best_branch is not None:
                    return best_branch
        return False

    def try_grow_from_point(self, pic, xstart, ystart):
        ranged_matches = self.first_node.experiment.make(pic, xstart, ystart)
        num_of_variants = ranged_matches['x']
        if len(num_of_variants == 0):
            return False

        sprouts = [] # росток это последовательность записей вида "нода, фактическая координата гипотезы"
        for i in range(num_of_variants):
            # добавляем num_of_variants новых ростков "единичной" высоты
            sprouts.append([self.first_node, ranged_matches['x'][i], ranged_matches['y'][i]])

        # из лучшего ростка получаем указатель на последнюю в нем ноду (т.е. это сбывшееся пресказаие, запускать эксперимемнт не надо)
        # из этой ноды смотрим, какой у нас следующий эксперимент.
        # если его в памяти нет, то этот росток дорощен до успещного конца
        # если он есть, то выполняем его, и получаем н сбышихся похожих предсказаний.
        # удаляем лучший росток, и заменяем его на н штук новых соритрованных лучших ростков. Цикл замкнулся.
        # если росток пришел в тупик (т.е. нода не последняя, а гипотез выполнившихся нет), то удаляем его
        # если все ростки пришли в тупик (т.е. sprouts пустой), то возврашаем неудчу (false)

        while True:
            if len(sprouts) == 0:
                return False








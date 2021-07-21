class Node:
    def __init__(self, experimentLT, node_id):
        self.node_id = node_id
        self.experiment = experimentLT
        self.next_node = None
        self.predictions = []


class Motif:
    def __init__(self, first_node):
        self.first_node = first_node

    def apply_to_pic(self,pic, desired_num_of_full_sprouts):
        ymax = pic.shape[0]
        xmax = pic.shape[1]

        for centery in range(0, ymax):
            for centerx in range(0, xmax):
                full_sprouts = self.try_grow_from_point(pic, centerx, centery, desired_num_of_full_sprouts)
                if full_sprouts is not None:
                    return full_sprouts
        return False

    def try_grow_from_point(self, pic, xstart, ystart,desired_num_of_full_sprouts):
        ranged_matches = self.first_node.experiment.make(pic, xstart, ystart)
        num_of_variants = ranged_matches['x']
        if len(num_of_variants == 0):
            return False
        full_sprouts = []  # сюда добавляем лишь завершенные ростки, первый лучший
        sprouts = []  # росток это последовательность записей вида "нода, фактическая координата гипотезы"
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
                # все имеющиеся на рассмотрении ростки пришли в тупик
                if len(full_sprouts)>0:
                    return full_sprouts
                else:
                    return False
            top_of_best_sprout = sprouts[0][-1]
            current_done_node = top_of_best_sprout[0]
            currentx = top_of_best_sprout[1]
            currenty = top_of_best_sprout[2]

            if current_done_node.next_node is None:
                # лучший росток дорощен до успещного конца
                full_sprouts.append(list(sprouts[0]))
                sprouts.pop(0)
                if desired_num_of_full_sprouts < len(full_sprouts):
                    continue
                else:
                    return full_sprouts
            ranged_matches = current_done_node.next_node.experiment.make(pic, currentx, currenty)
            if len(ranged_matches['x']) == 0:  # лучший росток пришел в тупик
                sprouts.pop(0)
            else:
                # удаляем лучший росток, и заменяем его на н штук новых соритрованных лучших ростков
                # "на единицу" выше старого
                new_best_sprouts = []
                for i in range(ranged_matches['x']):
                    new_top_for_sprout = [current_done_node.next_node, ranged_matches['x'][i], ranged_matches['y'][i] ]
                    new_sprout = list(sprouts[0]).append(new_top_for_sprout)
                    new_best_sprouts.append(new_sprout)
                sprouts.pop(0)
                sprouts = new_best_sprouts + sprouts












# хороший мотив хорош тем, что хорошо что-то предсказывает.
# Имея в данной ситуации сработавший мотив, мы знаем "что именно мы теперь можем предсказать,
# и оно будет с большой вероятнсотью верно". Предсказание будет делаться в виде проверяемой
# гипотезы, т.е. такой, какую можно проверить при желании.
# Проверяемвая гипотеза будет в виде: если сработал мотив А, то совершаем такое-то управление,
# и там сработает мотив Б.

# Итоговый сценарий (ручного) эксперимента:
# сделать сохранение мотива с координатами исходного клика на эталоне
# загружаем мотив. В начале эксперименты имеет смысл тестить простейшие мотивы из одной ноды
# кликаем в места предсказаний кликером, формируем структуру предсказаний.
# бегаем мотивом по всем картинкам и в каждом месе срабатыввания собираем активации по предсказаниям,
# складываем их в контейнер. После того, как контейнер набран, визуализируем гистограммы и в хтмл.
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from motif import *
from logger import *
from sensors import *
from create_motif import *
from init_motif import *
from data import *

def PREDICTION_EXPERIMENT(logger):
    motif, init_coords = motif_from_json("simplest.motif")
    desired_num_of_full_sprouts = 3
    pics = etalons_of3()
    predictions = init_predictions(pics[0], init_coords)
    raw_predictions_data = gather_stat_for_predictions(pics, motif, predictions)
    for prediction in predictions:

def init_predictions(pic, init_coords):
    pass

def gather_stat_for_predictions(pics, motif, predictions):
    raw_acivations_data = {id:[] for id in list(predictions.keys())}
    for pic in pics:
        dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic,  desired_num_of_full_sprouts=1)
        for coords in dict_coords_sprouts.keys():
            for prediction_id in predictions.keys():
                res = check_prediction(predictions[prediction_id], pic, coords[0], coords[1])
                raw_acivations_data[prediction_id].append(res)
    return raw_acivations_data


def check_prediction(prediction, pic, anchorx, anchory):
    pass

if __name__ == "__main__":
    logger = HtmlLogger("EX_PRED")
    PREDICTION_EXPERIMENT(logger)
    logger.close()

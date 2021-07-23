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

class Prediction:
    def __init__(self, dx, dy, u_radius, etalon_mean, sensor_field_radius):
        self.dx = dx
        self.dy = dy
        self.u_radius = u_radius
        self.etalon_mean = etalon_mean
        self.sensor_field_radius = sensor_field_radius

    def apply(self, pic, anchorx, anchory):
        X, Y = get_coords_less_or_eq_raduis(anchorx, anchory, self.u_radius)
        nearest_mean =  make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon_mean) < abs(nearest_mean - self.etalon_mean):
                nearest_mean = mean
        return nearest_mean

def predictions_to_json(json_name, predictions):
    pass

def predictions_from_json(json_name):
    pass

def PREDICTION_EXPERIMENT(logger):
    motif, init_coords = motif_from_json("simplest.motif")
    pics = etalons_of3()
    predictions = init_predictions(pics[0], init_coords)
    raw_acivations_data = gather_stat_for_predictions(pics, motif, predictions)
    visualise_predictions_stat(predictions, raw_acivations_data, logger)

def init_predictions(pic, init_coords):
    pass

def visualise_predictions_stat(predictions, raw_acivations_data, logger):
    pass

def gather_stat_for_predictions(pics, motif, predictions):
    raw_acivations_data = {id:[] for id in list(predictions.keys())}
    for pic in pics:
        dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic,  desired_num_of_full_sprouts=1)
        for coords in dict_coords_sprouts.keys():
            for prediction_id in predictions.keys():
                res = check_prediction(predictions[prediction_id], pic, coords[0], coords[1])
                raw_acivations_data[prediction_id] =raw_acivations_data[prediction_id] + res
    return raw_acivations_data


def check_prediction(prediction, pic, anchorx, anchory):   #return array!!!
    val = prediction.apply(pic, anchorx, anchory)
    return val

if __name__ == "__main__":
    logger = HtmlLogger("EX_PRED")
    PREDICTION_EXPERIMENT(logger)
    logger.close()

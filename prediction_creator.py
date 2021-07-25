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
import uuid

class Prediction:
    def __init__(self, dx, dy, u_radius, etalon_mean, sensor_field_radius, stat={}):
        self.dx = dx
        self.dy = dy
        self.u_radius = u_radius
        self.etalon_mean = etalon_mean
        self.sensor_field_radius = sensor_field_radius
        self.stat = stat

    def apply(self, pic, anchorx, anchory):
        X, Y = get_coords_less_or_eq_raduis(anchorx, anchory, self.u_radius)
        nearest_mean = make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon_mean) < abs(nearest_mean - self.etalon_mean):
                nearest_mean = mean
        return nearest_mean

def predictions_to_json(json_name, predictions):
    predictions_dicts = {}
    for prediction_id in predictions.keys():
        predictions_dicts[prediction_id] = vars(predictions[prediction_id])
    with open(json_name, 'w') as f:
        json.dump(predictions_dicts, f)

def predictions_from_json(json_name):
    predictions = {}
    if os.path.isfile(json_name):
        with open(json_name) as f:
            predictions_dicts = json.load(f)
            for prediction_id in predictions_dicts.keys():
                prediction = Prediction(**predictions_dicts[prediction_id])
                predictions[prediction_id] = prediction
            return predictions
    return None



def init_predictions_dict(pic, init_coords, u_radiuses, sensor_field_radiuses ):
    X, Y = select_coord_on_pic(pic)
    predictions_dict = {}
    for i in range(len(X)):
        dx = X[i] - init_coords[0]
        dy = Y[i] - init_coords[1]
        for u_radius in u_radiuses:
            for sensor_field_radius in sensor_field_radiuses:
                etalon_mean = make_measurement(pic, X[i], Y[i], sensor_field_radius)
                prediction = Prediction(dx, dy, u_radius, etalon_mean, sensor_field_radius)
                predictions_dict[str(uuid.uuid4())] = prediction
    return predictions_dict



if __name__ == "__main__":
    pics = etalons_of3()
    motif, init_coords = motif_from_json("simplest.motif")
    predictions = init_predictions_dict(pics[0], init_coords,  u_radiuses=[3], sensor_field_radiuses=[2,3])
    predictions_to_json("predict.predictions", predictions)
    predictions = predictions_from_json("predict.predictions")


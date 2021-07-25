# открываем файл с предикшенс
# открываем набор произвольных картинок
# случайным образом бегаем по случайным точкам картинок (берем их в качестве якорей)
# выводим статистику активаций в лог

from prediction_creator import *
from logger import *
from sensory_stat_data import get_hist

from random import choice
import random

def select_random_pic(pics):
    return choice(pics)

def select_random_xoord_on_pic(pic):
    maxX = pic.shape[1]
    maxY = pic.shape[0]
    x = random.randint(0, maxX-1)
    y = random.randint(0, maxY - 1)
    return x,y

def gather_activations_sample_for_prediction(prediction, pics, n_samples):
    activations = []
    for i in range(n_samples):
        pic = select_random_pic(pics)
        x,y = select_random_xoord_on_pic(pic)
        activation = prediction.apply(pic,x,y)
        activations.append(activation)
    return activations

def gather_stat_for_predictions_json(json_name):
    n_samples = 400
    pics = get_diverse_set_of_numbers(200)
    predictions = predictions_from_json(json_name)
    for prediction_id in predictions.keys():
        prediction = predictions[prediction_id]
        activations = gather_activations_sample_for_prediction(prediction, pics, n_samples)
        probs, bins = get_hist(activations, nbins=20)
        predictions[prediction_id].stat = {'probs':probs.tolist(), 'bins':bins.tolist()}
    predictions_to_json(json_name, predictions)

def visualise_stat(json_name):
    logger = HtmlLogger("NoConPred")
    predictions = predictions_from_json(json_name)
    for prediction_id in predictions.keys():
        prediction = predictions[prediction_id]
        logger.add_text(str(vars(prediction)))
        probs, bins = prediction.stat['probs'], prediction.stat['bins']
        fig = plot_probs_bins(probs, bins)
        logger.add_fig(fig)
    logger.close()

if __name__ == "__main__":
    json_name = "predict.predictions"
    gather_stat_for_predictions_json(json_name)
    visualise_stat(json_name)




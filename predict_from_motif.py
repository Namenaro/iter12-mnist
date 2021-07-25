import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from motif import *
from logger import *
from sensory_stat_data import get_hist
from create_motif import *
from init_motif import *
from data import *
from prediction_creator import *


def gather_stat_for_predictions(pics, motif, predictions):
    raw_acivations_data = {id:[] for id in list(predictions.keys())}
    for pic in pics:
        dict_coords_sprouts = motif.get_sprouts_for_all_pic(pic,  desired_num_of_full_sprouts=1)
        for coords in dict_coords_sprouts.keys():
            for prediction_id in predictions.keys():
                res = check_prediction(predictions[prediction_id], pic, coords[0], coords[1])
                raw_acivations_data[prediction_id] = raw_acivations_data[prediction_id] + res
    return raw_acivations_data


def check_prediction(prediction, pic, anchorx, anchory):   #return array!!!
    val = prediction.apply(pic, anchorx, anchory)
    return [val]


if __name__ == "__main__":
    logger = HtmlLogger("PRED")
    pics = etalons_of3()
    motif, _ = motif_from_json("simplest.motif")
    predictions = predictions_from_json("predict.predictions")

    raw_acivations_data = gather_stat_for_predictions(pics, motif, predictions)
    for prediction_key in predictions.keys():
        logger.add_text(str(vars(predictions[prediction_key])))
        activations= raw_acivations_data[prediction_key]
        logger.add_text("NUM_ACTIVATIONS="+ str(len(activations)))
        probs, bins = get_hist(activations, nbins=20)
        fig = plot_probs_bins(probs, bins)
        logger.add_fig(fig)
    logger.close()

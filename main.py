# нужно шас состряпать хтмл слдуюдего содержания:
# 1. Выбираем в качестве мотива одну точку на хвостике 3.Сохраняем джсон one.motif
# 2. в качестве предсказания выбираем точку рядом, на черном. Сохраняем джсон one.prediction
# 3. Выводим безуслвгую гистограмму по one.prediction
# 4. Выводим условную гистограмму по нему же относительно мотива.
# 5. В джсон рисуем картинку с тройкой + исходный мотив (по координате) + точка предсказания
# мы этот функционал далеаем как функцию, которая на вход принимает два джсона, и сохр.хтмлл с визуализацией
# и вызываем ее несколько раз, наращивая исходный мотив и наблюдая (?) падение энтропии предсказания.
# хтмлки кидаем себе на планшет и с ним мотаемся по нижнему.
from prediction_stat_data import *
from predict_from_motif import gather_stat_for_predictions
from create_motif import init_motif_handly, motif_to_json
from data import *

def draw_motif_and_preds(motif, init_coords, predictions):
    return fig

def make_exepriment_1(name):
    logger = HtmlLogger(name)
    # Создаем мотив, сохраняем
    json_name_motif = name + ".motif"
    motif, init_coords = init_motif_handly()
    motif_to_json(json_name_motif, motif, init_coords)

    # создаем предсказание, созраняем
    json_name_prediction = name+".prediction"
    predictions = init_predictions_dict(etalons_of3()[0], init_coords, u_radiuses=[3], sensor_field_radiuses=[2])
    predictions_to_json(json_name_prediction, predictions)

    # 3. Выводим безусловную гистограмму по one.prediction
    gather_stat_for_predictions_json(json_name_prediction)
    predictions = predictions_from_json(json_name_prediction)
    for prediction_id in predictions.keys():
        prediction = predictions[prediction_id]
        logger.add_text("Unconditional:")
        logger.add_text(str(vars(prediction)))
        probs, bins = prediction.stat['probs'], prediction.stat['bins']
        fig = plot_probs_bins(probs, bins)
        logger.add_fig(fig)

    # 4. Выводим условную гистограмму по нему же относительно мотива.
    raw_acivations_data = gather_stat_for_predictions(pics, motif, predictions)
    for prediction_key in predictions.keys():
        logger.add_text("Conditional:")
        activations = raw_acivations_data[prediction_key]
        logger.add_text("NUM_ACTIVATIONS=" + str(len(activations)))
        probs, bins = get_hist(activations, nbins=20)
        fig = plot_probs_bins(probs, bins)
        logger.add_fig(fig)

    # 5. В джсон рисуем картинку с тройкой + исходный мотив (по координате) + точка предсказания
    fig = draw_motif_and_preds(motif, init_coords, predictions)
    logger.add_fig(fig)

    logger.close()

if __name__ == "__main__":
    make_exepriment_1(logger_name="one")
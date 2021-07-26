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
from create_motif import motif_to_json
from init_motif import *
from data import *

def draw_motif_and_preds(motif, init_coords, predictions):
    pic = etalons_of3()[0]
    fig, ax = plt.subplots()
    ax.imshow(pic, cmap='gray_r')

    #draw motif
    X = [init_coords[0]]
    Y = [init_coords[1]]
    current_node = motif.first_node
    while True:
        if current_node.next_node is None:
            break
        current_node = current_node.next_node
        X.append[X[-1]+current_node.experiment.dx]
        Y.append[Y[-1] + current_node.experiment.dy]
        UX, UY = get_coords_less_or_eq_raduis(X[-1], Y[-1], current_node.experiment.u_radius)
        ax.scatter(UX, UY, s=100, c='blue', marker='o', alpha=0.4)
    ax.plot(X, Y, 'o-')
    # draw predictions
    for prediction_id in predictions.keys():
        prediction = predictions[prediction_id]
        x = X[0] + prediction.dx
        y = Y[0] + prediction.dy
        ax.scatter(x, y, s=100, c='green', marker='*', alpha=0.7)
        pX, pY = get_coords_less_or_eq_raduis(x, y, prediction.u_radius)
        ax.scatter(pX, pY, s=70, c='green', marker='*', alpha=0.5)

    return fig

def make_exepriment_1(name):
    logger = HtmlLogger(name)
    # Создаем мотив, сохраняем
    json_name_motif = name + ".motif"
    motif, init_coords = init_motif_handly()
    motif_to_json(json_name_motif, motif, init_coords)

    # создаем предсказание, созраняем
    json_name_prediction = name+".prediction"
    predictions = init_predictions_dict(etalons_of3()[0], init_coords, u_radiuses=[1], sensor_field_radiuses=[1])
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
    pics = etalons_of3()
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
    make_exepriment_1("one")
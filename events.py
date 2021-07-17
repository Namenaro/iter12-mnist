# здесь задача опять получить гистограмму для радиуса, но теперь с учетом неопределенности управления

# на входе для данного радиуса сенсорного поля мы имеем гистограмму вида:
# среднее значение поля - частота его встречания

# но поскольку мы предсказываем не точно, а примерно, то предсказания в общем случае будут носить вид:
# "в данном множесте управлений найдется хотя бы одно такое управление,
# что его сенсорный результат будет попадать в рамки данного события",
# события у нас те же - заданные бинами гистограммы.
#
# в итоговой гистогграмме должны быть те же бины, что и во входной. Но поскольку события не
# являются не совместными (теперь), то гистограмма это не распределеение вероятностей
# противоположность событию "найдется хотя бы один из данного бина" это "не найдется ни одного из данного бина".

from sensory_stat_data import get_hist_for_sensradius
from sensors import get_size_of_field_by_its_radius
from logger import *
from plotter import *

def get_hist_for_uradius_sensradius(sensor_field_radius, u_radius):
    probs, bins = get_hist_for_sensradius(sensor_field_radius)
    size_u_field = get_size_of_field_by_its_radius(u_radius)

    new_brobs = []
    for i in range(len(probs)):
        i_th_event_probability = probs[i]
        not_i_th_event_probability = 1 - i_th_event_probability
        p_of_not_even_one_in_u_set =  not_i_th_event_probability **size_u_field
        p_of_at_least_one_in_u_set = 1 - p_of_not_even_one_in_u_set
        new_brobs.append(p_of_at_least_one_in_u_set)

    return new_brobs, bins


if __name__ == "__main__":
    logger = HtmlLogger("EX0")
    sensor_field_radius = 7

    u_radius = 2
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    u_radius = 7
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    u_radius = 13
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    logger.close()


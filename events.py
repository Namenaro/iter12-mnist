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


def get_probability_of_eventA(minA, maxA, sensor_field_radius, u_radius ):
    probs, bins = get_hist_for_sensradius(sensor_field_radius)

    # найдем какие бины надо "слить" друг с другом, чтоб получить вероятность события А
    start_bin = None
    end_bin = None
    for j in range(len(bins)-1):
        if minA >= bins[j] and minA <=bins[j+1]:
            start_bin = j
        if maxA >= bins[j] and maxA <=bins[j+1]:
            end_bin = j

    # считаем вероятность события А без учета неопределенности по управлению
    A_probability = 0
    for j in range(start_bin, end_bin+1):
        A_probability += probs[j]

    # теперь учтем, что управлений множество, и надо чтоб "хотя бы одно" привело к А
    not_A_probability = 1 - A_probability
    size_u_field = get_size_of_field_by_its_radius(u_radius)
    p_of_not_even_one_in_u_set = not_A_probability ** size_u_field  # вер-ть, что для всех u выполнится !А
    p_of_at_least_one_in_u_set = 1 - p_of_not_even_one_in_u_set # вер-ть, что хотя бы для одного u выполнится А
    return p_of_at_least_one_in_u_set


if __name__ == "__main__":
    logger = HtmlLogger("EX1")
    sensor_field_radius = 1

    u_radius = 1
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    u_radius = 3
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    u_radius = 4
    probs, bins = get_hist_for_uradius_sensradius(sensor_field_radius, u_radius)
    logger.add_text("sensor_field_radius:" + str(sensor_field_radius))
    logger.add_text("u_radius:" + str(u_radius))
    fig = plot_probs_bins(probs, bins)
    logger.add_fig(fig)

    logger.close()
    print(get_probability_of_eventA(120, 140, sensor_field_radius=1, u_radius=1))


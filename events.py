# здесь задача опять получить гистограмму для радиуса, но теперь с учетом неопределенности управления

# на входе для данного радиуса сенсорного поля мы имеем гистограмму вида:
# среднее значение поля - частота его встречания

# но поскольку мы предсказываем не точно, а примерно, то предсказания в общем случае будут носить вид:
# "в данном множесте управлений найдется хотя бы одно такое управление,
# что его сенсорный результат будет попадать в рамки данного события",
# события у нас те же - заданные бинами гистограммы.
#
# в итоговой гистогграмме должны быть те же бины, что и во входной.
# противоположность событию "найдется хотя бы один из данного бина" это "не найдется ни одного из данного бина".

from naive_stat_data import get_hist_for_sensradius
from sensors import get_size_of_field_by_its_radius

def get_hist_for_uradius_sensradius(sensor_field_radius, u_radius):
    probs, bins = get_hist_for_sensradius(sensor_field_radius)
    size_u_field = get_size_of_field_by_its_radius(u_radius)

    new_brobs = []
    for i in range(len(probs)):
        i_th_event_probability = probs[i]
        not_i_th_event_probability = 1 - i_th_event_probability
        p_of_not_even_one_in_u_set = size_u_field * not_i_th_event_probability
        p_of_at_least_one_in_u_set = 1 - p_of_not_even_one_in_u_set
        new_brobs.append(p_of_at_least_one_in_u_set)

    return new_brobs, bins





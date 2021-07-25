# сравниваем два мотива  по предсказаельным качетсвам для заданного эксперимента
# при какой предыстории предсказание для заданного эксперимента будет самым информативным
# для каких еще она будет информативней чем учет лищь текщего эксперимента?


# Как выглядит законченный эксперимент N1 (предсказание без неопределенности по управлению):
# 1.сначала руками инициализируем мотив:
# (один или несколько кликов перемежаемых вводом сенсорного радиуса из консоли + вводом припуска на событие)
# 2.потом визуализируем мотив ( в виде результата применения к конкретной тройке).
# 3. потом руками инициализируем регионы влияния (один или несколько кликов, чтоб обозначить координаты +
#   хардкодим сенсорный раиус, единый для всех регионов).
# 4. потом для каждого из регионов, выставив ю-радуис в ноль, собираем выборку активаций в интересующем районе.
# 5. визуализируем -анализируем эту выборку по сравнению с известным безусловным расперделением.
#    - строим гистограмму с тем же кол-вом бинов, что и в умолчательных гистограммах (sensory_stat_data.py)
#    - кодом ильи проверяем гипотезу о том, что эта выбрка из распределения умолчательной гистограммы данного сенс-радиуса.
#    - меряем падение энтропии
# 6. результаты в ХТМЛ в след.виде:
# картинка с визуализаций мотива + для каждого региона картинка с визуализацией региона  + данные по ней:
# (2  гистограммы - эта и умолчательная, а также размер выборки, р-валью по стат.гипотезе)
# здесь стратегическая задача 1: посмотреть какие есть тенденции при вариации сенс-радиусов 1 и 2,
# и при увеличении-уменьшении сдвига ю. Верноли что при больших сенс радиусах даже тут появятся четкие
# отличия надежные отличия в гистограммах? Ну и код отладить для след.,буолее сложного эксперимента.

# Как выглядит законченный эксперимент N2 (учтем неопределенность по управлению в предсказании через мотив):
# (поначалу все так же как и в пролом экс:) -------
# 1.сначала руками инициализируем мотив:
# (один или несколько кликов перемежаемых вводом сенсорного радиуса из консоли + вводом припуска на событие)
# 2.потом визуализируем мотив ( в виде результата применения к конкретной тройке).
# 3. потом руками инициализируем регионы влияния (один или несколько кликов, чтоб обозначить координаты +
#   хардкодим сенсорный раиус, единый для всех регионов). Сренее в точке кликов сохраняем для обучения по образцу!

# 4. потом для каждого из регионов, перебираем возможные ю-радуисы! А именно:
# мы в каждой итерации этого вложенного цикла (по ю-радиусам) имеем точку, сенс-радиус, эталонное среднее и ю-радиус..
# а значит, можем при сборе статистики мотивом по этому региону работать с прото-экспериментом - хоть у нас пока не
# определено понятие события, в качестве "срабатывание" будем брать ближайшее к эталону среднее в ю-радиусе.
# Итого для каждого Ю-радиуса для данного региона мы имеем выбрку активаций.
# 5. Ее надо визуализировать: показать ее гистограмму с тем же кол-вом бинов, что и
# в гистограмме get_hist_for_uradius_sensradius(sensor_field_radius, u_radius). Сравнить визуально обе гистограммы.
# 6.  результаты в ХТМЛ в след.виде:
# # картинка с визуализаций мотива + для каждого региона картинка с визуализацией региона  + данные по ней
# (2  гистограммы - эта и умолчательная, размер выборки, р-валью по стат.гипотезе ИЛЬИ)
# здесь стратегическая задача1: научиться выбирать событие для этого протоэксперимента (Бмин,Бмакс).
#  стратегическая задача2: показать что мотиву 1(точка на хвостике) придает предсказательности добавление
#  в мотив точки на др.хвостике.

class Foo:
    def __init__(self,dic):
        self.dic = dic

m = {'r':[2, 5], 'l':55}

foo = Foo(m)
v = vars(foo)

bar = Foo(v)
print (bar.dic)
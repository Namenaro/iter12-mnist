# фрагмент долговревенной памяти
# крепится к другим ее фрагментам
from sensors import *

class ExperimentLongTerm:
    def __init__(self,dx, dy, u_radius, sensor_field_radius, ed_min, ed_max):
        # управление
        self.dx = dx
        self.dy = dy

        # неопределенность управления
        self.u_radius = u_radius

        # сенсорное измерение после управления
        self.sensor_field_radius = sensor_field_radius

        # регистрация сенсорного события (было/не было)
        self.event_detector_min = ed_min
        self.event_detector_max = ed_max


    def make(self, pic, x, y):
        expected_x = x + self.dx
        expected_y = y + self.dy
        for r in range(0, self.u_radius + 1):
            X, Y = get_coords_for_radius(expected_x, expected_y, r)
            for i in range(len(X)):
                mean = make_measurement(pic, X[i], Y[i], r)
                if mean >= self.event_detector_min and mean <= self.event_detector_max:
                    return True
        return False

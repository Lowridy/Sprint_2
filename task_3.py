class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        return 101 - place


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        return meters * 0.5


class TotalPoints:
    @staticmethod
    def get_total_points(meters, place):
        place_points = PointsForPlace.get_points_for_place(place)
        meters_points = PointsForMeters.get_points_for_meters(meters)
        return place_points + meters_points


# Проверка работы (как в задании)
print(PointsForPlace.get_points_for_place(10))
print(PointsForMeters.get_points_for_meters(10))
print(TotalPoints.get_total_points(100, 10))
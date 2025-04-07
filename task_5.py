class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"
    
    def total_points(self):
        points = 3 * self.victories + self.draws
        return f"Общее количество очков: {points}"


class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"
    
    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"


# Создаем объекты
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Вызываем методы для football_team
print(football_team.number_of_wins())
print(football_team.number_of_draws())
print(football_team.number_of_losses())
print(football_team.total_points())

# Вызываем методы для hockey_team
print(hockey_team.number_of_wins())
print(hockey_team.number_of_draws())
print(hockey_team.number_of_losses())
print(hockey_team.total_points())

# С использованием цикла
teams = [football_team, hockey_team]
for team in teams:
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
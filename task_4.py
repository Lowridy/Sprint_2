class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, rest_days):
        if rest_days is None:
            return 0
        return (7 - rest_days) * 8
    
    @classmethod
    def get_email(cls, name):
        if name is None:
            return None
        return f"{name.lower().replace(' ', '.')}@email.com"
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        actual_hours = self.hours if self.hours is not None else self.get_hours(self.rest_days)
        return actual_hours * self.hourly_payment
    
    # Проверка:
worker = EmployeeSalary("Иван Иванов", hours=28,)
print(f"Зарплата: {worker.salary()}")
print(f"Email: {worker.get_email("Иван Иванов")}")
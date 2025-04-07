class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email=None):
        hours = (7 - rest_days) * 8 if rest_days is not None else None
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f"{name.lower().replace(' ', '.')}@email.com" if name else None
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        actual_hours = self.hours if self.hours is not None else self.get_hours(self.rest_days)
        return actual_hours * self.hourly_payment
    
    # Проверка:
worker = EmployeeSalary("Иван Иванов", hours=28,)
print(f"Зарплата: {worker.salary()}")

worker_with_email = EmployeeSalary.get_email("Иван Иванов", hours=28)
print(f"Email: {worker_with_email.email}")

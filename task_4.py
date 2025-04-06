class EmployeeSalary:
    hourly_payment = 400 
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    def get_hours(self):
        if self.hours is None:
            if self.rest_days is None:
                return 0
            self.hours = (7 - self.rest_days) * 8
        return self.hours
    
    def get_email(self):
        if self.email is None:
            self.email = f"{self.name.lower().replace(' ', '.')}@email.com"
        return self.email
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        return self.get_hours() * self.hourly_payment
    
    # Проверка:
worker = EmployeeSalary("Иван Иванов", hours=28,)
print(f"Зарплата: {worker.salary()}")
print(f"Email: {worker.get_email()}")
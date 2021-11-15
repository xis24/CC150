import datetime


class Employee:
    def __init__(self, name, salary, hired_date, left_date=None) -> None:
        self.name = name
        self.salary = salary
        self.start_date = datetime.datetime.strptime(hired_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(left_date, '%Y-%m-%d')

    def salaryInYear(self, year):
        if year < self.start_date.year or year > self.end_date.year:
            raise Exception("invalid input")
        delta = self.end_date - self.start_date
        if delta.days < 365:
            return self.salary // 365 * delta.days
        if self.end_date.year == year:
            firstDay = datetime.datetime.strptime(
                str(year)+"-01-01", '%Y-%m-%d')
            return self.salary // 365 * ((self.end_date - firstDay).days)
        else:
            return self.salary


if __name__ == '__main__':
    obj = Employee('leo', 400000, '2021-1-1', '2024-6-30')
    obj2 = Employee('david', 600000, '2021-1-1', '2021-6-30')

    print(obj.salaryInYear(2024))
    # print(obj.salaryInYear(2020))
    # print(obj.salaryInYear(2025))
    print(obj2.salaryInYear(2021))

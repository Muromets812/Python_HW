import datetime as dt
from application.salary import salary_func
from application.db.people import people_func


if __name__ == '__main__':
    salary_func()
    people_func()
    print(dt.datetime.now())
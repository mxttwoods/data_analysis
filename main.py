from attrs import define, asdict
import pandas as pd
import matplotlib.pyplot as plt


@define(slots=False)
class Person(object):
    name: int
    age: int

    @property
    def get_name(self):
        return self.name


@define(slots=False)
class User(object):
    user_id: int

    @property
    def get_user_id(self):
        return self.user_id


@define(slots=True, frozen=True)
class Student(Person, User):
    student_id: int

    @property
    def get_student_id(self):
        return self.student_id

    def do_something(self):
        self.df: pd.DataFrame = pd.read_csv(
            "https://people.sc.fsu.edu/~jburkardt/data/csv/zillow.csv"
        )
        print(self.df.head())


student = Student(name="Chris", age=32, user_id="ctao", student_id=1234567890)
student.student_id = 3

print(student.student_id)

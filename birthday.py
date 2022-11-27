import csv
import dataclasses
import datetime


@dataclasses.dataclass
class NameAndBirthday:
    name: str
    month: int
    day: int


class NameAndBirthdayList:
    def __init__(self):
        with open("birthday_list.csv") as f:
            reader = csv.reader(f)
            self.birthday_list = [
                NameAndBirthday(name=row[0], month=int(row[1]), day=int(row[2]))
                for row in reader
                ]

    def get_birthday_people(self) -> list[NameAndBirthday]:
        today = datetime.date.today()
        birthday_people = [person
                           for person in self.birthday_list
                           if person.month == today.month
                           and person.day == today.day]
        return birthday_people

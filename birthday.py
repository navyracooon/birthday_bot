import os
import datetime
import pytz

class Birthday:
    def __init__(self, index):

        birthday_list = eval(os.environ["BIRTHDAY_LIST"])

        birthday_pair = birthday_list[index]
        self.name = birthday_pair[0]
        self.date = birthday_pair[1].split("/")
        self.len = len(birthday_list)

    def is_today_birthday(self):
        now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        if now.month == int(self.date[0]) and now.day == int(self.date[1]):
            return True
        else:
            return False


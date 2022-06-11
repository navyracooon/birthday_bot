import datetime
import pytz

class Birthday:
    def __init__(self, index):
        birthday_files = open('birthday_files.txt', 'r', encoding = 'utf_8')
        birthday_lines = birthday_files.readlines()
        birthday_files.close()

        birthday_line = birthday_lines[index].rstrip('\n')
        birthday_pair = birthday_line.split()
        self.name = birthday_pair[0]
        self.date = birthday_pair[1].split("/")
        self.len = len(birthday_lines)

    def is_today_birthday(self):
        now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        if now.month == int(self.date[0]) and now.day == int(self.date[1]):
            return True
        else:
            return False


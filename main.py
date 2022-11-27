import os

from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv

from birthday import NameAndBirthdayList


def main():
    load_dotenv(".env")

    CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
    GROUP_ID = os.getenv("GROUP_ID")

    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    name_and_birthday_list = NameAndBirthdayList()
    birthday_person_list = name_and_birthday_list.get_birthday_people()

    include_message = ""

    for person in birthday_person_list:
        if person != birthday_person_list[-1]:
            include_message += person.name + "さんと"
        else:
            include_message += person.name + "さん"

    output_message = f"今日は{include_message}の誕生日です！\nおめでとうございます！🎉🎉"

    if len(birthday_person_list) != 0:
        line_bot_api.push_message(
            GROUP_ID, TextSendMessage(text=output_message))


if __name__ == "__main__":
    main()

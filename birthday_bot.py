from slack_sdk import WebClient
import datetime as dt
import attr
import csv
import os


@attr.s(auto_attribs=True, frozen=True)
class Birthday:
    name: str
    date_of_birth_string: str
    user_id: str

    def congratulation_string(self):
        return f'Happy birthday to {self.name}! {self.user_id}! :balloon: :cake:'

    def is_celebrated(self, date):
        return date == self.date_of_birth_string


def read_csv(file_name):
    with open(file_name, 'r') as birthdays:
        birthday_list = []

        csv_reader = csv.reader(birthdays, delimiter=',')
        next(csv_reader)  # Remove headers

        for row in csv_reader:
            name, date, month, user_id = row
            birthday = Birthday(name, f'{date}-{month}', user_id)
            birthday_list.append(birthday)

    return birthday_list


def birthday_bot(birthdays, slack_token):
    """
    Check if there is a birthday today
    """
    today = f'{dt.date.today():%d-%m}'
    slack_client = WebClient(token=slack_token)  # OAuth token
    for birthday in birthdays:
        if birthday.is_celebrated(today):
            slack_client.chat_postMessage(
                channel=channel, text=birthday.congratulation_string())


if __name__ == '__main__':
    token = os.environ['SLACK_BOT_TOKEN']
    channel = os.environ['BIRTHDAY_BOT_CHANNEL'] 
    birthday_bot(birthdays=read_csv('birthdays.csv'), slack_token=token)

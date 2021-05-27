# Importing libraries
from slack_sdk import WebClient
from dotenv import load_dotenv
import datetime as dt
import attr
import csv
import os

# Defining the Birthday-class.
@attr.s(auto_attribs=True, frozen=True)
class Birthday:
    name: str
    date_of_birth_string: str
    user_id: str


# Reading the .csv-file
def read_csv(file_name):
    with open(file_name, 'r') as birthdays:
        birthday_list = []
    
        csv_reader = csv.reader(birthdays, delimiter=',')
        next(csv_reader)  # Getting rid of headers
        
        # Looping through rows and appends birthdays to the birthday list. 
        for row in csv_reader:
            name, date, month, user_id = row
            birthday = Birthday(name, f'{date}-{month}', user_id)
            birthday_list.append(birthday)
    return birthday_list


# Check if there is a birthday today
def birthday_bot(birthdays, slack_token):
    today = f'{dt.date.today():%d-%m}'
    slack_client = WebClient(slack_token)  # Slack API OAuth token
    for date_of_birth in birthdays:
        # If birthday == True: post message!
        if today == date_of_birth.date_of_birth_string:
            message = f'Happy birthday to {date_of_birth.name}! {date_of_birth.user_id}! :balloon: :cake:'
            slack_client.chat_postMessage(channel=channel, text=message)


if __name__ == '__main__':
    load_dotenv()  # Loading token and channel from .env file
    token = os.environ.get('SLACK_BOT_TOKEN')
    channel = os.environ.get('BIRTHDAY_BOT_CHANNEL')  # Channel to post to
    birthday_bot(birthdays=read_csv('birthdays.csv'), slack_token=token)

import sys
from fileinput import close

from pyautogui import click

from steps.steps import *
import time
from functions.get_csv_data import *


emails_array = get_emails_array()

open_edge()
time.sleep(4)

search_gmail()
time.sleep(10)

for email in emails_array:
    click_write_email_button()
    time.sleep(6)

    click_button_destination()
    write_text(email['destination'])

    click_button_subject()
    write_text(email['subject'])

    click_button_body()
    write_text(email['body'])
    time.sleep(3)

    press_send_email()
    time.sleep(4)

close_browser()
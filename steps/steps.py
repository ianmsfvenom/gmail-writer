import time

import pyautogui as pag
from pyautogui import ImageNotFoundException

from utils.screen import *

pag.FAILSAFE = False

def open_edge():
    pag.click(adapt_pos_x(174), adapt_pos_y(1065))
    pag.write('microsoft edge')
    time.sleep(3)
    pag.click(adapt_pos_x(213), adapt_pos_y(517))


def search_gmail():
    pag.click(adapt_pos_x(414), adapt_pos_y(52))
    pag.write('https://mail.google.com/mail/u/0/#inbox')
    pag.press('enter')


def click_write_email_button():
    while True:
        try:
            send_button = pag.locateOnScreen("./images/send_email_button.png", confidence=0.6)
            pag.click(pag.center(send_button))
            break
        except ImageNotFoundException:
            time.sleep(4)

def click_button_destination():
    while True:
        try:
            to_button = pag.locateOnScreen("./images/to_field_button.png", confidence=0.6)
            pag.click(pag.center(to_button))
            break
        except ImageNotFoundException:
            time.sleep(4)

def click_button_subject():
    pag.click(adapt_pos_x(1701), adapt_pos_y(484))

def click_button_body():
    pag.click(adapt_pos_x(1304), adapt_pos_y(639))

def press_send_email():
    pag.hotkey('ctrl', 'enter')

def write_text(text):
    pag.write(text)

def close_browser():
    pag.hotkey('alt', 'f4')

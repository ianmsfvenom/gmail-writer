import tkinter as tk

base_screen_x = 1920  # Coordenada x base que serão adaptadas
base_screen_y = 1080  # Coordenada y base que serão adaptadas
root_screen = tk.Tk()  # Consultar telas X e Y da máquina


def adapt_pos_x(x):
    device_x = root_screen.winfo_screenwidth()
    percent_x = (device_x / base_screen_x)
    result_x = x * percent_x
    return result_x


def adapt_pos_y(y):
    device_y = root_screen.winfo_screenheight()
    percent_y = (device_y / base_screen_y)
    result_y = y * percent_y
    return result_y

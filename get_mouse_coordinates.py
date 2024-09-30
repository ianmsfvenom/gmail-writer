import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Cria uma nova janela no topo

# Função para obter coordenadas do mouse
def get_mouse_position():
    x, y = pyautogui.position()
    return x, y

# Movendo o mouse para a coordenada obtida
def move_mouse_to_position(x, y):
    pyautogui.moveTo(x, y, duration=1)  # Movendo com duração de 1 segundo

# Script principal
if __name__ == "__main__":
    print("Posicione o mouse no ponto desejado e aguarde 5 segundos...")
    time.sleep(10)  # Espera 10 segundos para o usuário posicionar o mouse
    x, y = get_mouse_position()
    messagebox.showinfo("Coordenadas", f"Coordenadas obtidas: X={x}, Y={y}")


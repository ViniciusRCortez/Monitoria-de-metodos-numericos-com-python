from Metodos_numericos.metodos import *
import numpy as np
import pandas as pd
from math import exp
import pyautogui
from time import sleep

'''sleep(5)
a = pyautogui.position()
pyautogui.position()
print(a)
'''
pyautogui.alert('Vou começar, não mecha')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('google chrome')
pyautogui.press('ENTER')
sleep(5)
pyautogui.click(x=707, y=429)
sleep(2.5)
pyautogui.click(x=509, y=51)
pyautogui.press('SPACE')

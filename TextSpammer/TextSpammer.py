# TextSpammer.py
# Robin Martinez
# 04/13/2021

import time
import pyautogui
import sys


TEXT_PATHNAME = 'type a pathname'

def spam():
	time.sleep(2)
	with open(TEXT_PATHNAME) as f:
		lines = f.readlines()
	for line in lines:
		pyautogui.typewrite(line.strip())
		pyautogui.press('enter')

spam()

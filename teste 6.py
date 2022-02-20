import pyautogui
import time

#Point(x=609, y=745) "Feed"
#Point(x=998, y=240) "Detalhes"
#Point(x=1235, y=324) "Excluir"
#Point(x=1262, y=525) "Fechar"

time.sleep(5)

pyautogui.click(x=609, y=745)

for i in range(316):
    pyautogui.click(x=998, y=240)
    pyautogui.click(x=1235, y=324)
    pyautogui.click(x=1235, y=324)
    pyautogui.click(x=1235, y=324)
    pyautogui.click(x=1262, y=525)


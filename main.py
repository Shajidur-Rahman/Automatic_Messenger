number_of_message = int(input("How many message do you want to send? "))
import pyautogui
import time
message = 0
while message < number_of_message:
    time.sleep(2)
    pyautogui.typewrite('hello we make song and programming projects. Now i made a project called automatic messenger')
    pyautogui.press('enter')
    message = 1 + message


import pyautogui
import time 
def Greet(name):
    greeting_message = f"hello, {name}! k xa nani babu"
    return greeting_message

time.sleep(2)

my_guest = ['raaz','sandesh','bijaya','abhinav''raaz','sandesh','bijaya','abhinav']

for guest in my_guest:
    greet_message= Greet(guest)
    time.sleep(2)
    pyautogui.write(greet_message)
    pyautogui.press('enter')

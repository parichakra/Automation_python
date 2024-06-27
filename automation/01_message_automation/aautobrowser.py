import pyautogui
import time 
# pyautogui.moveTo(700,10 , duration=2)

# pyautogui.click(700,10)

# pyautogui.write("I am writing this message")



tab_links= ['https://www.youtube.com/']


time.sleep(2)

def open_browser(browser_name):
    pyautogui.press('win')
    
    pyautogui.write(browser_name, interval= 1)
    pyautogui.press('enter')

def launch_site_in_newtab(url):
    pyautogui.write(url)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','t')
    

    time.sleep(2)
    pyautogui.write(url)
    pyautogui.press('enter')
    

open_browser('edge')
time.sleep(2)
for link in tab_links:
    launch_site_in_newtab(link)

time.sleep(2)

pyautogui.moveTo(460,150, duration=2)

pyautogui.click(460,150)
time.sleep(2)
pyautogui.write("yellow song cold play ")
pyautogui.press('enter')


time.sleep(2)

pyautogui.click(430,650)





# pyautogui.alert('all tabs opened successfully')

#3rd
# # mposition= pyautogui.displayMousePosition()
# print(mposition)

# screen_width, screen_height = pyautogui.size()
# print(f"Screen resolution: {screen_width},{screen_height}")
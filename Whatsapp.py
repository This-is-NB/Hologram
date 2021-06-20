import webbrowser as web
from urllib.parse import quote
import time
import pyautogui as pg

def close_tab(wait_time: int = 2):
    """Closes the Currently Opened Browser Tab"""
    time.sleep(wait_time)
    pg.hotkey("ctrl", "w")
    pg.press("enter")

def sendwhatsappmsg(phone_no, message, wait_time= 20, tab_close= False,browser= None):
    parsed_message = quote(message)
    web.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + parsed_message)
    time.sleep(2)
    width, height = pg.size()
    if browser:
        whats = pg.getWindowsWithTitle(browser)[0]
        whats.maximize()
        whats.activate()
    pg.click(width / 2, height / 2)
    time.sleep(wait_time - 2)
    pg.press('enter')
    if tab_close:
        close_tab()
        
if __name__=="__main__":
    sendwhatsappmsg("+91 9315171849","testing\nsdfgh",12)
import os
import time
import random

import webbrowser
import pyautogui
import pyperclip
from bs4 import BeautifulSoup

from dotenv import load_dotenv

load_dotenv()
SCRAPING_RESULT_DIRECTORY = os.environ.get("SCRAPING_RESULT_DIRECTORY")
os.makedirs(SCRAPING_RESULT_DIRECTORY, exist_ok=True)


def scrape(url: str, filename: str) -> None:
    """
    Scrape the website and save the rendered page source to specified path.
    :param url: url to scrape
    :param filename: filename to save, with json as file extension included
    :return:
    """
    webbrowser.open(url)
    time.sleep(random.uniform(1, 3))
    # scroll down to render the page
    pyautogui.scroll(-1000)
    time.sleep(random.uniform(1, 3))
    # inspect
    pyautogui.hotkey("option", "command", "c")
    time.sleep(random.uniform(1, 3))
    # input in console
    pyautogui.typewrite("copy(document.body.innerHTML);")
    time.sleep(random.uniform(1, 3))
    pyautogui.press("enter")
    time.sleep(random.uniform(1, 3))
    # save rendered page source
    text = pyperclip.paste()
    soup = BeautifulSoup(text, "html.parser")
    formatted_source = soup.prettify()
    with open(os.path.join(SCRAPING_RESULT_DIRECTORY, filename), "w", encoding="utf-8") as f:
        f.write(str(formatted_source))
    # close developer tools
    pyautogui.hotkey("option", "command", "i")
    # close the active tab
    pyautogui.hotkey("command", "w")
    print(f"Scraping Successful, saved to {os.path.join(SCRAPING_RESULT_DIRECTORY, filename)}")

# `pyautogui` Scraper
Web Scraping using pyautogui in attempt to bypass cloudflare protection.

## Usage
1. Set the `SCRAPING_RESULT_DIRECTORY` in `.env`
2. Call `scrape(url: str, filename: str)` function to scrape

It will open the website in the browser and save the rendered source code. Please do not be alarmed when you see it happens. 

## To do
- Add human-like mouse movement and delays.
- Adapt daemon process so it can run in the background.

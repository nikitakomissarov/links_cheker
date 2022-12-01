import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of

class Clicks:

    def clicking(self, clicklist, browser):
        handles = browser.window_handles
        cur_win = browser.current_window_handle
        for i in clicklist:
            i.click()
            print(handles)
            # browser.switch_to_window([win for win in browser.window_handles if win != cur_win][0])
            browser.switch_to_window(cur_win)



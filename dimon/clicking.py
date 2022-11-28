class Clicks:
    def __init__(self, browser):
        self.browser = browser

    def clicking(self):
        try:
            for i in clicklist:
                print(i.get_attribute('outerHTML'))
                i.click()
                print('сlick')
        finally:
            print(clicklist)

from selenium import webdriver

from src.abstract.LoggerAbstract import LoggerAbstract


class Screenshot(LoggerAbstract):
    def take_image(self, link: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        try:
            with webdriver.Chrome("/usr/local/bin/chromedriver", options=options) as browser:
                browser.get(link)
            return browser.get_screenshot_as_png()
        except Exception as e:
            self.logger.error(e)
            return None

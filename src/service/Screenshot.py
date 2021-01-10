from selenium import webdriver

from src.abstract.LoggerAbstract import LoggerAbstract


class Screenshot(LoggerAbstract):
    def take_image(self, link: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('window-size=1280x720')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        try:
            with webdriver.Chrome("/usr/local/bin/chromedriver", options=options) as browser:
                browser.set_script_timeout(30)
                browser.set_page_load_timeout(30)
                browser.get(link)
            return browser.get_screenshot_as_png()
        except Exception as e:
            self.logger.error(f'{e}, link:{link}', exc_info=True)

            return None

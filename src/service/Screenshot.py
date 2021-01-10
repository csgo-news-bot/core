from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.ConfigService import ConfigService


class Screenshot(LoggerAbstract):
    config: ConfigService

    def __init__(self):
        super(Screenshot, self).__init__()
        self.config = ConfigService()

    def take_image(self, link: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('window-size=1280x720')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        while True:
            try:
                with webdriver.Remote(
                    command_executor=f'{self.config.get_url_selenium()}/wd/hub',
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options
                ) as browser:
                    browser.set_script_timeout(30)
                    browser.set_page_load_timeout(30)
                    browser.get(link)
                return browser.get_screenshot_as_png()
            except Exception as e:
                self.logger.error(f'{e}, link:{link}', exc_info=True)

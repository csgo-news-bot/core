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
        command_executor = f'{self.config.get_url_selenium()}/wd/hub'

        try:
            browser = webdriver.Remote(
                command_executor=command_executor,
                desired_capabilities=DesiredCapabilities.CHROME,
                options=options
            )
            browser.get(link)
            result = browser.get_screenshot_as_png()
            browser.quit()

            return result
        except Exception as e:
            self.logger.error(f'{e}, link:{link}', exc_info=True)

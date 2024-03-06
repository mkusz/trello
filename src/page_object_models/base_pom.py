import logging
import urllib.parse
from typing import Optional
from typing import Pattern
from typing import Union

import playwright.sync_api as playwright
import playwright.sync_api._generated as playwright_generated

from src import configs


def _logger() -> logging.Logger:
    return logging.getLogger(__name__)


class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self.page: playwright.Page = page
        self.env: configs.EnvConfig = configs.EnvConfig()
        self.playwright: configs.PlaywrightConfig = configs.PlaywrightConfig()
        self._expect = playwright.Expect()
        self._expect.set_options(timeout=self.playwright.elements_timeout_sec * 1000)

    @property
    def default_url(self):
        """Returns default url of the given web page"""
        raise NotImplementedError

    def is_opened(self, selector: str):
        """Check is given POM opened (have to implemented inside given POM)"""
        raise NotImplementedError

    def expect(
        self,
        selector: str,
        has_text: Optional[Union[str, Pattern[str]]] = None,
        has_not_text: Optional[Union[str, Pattern[str]]] = None,
        has_locator: Optional[playwright.Locator] = None,
        has_not_locator: Optional[playwright.Locator] = None,
    ) -> playwright_generated.LocatorAssertions:
        locator: playwright.Locator = self.page.locator(
            selector=selector,
            has_text=has_text,
            has_not_text=has_not_text,
            has=has_locator,
            has_not=has_not_locator,
        )
        return self._expect(actual=locator)

    def goto(self, params: Optional[dict] = None):
        if params:
            url_params = urllib.parse.urlencode(params)
            url = f"{self.default_url}?{url_params}"
        else:
            url = self.default_url
        _logger().debug(f"Go to: {url}")
        self.page.goto(url)

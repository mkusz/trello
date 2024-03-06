import logging


def log() -> logging.Logger:
    return logging.getLogger(__name__)


def test_temp_open_trello(playwright_page, env_config):
    playwright_page.goto(env_config.url_ui)
    log().info("test")
    # playwright_page.wait_for_timeout(10000)

def test_temp_open_trello(playwright_page, env_config):
    playwright_page.goto(env_config.url_ui)
    playwright_page.wait_for_timeout(10000)

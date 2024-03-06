from typing import Optional
import pydantic_settings


class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(env_prefix="QA_ENV_", frozen=True)

    artifacts_dir: str = "artifacts/"
    artifacts_remove_old: bool = True
    url_ui: Optional[str] = None
    user: Optional[str] = ""
    password: Optional[str] = ""


class PlaywrightConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(env_prefix="QA_PLAYWRIGHT_", frozen=True)

    browser: str = "chromium"
    headless: bool = False
    navigation_timeout_sec: int = 120
    elements_timeout_sec: int = 60
    tracing_enable: bool = False
    tracing_screenshots: bool = True
    tracing_snapshots: bool = True

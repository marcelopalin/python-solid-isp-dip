"""
    Descrição:
    Explicando como funciona os Princípios SOLID em Python.

    Author:           @MarceloPalin
    Created:          2021-07-18
"""

try:
    from pathlib import Path

    from pyfiglet import Figlet

    from src.config import settings
    from src.init_loguru import get_loguru_logger, init_loguru

    init_loguru(
        file_path=Path(settings.LOG_MONITOR),
        diagnose=True,
        backtrace=True,
    )
    logger = get_loguru_logger()

except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")


@logger.catch
def main():
    logger.info("-" * 80)
    fmt_font = Figlet(font="standard")
    if settings.DEBUG:
        logger.info("\n" + fmt_font.renderText("DEBUG"))
    if settings.CURRENT_ENV == "development":
        logger.info("\n" + fmt_font.renderText("DEV"))
    logger.info("-" * 80)


if __name__ == "__main__":
    main()

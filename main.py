
"""
    Descrição:
    Explicando como funciona os Princípios SOLID em Python.

    Author:           @MarceloPalin
    Created:          2021-07-18
"""

try:
    from pathlib import Path
    from src.init_loguru import init_loguru, get_loguru_logger
    from pyfiglet import Figlet
    from termcolor import colored

    from config import settings

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
        logger.info("\n" + colored(fmt_font.renderText("DEBUG"), color="yellow"))
    if settings.CURRENT_ENV == 'development':
        logger.info("\n" + colored(fmt_font.renderText("DEV"), color="yellow"))
    logger.info("\n" + colored(fmt_font.renderText("SOLID"), color="yellow"))
    logger.info("-" * 80)

if __name__ == '__main__':
    main()
    
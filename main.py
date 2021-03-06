"""
    Descrição:
    Explicando como funciona os Princípios SOLID em Python.

    Author:           @MarceloPalin
    Created:          2021-07-18
"""

try:
    from asyncio import run
    from pathlib import Path

    from pyfiglet import Figlet

    from src.config import settings
    from src.infra.config import Base, DBConnectionHandler
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


async def create_database():
    dbconn = DBConnectionHandler()
    async with dbconn.get_engine().begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@logger.catch
def main():
    logger.info("-" * 80)
    fmt_font = Figlet(font="standard")
    if settings.DEBUG:
        logger.info("\n" + fmt_font.renderText("DEBUG"))
    if settings.CURRENT_ENV == "development":
        logger.info("\n" + fmt_font.renderText("DEV"))
    logger.info("-" * 80)
    run(create_database())


if __name__ == "__main__":
    main()

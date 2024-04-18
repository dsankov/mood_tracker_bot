import asyncio
from loguru import logger


async def main() -> None:

    logger.add(
        "logs/debug.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="30 KB",
        compression="zip",
    )

    logger.debug("Start logging")


if __name__ == "__main__":
    asyncio.run(main=main())

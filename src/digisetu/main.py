import logging

from digisetu.core.logging import setup_logging

from digisetu.core.exceptions import DigiSetuError

def main() -> None:
    setup_logging()

    logger = logging.getLogger(__name__)
    try:

        raise DigiSetuError("Something went wrong in digisetu")
    
    except DigiSetuError as error:

        logger.error("Application error: %s", error)
    # logger.info("DigiSetu application started")
    # logger.warning("This is a test warning")


if __name__ == "__main__":
    main()
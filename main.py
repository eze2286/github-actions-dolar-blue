import requests
import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    url = 'https://api.bluelytics.com.ar/v2/latest'
    api_result = requests.get(url)

    api_response = api_result.json()
    dolar_blue_last_price_sell = (api_response["blue"]["value_sell"])
    dolar_blue_last_price_buy = (api_response["blue"]["value_buy"])
    logger.info(f'Dolar Blue buy: {dolar_blue_last_price_buy} - Dolar Blue sell: {dolar_blue_last_price_sell}')



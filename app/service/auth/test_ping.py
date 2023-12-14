import requests

from app.model.static_globals import TEST_PING_URL
from app.service.logger import logger


def test_ping() -> bool:
    try:
        logger.info(f'Test ping to {TEST_PING_URL}')
        ping = requests.get(TEST_PING_URL).status_code
        if ping == 200:
            logger.info(f'Test ping to {TEST_PING_URL}. Response: 200')
            return True
    except:
        logger.info(f'Test ping to {TEST_PING_URL}. Failed')
    return False

import datetime

import coloredlogs
import logging
from pathlib import Path

from app.model.static_globals import LOG_PATH

log_format = '[%(asctime)s.%(msecs)03d] %(levelname)-9s %(filename)-27s %(message)s'

logger = logging.getLogger(__name__)
coloredlogs.DEFAULT_LEVEL_STYLES['info'] = dict(color='green')
coloredlogs.DEFAULT_LEVEL_STYLES['debug'] = dict(color='white')
coloredlogs.DEFAULT_FIELD_STYLES['asctime'] = dict(color='white')
coloredlogs.DEFAULT_FIELD_STYLES['levelname'] = dict(color='blue')
coloredlogs.DEFAULT_FIELD_STYLES['filename'] = dict(color='blue')

coloredlogs.install(level='DEBUG', logger=logger, fmt=log_format)


log_dir = Path(LOG_PATH)
log_dir.mkdir(exist_ok=True, parents=True)


path = log_dir / Path(f'{datetime.datetime.now().strftime("__%Y.%m.%d__%H.%M")}__.log')


formatter = logging.Formatter(log_format)
handler = logging.FileHandler(path, mode='w')
handler.setFormatter(formatter)

logger.addHandler(handler)

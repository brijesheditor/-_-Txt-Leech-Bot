# Don't Remove Credit Tg - @Oye_brijesh
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@bk_classes_28?si=hpJOu1O3DPqF3dTT
# Ask Doubt on telegram @Oye_brijesh

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.ERROR,
    format=
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


logging = logging.getLogger()

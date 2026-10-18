import logging
import sys
from pythonjsonlogger import jsonlogger


def setup_logger():
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging.INFO)

    # Evita duplicar handlers si se llama varias veces
    if not logger.handlers:
        log_handler = logging.StreamHandler(sys.stdout)

        # Formato JSON con los campos exigidos por la consigna
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(path)s %(status_code)s %(message)s",
            rename_fields={"asctime": "timestamp", "levelname": "level"},
        )
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)

    return logger


# Esta línea es fundamental para que main.py pueda importar 'logger'
logger = setup_logger()
import logging as python_logging
import time

python_logging.basicConfig(
    level=python_logging.DEBUG,
    format="%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s]  %(message)s",
    filename="debug.log"
)
python_logging.Formatter.converter = time.gmtime
logging = python_logging
logging.info('Logging configured')

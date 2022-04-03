import logging as python_logging

python_logging.basicConfig(
    level=python_logging.INFO,
    format="%(asctime)s [%(threadName)s] [%(name)s] [%(levelname)s]  %(message)s",
    handlers=[
        python_logging.FileHandler("debug.log"),
        python_logging.StreamHandler()
    ]
)
logging = python_logging
logging.info('Logging configured')

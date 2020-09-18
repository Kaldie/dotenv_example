from dotenv import load_dotenv

import logging
import os

load_dotenv()

variable = os.getenv("VARIABLE")
password = os.getenv("PASSWORD")
key = os.getenv("KEY")

logging.warning('variable %s', variable)
logging.warning('password %s', password)
logging.warning('key %s', key)

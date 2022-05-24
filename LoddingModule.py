import logging
from main import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename='Python_calc\calc.log')
logging.info(f'Run : {start}')
logging.debug(f'First number: {a}')
logging.debug(f'Two number: {b}')
logging.info(f'illustration: {primer}')
logging.debug(f'Result: {result}')
logging.info('End work')
# logging.error('Error')
# logging.warning('And this, too')
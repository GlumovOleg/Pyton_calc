import logging
from main import *


def logirovanie():
    global a, b, start, primer, result
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename='Python_calc\calc.log')
    logging.info(f'Run : {start}')
    logging.debug(f'First number: {a}')
    logging.debug(f'Two number: {b}')
    logging.info(f'illustration: {primer}')
    logging.debug(f'Result: {result}')
    logging.info('End work\n\n')

logirovanie()
exit()
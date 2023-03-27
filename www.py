import logging
import requests

logging.basicConfig(level=10)
logger = logging.getLogger('logGG')

def log_decorator(original_function):
    """Logging actions using doc stings"""

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper

@log_decorator
def main(name):
    '''Check logger for fun'''
    logger.warning('LOGGER_warning - {}'.format(name))
    r = requests.get('https://www.google.com')


if __name__ == '__main__':
    main('wer')

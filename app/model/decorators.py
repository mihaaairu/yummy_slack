from threading import Thread, active_count
import time
from slack_sdk.errors import SlackApiError
from typing import Callable

from app.model.static_globals import FAILED
from app.service.logger import logger


def run_in_new_thread(func: Callable):

    def run_in_new_thread_wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        logger.debug(f'Started thread with [{func.__name__}] function. Active threads: {active_count()}')
    return run_in_new_thread_wrapper


def handle_exception(func: Callable):
    def handle_exception_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.error(f'[{func.__name__}] crashed. Traceback: {error}')
            return FAILED

    return handle_exception_wrapper


def handle_thread_errors(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.error(f'[{func.__name__}] crashed. Traceback: {error}')
            return False

    def start_thread(*args, **kwargs):
        thread = Thread(target=wrapper, args=args, kwargs=kwargs)
        thread.start()
        logger.info(f'Started thread with [{func.__name__}] function. Active threads: {active_count()}')

    return start_thread


def restart_threaded_func_on_fail(func: Callable):
    retries = 20

    def wrapper(*args, **kwargs):
        attempt = 1
        while attempt <= retries:
            try:
                logger.info(f'Function [{func.__name__}] - attempt {attempt}')
                func(*args, **kwargs)
                return True
            except SlackApiError as error:
                logger.error(f'Function [{func.__name__}] - SlackApiError: {error}')
                time.sleep(1)
            except Exception as error:
                logger.error(f'Function [{func.__name__}] - {error}')
                break
            attempt += 1

        return False

    def start_thread(*args, **kwargs):
        thread = Thread(target=wrapper, args=args, kwargs=kwargs)
        thread.start()
        logger.info(f'Started thread with [{func.__name__}] function. Active threads: {active_count()}')

    return start_thread


def restart_functon_on_fail(func: Callable):
    retries = 20

    def restart_functon_on_fail_wrapper(*args, **kwargs):
        attempt = 1
        time_to_wait = 1
        while attempt <= retries:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                logger.error(f'Function [{func.__name__}] FAILED attempt {attempt}/{retries}. '
                             f'Next attempt in {time_to_wait} seconds. Traceback: {error}')
                time.sleep(time_to_wait)
            attempt += 1
        return FAILED
    return restart_functon_on_fail_wrapper


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        else:
            pass
        return instances[cls]

    return get_instance


# def restart_functon_on_fail(retries, exception):
#     def decorator(func):
#         def wrapper(*args):
#             attempt = 0
#             while attempt < retries:
#                 try:
#                     logging.info(f'Function [{func.__name__}] - attempt {attempt}')
#                     return func(args)
#                 except exception as error:
#                     logging.error(f'Function [{func.__name__}] - {error}')
#                     time.sleep(2)
#                 attempt += 1
#         return wrapper
#     return decorator

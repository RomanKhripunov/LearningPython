import logging
print(__name__)
log = logging.getLogger(__name__)


def do_something():
    log.debug("Doing something!")


do_something()
print(log)
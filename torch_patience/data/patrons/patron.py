import random

from typing import *
from logzero import logger


DEFAULT_MIN_PATIENCE = 1  # Min. customer patience
DEFAULT_MAX_PATIENCE = 3  # Max. customer patience


def customer(env, name, counter, time_in_bank):
    """Customer arrives, is served and leaves."""
    arrive = env.now
    logger.info('%7.4f %s: Here I am' % (arrive, name))

    with counter.request() as req:
        patience = random.uniform(DEFAULT_MIN_PATIENCE, DEFAULT_MAX_PATIENCE)
        # Wait for the counter or abort at the end of our tether
        results = yield req | env.timeout(patience)

        wait = env.now - arrive

        if req in results:
            # We got to the counter
            logger.info('%7.4f %s: Waited, %6.3f' % (env.now, name, wait))

            tib = random.expovariate(1.0 / time_in_bank)
            yield env.timeout(tib)
            logger.info('%7.4f %s: Finished, %6.3f' % (env.now, name, tib))

        else:
            # We reneged
            logger.info('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait))


class Patron:
    def __init__(self, config):
        self.config = config

    def write(self):
        pass


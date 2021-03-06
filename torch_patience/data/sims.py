import random
import simpy

from typing import *
from logzero import logger

from torch_patience.data.servers.server import source


RANDOM_SEED = 42
NEW_CUSTOMERS = 25  # Total number of customers
INTERVAL_CUSTOMERS = 5.0  # Generate new customers roughly every x seconds


# Setup and start the simulation
print('Bank renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Start processes and run
counter = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
env.run()








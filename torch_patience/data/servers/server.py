import ecimpy
import random

from typing import *
from logzero import logger

from torch_patience.data.patrons.patron import customer


def source(env, number, interval, counter):
    """Source generates customers randomly"""
    for i in range(number):
        c = customer(env, 'Customer%02d' % i, counter, time_in_bank=12.0)
        env.process(c)
        t = random.expovariate(1.0 / interval)  # Exponential distribution
        yield env.timeout(t)


class Queue:
    """A eimpy simulation with a class structure to mimic OpenAI's gym"""
    def __init__(self, config):
        self.config = config
        self.state = {
            "prospects": 0
        }
        self.env = simpy.Environment()
        self.counter = simpy.Resource(self.env, capacity=config["capacity"])
        self.curr_time_step = 0
        self.next_time_step = 0

    def _action_check(self, action):
        assert isinstance(action, None)

    def render(self):
        pass

    def step(self, action):
        # Check action is legal (raise exception if not):
        self._action_check(action)

        # Make a step in the simulation
        self.next_time_step += self.curr_time_step
        self.env.run(until=self.next_time_step)

    def close(self):
        pass

    def handle_prospect(self) -> Generator[int]:
        return prospect.handle(self.env, self.counter)

    def reset(self):
        # Set up starting processes
        self.env.process(self.handle_prospect())

        # Set starting state values
        self.state['queue_len'] = 0

        # Inital load of patients (to average occupancy)
        self._load_patients()

        # Return starting state observations
        observations = self._get_observations()
        return observations

    def __repr__(self):
        pass

    def __str__(self):
        self.render()



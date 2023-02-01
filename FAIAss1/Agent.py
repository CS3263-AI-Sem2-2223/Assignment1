"""
The script to define agents.
"""

from typing import Callable


class Agent:
    def __init__(self, problem):
        self.problem = problem

    def __call__(self, s, h):
        actions_available = self.problem.actions(s)
        a = self.searching(s, actions_available, self.problem.result, self.problem.value)
        return a

    def searching(self, s, actions_available, result: Callable, v: Callable):
        raise NotImplementedError


class OnlineAgent(Agent):
    """
    The online-search algorithm agent.
    """

    def __init__(self, problem):
        super(OnlineAgent, self).__init__(problem)
        self.s = None
        self.a = None

    def __call__(self, s1, h):
        action = self.search(self.s, self.a, s1, self.problem.goal_test, h, self.problem.actions, self.problem.c)
        self.s = s1
        self.a = action
        return action

    def search(self, s_previous, a_previous, s1, goal_test: Callable, h: Callable, actions: Callable, cost: Callable):
        raise NotImplementedError

    def cost(self, s, a, s1, h: Callable, c: Callable):
        '''
        used for the online searching algorithm
        '''
        raise NotImplementedError

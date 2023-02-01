"""
Assignment 1 programming script.

* Group Member 1:
    - Name:
    - Student ID:

* Group Member 2:
    - Name:
    - Student ID:
"""

from typing import Callable
from FAIAss1.Agent import Agent, OnlineAgent


class hillclimbingAgent(Agent):
    def __init__(self, problem):
        super().__init__(problem)

    def searching(self, s, actions_available, result: Callable, v: Callable):
        '''The hill climbing algorithm
        args:
            ::s:: current state
            ::actions_available:: the action you can take at current state
            ::result:: Callable, predict the next state given the current state and action
            ::v:: Callable, value of the states.
        returns:
            ::a:: actions to take next, if stop, return None
        '''

        a = None

        '''---your codes start here---'''

        '''----your codes end here----'''

        return a


class LRTAstarAgent(OnlineAgent):
    def __init__(self, problem):
        super().__init__(problem)
        self.H = None
        self.result = None

    def search(self, s_previous, a_previous, s1, goal_test: Callable, h: Callable, actions: Callable, cost: Callable):
        '''The searching algorithm of Learning Real-time A*
        args:
            :s_previous: previous state
            :a_previous: previous action
            :s1: current state
            :goal_test: Callable, test whether a state is a goal
            :h: Callable, heuristic function
            :actions: Callable, return the available actions given the state
        returns:
            :a: next action to take
        '''

        a = None

        '''---your codes start here---'''

        '''----your codes end here----'''

        return a

    def cost(self, s, a, h: Callable, c: Callable):
        '''Returns cost to move from state 's' given the action 'a'.
        args:
            :s: current state (list)
            :a: current action (int)
            :h: heuristic function (callable)
            :c: cost function(callable)
        returns:
            :cost_value: the cost value to the next state (float)
        '''
        cost_value = None

        '''---your codes start here---'''

        '''----your codes end here----'''

        return cost_value


agent_list = {
    'hill_climbing': hillclimbingAgent,
    'lrtastar': LRTAstarAgent,
}

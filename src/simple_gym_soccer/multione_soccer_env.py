import logging
import math
from gym_soccer.envs.soccer_env import SoccerEnv
from gym_soccer.envs.soccer_empty_goal import SoccerEmptyGoalEnv
from simple_soccer_env import SimpleSoccerEnv
import os, subprocess, time, signal
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

try:
    import hfo_py
except ImportError as e:
    raise error.DependencyNotInstalled("{}. (HINT: you can install HFO dependencies with 'pip install gym[soccer].)'".format(e))


logger = logging.getLogger(__name__)

class MultiOneSoccerEnv(SoccerEmptyGoalEnv):
    """
    MultiSoccerOneEnv tasks the multiple agents with approaching the ball,
    dribbling, and scoring a goal. Rewards are given as the agent nears
    the ball, kicks the ball towards the goal, and scores a goal.
    """

    def __init__(self):
        super(MultiOneSoccerEnv, self).__init__();
        self.action_space = spaces.Discrete(5)

    def _take_action(self, action):
        """ Converts the action space into an HFO action. """
        action_type = ACTION_LOOKUP[action]
        if action_type == hfo_py.MOVE:
            self.env.act(action_type)
        elif action_type == hfo_py.SHOOT:
            self.env.act(action_type)
        elif action_type == hfo_py.DRIBBLE:
            self.env.act(action_type)
        elif action_type == hfo_py.PASS:
            if action == 3:
                self.env.act(action_type, 2)
            elif action == 4:
                self.env.act(action_type, 3)
            elif action == 5:
                self.env.act(action_type, 2)
            else:
                print('Unrecognized action %d' % action_type)
                self.env.act(hfo_py.NOOP)
        else:
            print('Unrecognized action %d' % action_type)
            self.env.act(hfo_py.NOOP)

    def _configure_environment(self):
        """
        Provides a chance for subclasses to override this method and supply
        a different server configuration. By default, we initialize one
        offense agent against no defenders.
        """
        super(MultiOneSoccerEnv, self)._start_hfo_server(offense_npcs=2,
                                                              offense_on_ball=0)

ACTION_LOOKUP = {
    0 : hfo_py.MOVE,
    1 : hfo_py.SHOOT,
    2 : hfo_py.DRIBBLE,
    3 : hfo_py.PASS, # Used on defense to slide tackle the ball
    4 : hfo_py.PASS,
    5 : hfo_py.PASS  # Used only by goalie to catch the ball
}
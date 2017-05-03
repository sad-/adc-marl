import logging
from gym.envs.registration import register
from simple_soccer_env import SimpleSoccerEnv
from multione_soccer_env import MultiOneSoccerEnv

logger = logging.getLogger(__name__)

register(
    id='SimpleSoccer-v0',
    entry_point='simple_gym_soccer:SimpleSoccerEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='MultiOneSoccer-v0',
    entry_point='simple_gym_soccer:MultiOneSoccerEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
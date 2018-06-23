import random
import numpy as np

import utilize

# This Env is only used for code validation.
class Env:
    def __init__(self, dim_state, dim_action, seed, num_paths):
        np.random.seed(seed)
        self.__NUM_PATHS = num_paths
        self.__dim_state = dim_state
        self.__dim_action = dim_action
        self.__init_state = self.reset()
        self.__base_sol = utilize.get_base_solution(dim_action)
        self.__best_sol = utilize.convert_action(utilize.run_action(self.__base_sol,
                                             self.__get_rnd(dim_action)), num_paths)

    @property
    def state_init(self):
        return self.__init_state

    @property
    def best_sol(self):
        return np.array(self.__best_sol)

    def reset(self):
        return self.__get_rnd(self.__dim_state)

    # Generate Random Array
    def __get_rnd(self, dim):
        return np.random.rand(dim)

    def getReward(self, state, action):
        state_next = action
        action = np.array(action)
        act = np.array(utilize.convert_action(action, self.__NUM_PATHS))
        reward = - sum(abs(self.best_sol - act))
        # print('best_sol, ', self.__best_sol)
        # print('state_next, ', state_next)
        # print('reward, ', sum(abs(self.__best_sol - state_next)))
        # print('reward, ', reward)
        # reward = reward / 2. - 1.
        # reward = 0.5
        return state_next, reward
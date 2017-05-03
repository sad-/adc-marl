import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

pixel_training_log = pickle.load(open('training_log_step1200000_data.pkl', 'rb'))
print pixel_training_log.keys()
ts = pixel_training_log['ts']
pixel_mean_rewards = pixel_training_log['mean_rewards']
pixel_best_mean_rewards = pixel_training_log['best_mean_rewards']
pixel_num_passes = pixel_training_log['num_passes']

fig = plt.figure()
plt.plot(ts, pixel_mean_rewards, label="Mean 100-episode reward")
plt.plot(ts, pixel_best_mean_rewards, label="Best mean reward")
plt.xlabel('iteration time step')
plt.ylabel('reward')
plt.legend()
plt.savefig("multi_player_log.png")


fig = plt.figure()
plt.plot(ts, pixel_num_passes, label="Mean 100-episode num of passes")
plt.xlabel('iteration time step')
plt.ylabel('passes')
plt.legend()
plt.savefig("multi_player_passes.png")

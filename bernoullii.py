import random
import numpy as np
import matplotlib.pyplot as plt

no_trials= np.array(range(1,10001))
fav, unfav = 0, 0
ratio= []
for i in range(1, 10001):
    toss = random.choice(['F', 'U'])
    if toss == 'F':
        fav += 3
    else:
        unfav += 2
    if unfav==0:
        ratio.append(10)
    else:
        ratio.append(fav/unfav)


plt.plot(no_trials, ratio)
plt.xlabel('No. of Trials')
plt.ylabel('Heads/Tails')
plt.show()

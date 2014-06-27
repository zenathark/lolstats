from __future__ import division

import scipy as np
import formulae as lol
import matplotlib.pyplot as plt
from leona import Leona


health_flat = 8
health_scaling = 1.33
health_percentage = 0.05
champ = Leona()

flat = np.ones(18) * health_flat
scaling = lol.scaling_level(health_scaling)
champ_heal = champ.calc_health()

# plt.plot(flat)
# plt.plot(scaling)
# plt.xlabel("Level")
# plt.ylabel("Health")
# plt.show()

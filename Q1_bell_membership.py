# Question 1: Given following membership functions for fuzzy set Old and Young 
# Where, x is the age of the Person. Calculate the value of the following:
# μ_young(x) = bell(x, 20, 2, 40)
# μ_old(x) = bell(x, 30, 3, 100)
# - More or less young
# - Not young and not old
# - Young but not too young
# - Extremely old

import numpy as np
import matplotlib.pyplot as plt

def bell(x, a, b, c):
    return 1/(1+np.abs((x-c) / a)**(2*b))

x = np.linspace(0, 100, 300)
mu_young = bell(x, 20, 2, 0)
mu_old = bell(x, 30, 3, 100)

more_or_less_young = np.sqrt(mu_young)
not_young_and_not_old = (1 - mu_young)*(1 - mu_old)
young_but_not_too_young = mu_young * (1-np.power(mu_young, 2))
extremely_old = np.power(mu_old, 2)

plt.plot(x, mu_young, label="Young")
plt.plot(x, mu_old, label="Old")
plt.plot(x, more_or_less_young, label="More or Less Young")
plt.plot(x, not_young_and_not_old, label="Not Young and not Old")
plt.plot(x, young_but_not_too_young, label="Young but not too Young")
plt.plot(x, extremely_old, label="Extremely Old")
plt.legend()
plt.show()

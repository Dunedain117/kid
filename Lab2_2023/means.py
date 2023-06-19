import numpy as np
import matplotlib.pyplot as plt

cic = [5,10,20,50,100]
means = [840,1068,1175,1500,1712]
std_dev = [245,245,227,238,239]
plt.ylabel("Means (mrad)")
plt.xlabel("# of cycles")
plt.errorbar(cic,means,yerr = std_dev,fmt = ".")
plt.savefig("means.png")
plt.show()

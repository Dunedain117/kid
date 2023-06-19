import matplotlib.pyplot as plt
import scipy
import numpy as np

std_dev = [200,210,227,238,239]
means = [840,1068,1175,1500,1712]
def f(x,a,b):
    return b + a*x
std_dev = np.array(std_dev)**2
popt, pcov = scipy.optimize.curve_fit(f,means,std_dev)
print(popt)
plt.plot(means,std_dev,".")
fit_values = []
for element in means:
    fit_values.append(f(element,popt[0],popt[1]))
plt.xlabel("means (mrad)")
plt.ylabel("Variance (mrad^2)")
plt.plot(means,fit_values)
plt.savefig("var.png")
plt.show()
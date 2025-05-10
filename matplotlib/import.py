import matplotlib
#most matplotlib utilities lies under pyplot submodule, and usually imported under plt alias
import matplotlib.pyplot as plt
import numpy as np

#checking matplotlib version
print(matplotlib.__version__)

#a straight line

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints , ypoints)
plt.show()

#plotting without line

xpoint = np.array([0,3])
ypoint = np.array([0,50])

plt.plot(xpoint , ypoint , 'o')
plt.show()

#multiple points

xpoint = np.array([1,2,7,15])
ypoint = np.array([3,8,1,14])

plt.plot(xpoint , ypoint)
plt.show()

#default x points

ypoints = np.array([3,8,1,10,5,12])

plt.plot(ypoints)
plt.show()


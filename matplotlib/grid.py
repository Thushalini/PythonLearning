import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([80,85,90,95,100,105,110])
y = np.array([150,160,170,180,190,200,210])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.grid()
plt.show()


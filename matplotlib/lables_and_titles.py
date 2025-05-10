import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

x = np.array([80,85,90,95,100,105])
y = np.array([110,120,130,140,150,160])

#set font properties for title and labels
font1 = {'family':'serif', 'color':'blue' , 'size':'15'}
font2 = {'family':'serif' , 'color':'darkred' , 'size':'21'}

#title for the plot
#loc for position the title
plt.title("Sports Watch data" , fontdict=font1 , loc = 'left')
#name(label) for x , y axis
plt.xlabel("Average pulse" , fontdict = font2)
plt.ylabel("Calorie Burnage" , fontdict = font2)

plt.plot(x,y,color='k')
plt.show()


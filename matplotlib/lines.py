import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#linestyle as ls 

ypoint = np.array([1,9,3,12])

#line styles = 'dotted' = ':' , 'dashed' = '--' , 'solid(default) = '-', 'dashdot' = '-.'
#'None' = ''or''
plt.plot(ypoint , linestyle = 'dotted')
plt.show()

plt.plot(ypoint , ls = '-.')
plt.show()

#color as c for change line color

plt.plot(ypoint , color = 'r')
plt.show()

plt.plot(ypoint , c = '#4CAF50')
plt.show()

#linewidth as lw

plt.plot(ypoint , linewidth = '12.6')
plt.show()

ypoint1 = np.array([4,9,10,6])

plt.plot(ypoint)
plt.plot(ypoint1)
plt.show()

x1 = np.array([1,3,6,9])
y1 = np.array([3,8,10,16])
x2 = np.array([2,6,14,7])
y2 = np.array([2,9,10,15])

plt.plot(x1,y1,x2,y2)
plt.show()

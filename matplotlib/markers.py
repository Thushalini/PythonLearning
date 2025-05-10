import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,12])

plt.plot(ypoints , marker = 'o')     #'o' represents rings or circle
plt.show()

ypoints = np.array([1,9,5,6])

plt.plot(ypoints , marker = '*')
plt.show()

# markers : '.' = point , ',' = pixel , 'x' = X , 'X' = X(filled)
#'+' = plus , 'P' = plus(filled) , 's' = square , 'D' = diamond , 'd' = diamond(thin) 
# 'p' = pentagon , 'h' = hexagon , 
#'v' , '^' , '<' , '>' = triangle down , up , left , right ,
# '1' = tri down , '2' = tri up , '3' = tri left , '4' = tri right , '|' = vline , '_ ' = hline

#format strings 

ypoint = np.array([3,1,8,1,12])

#marker|line|color
plt.plot(ypoint , '*-.g')
#line types => '-' = solid line , ':' = dotted line , '--' = dashed line , '-.' = dashed/dotted line
plt.show()

#color reference => 'r'=Red	,'g'=Green , 'b'=Blue , 'c'=Cyan , 'm'=Magenta , 'y'=Yellow , 'k'=Black , 'w'=White

#marker size
#ms shorter version of markersize

plt.plot(ypoints , marker = '*' , ms = 20)
#if mention marker without marker keyword their appears without line points graph
plt.show()

#marker color
#markeredgecolor as mec

plt.plot(ypoints , ms = 12 , mec = 'r' , marker = 'o')
plt.show()

#markerfacecolor as mfc

plt.plot(ypoints , marker = 'o' , ms = 12 , mfc = 'r')
plt.show()

#can use both mfc and mec to color entire marker

plt.plot(ypoints , marker = 'o' , ms = 12 , mfc = '#4CAF50' , mec = 'r')
plt.show()


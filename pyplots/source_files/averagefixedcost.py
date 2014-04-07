from pylab import *

x = np.linspace(0,10,100)
y = x**(-1) 
plot(x, y, color='crimson', linewidth=2.0)
ylim(0,10)

show()

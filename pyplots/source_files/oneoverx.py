from pylab import *

xneg = np.arange(-10,-0.1,0.01)
xpos = np.arange(0.1,10,0.01)

plot(xneg, xneg**(-1), color='crimson', linewidth=2.0)
plot(xpos, xpos**(-1), color='crimson', linewidth=2.0)
grid(True)

title('Illustration:- The function $1/x$ has different one-sided limits at zero')
show()

from pylab import *

x = np.linspace(0,10,30)
y = (x-4)**2 
plot(x, y, color='crimson', linewidth=2.0)

x = np.arange(7,9,0.01)
plot(x, 16+8*(x-8), '--', color='black')

plot([2,8],[4,16], 'o--', color='black')
plot([2,2],[0,4], '--', color='black')
plot([8,8],[0,16], '--', color='black')

gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 

text(1.9,5,'A')
text(7.9,17,'B')
text(1.9,-1.4,'$x$')
text(7.9,-1.4,'$x_0$')
xlim(0,11)
ylim(0,40)
grid(True)
show()

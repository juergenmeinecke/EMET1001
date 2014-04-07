from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
S = np.sin(X)

plot(X,S, color='crimson', linewidth=2.0)
plot([-4,4],[0,0], color='black')
plot([np.pi/2,np.pi/2],[0,1], '--', color='black')
plot([np.pi/2-.5,np.pi/2+.5],[1,1], '--', color='black')

ylim(-1.5,1.5)
text(-np.pi-.1,0.05,'$a$')
text(np.pi,-0.1,'$b$')
text(np.pi/2-.1,-0.1,'$c$')
text(np.pi/2+0.6,1, '$f\'(c)=0$')

gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 
show()

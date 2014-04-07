from pylab import *

def f(x):
    y = np.cos(x)+x/3
    return y

xmin = -np.pi/2 
xmax = 2.5*np.pi
fmax = f(xmax) 
fmin = f(xmin) 

x0 = np.linspace(xmin, xmax, 256,endpoint=True)
plot(x0,f(x0), color='crimson', linewidth=2.0)

plot([xmin,xmax],[fmin,fmax],'--', color='black')
plot([xmin,xmin],[-1,fmin],'--',color='black')
plot([xmax,xmax],[-1,fmax],'--',color='black')
plot([np.pi,np.pi],[-1,f(np.pi)],'--',color='black')

slope = (fmax-fmin)/(xmax-xmin)
x1 = np.linspace(2,4.5,30)
plot(x1, -1.0+slope*x1, '--', color='black')

text(-np.pi/2,-1.2,'$a$')
text(2.5*np.pi,-1.2,'$b$')
text(np.pi,-1.2,'$c$')

gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 
xlim(xmin-.5,xmax+.5)
show()

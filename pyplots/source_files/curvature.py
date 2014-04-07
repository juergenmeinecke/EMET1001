from pylab import *

figure(figsize=(8,8), dpi=80)
plt.subplots_adjust(hspace=0.4)

x = np.linspace(0,1,100)
y = -sqrt(1-x**2) 
subplot(2,2,1)
plot(x, y, color='crimson', linewidth=2.0)
text(0.2,-0.2,'convex, sloping up')
ylim(-1,0)
gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 
title('Illustration:- Curvature of functions')

x = np.linspace(-1,0,100)
y = -sqrt(1-x**2) 
subplot(2,2,2)
plot(x, y, color='crimson', linewidth=2.0)
text(-0.8,-0.2,'convex, sloping down')
ylim(-1,0)
gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 


x = np.linspace(-1,0,100)
y = sqrt(1-x**2) 
subplot(2,2,3)
plot(x, y, color='crimson', linewidth=2.0)
text(-0.8,0.15,'concave, sloping up')
ylim(0,1)
gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 

x = np.linspace(0,1,100)
y = sqrt(1-x**2) 
subplot(2,2,4)
plot(x, y, color='crimson', linewidth=2.0)
text(0.2,0.15,'concave, sloping down')
ylim(0,1)
gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 


show()

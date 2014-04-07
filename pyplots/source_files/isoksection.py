from pylab import *

x = np.linspace(0,10,100)
y1 = sqrt(x)
y2 = sqrt(x)/1.4
plot(x, y1, color='crimson', linewidth=2.0, label='$f(K_1,L)$')
plot(x, y2, '--', color='crimson', linewidth=2.0,label='$f(K_0,L)$ with $K_0<K_1$')

#plotting MPL
plot([1,4],[sqrt(2)-0.5*(2**(-0.5)), sqrt(2)+2*0.5*(2**(-0.5))], '--', color='black', linewidth=2.0, label='$MPL$')
plot([2,2],[0,sqrt(2)], '--', color='black')

#plotting APL
plot([0,4],[0,4*0.5*sqrt(2)], '-.', color='black', linewidth=2.0, label='$APL=Q/L$')


ylim(0,3.5)
legend(loc='lower right')
gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 
text(9.8,-0.2,'$L$')
text(1.75,sqrt(2),'$P$')
text(0.5,3.25,'at point $P$ the following relationship holds: $APL>MPL$')
title('Illustration:- Iso-$K$-section of the production function')

show()

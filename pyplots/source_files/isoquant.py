from pylab import *

x = np.linspace(0.04,1,100)

# first isoquant
q1 = 10;
a = 0.5
b = 0.5
y1 = (1.5*q1*x**(-a))**(1/b)
plot(x, y1, color='crimson', linewidth=2.0, label='$10= 2/3 \cdot K^{1/2} L^{1/2}$')

# second isoquant
q2 = 15
y2 = (1.5*q2*x**(-a))**(1/b)
plot(x, y2, '--', color='crimson', linewidth=2.0, label='$15= 2/3 \cdot K^{1/2} L^{1/2}$')

# third isoquant
q3 = 20
y3 = (1.5*q3*x**(-a))**(1/b)
plot(x, y3, '-.', color='crimson', linewidth=2.0, label='$20= 2/3 \cdot K^{1/2} L^{1/2}$')

plot([0.2,0.2], [0,5000], '--', color='black')
plot([0.3,0.3], [0,5000], '--', color='black')
plot([0.6,0.6], [0,5000], '--', color='black')
plot([0.7,0.7], [0,5000], '--', color='black')

gca().xaxis.set_major_locator(NullLocator()) 
gca().yaxis.set_major_locator(NullLocator()) 
text(0.21,4500,'$P_0$')
text(0.31,3000,'$P_1$')
text(0.61,1500,'$P_2$')
text(0.71,1300,'$P_3$')
title('Illustration:- Isoquant and decreasing marginal rate of substitution')

text(-0.05,4800,'$K$')
text(0.975,-150,'$L$')

legend(loc='upper right')
ylim(0,5000)
xlim(0,1)
show()

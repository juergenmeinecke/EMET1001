from pylab import *

x = np.linspace(-2,2,30)
y1 = x**3 
y2 = 3*x**2 
y3 = 6*x 
figure(figsize=(9,6), dpi=80)

plt.subplots_adjust(hspace=0.4)
subplot(1,2,1)
plot(x, y1, color='crimson', linewidth=2.0, label='$f(x)=x^3$')
plot(x, y2, '--', color='crimson', linewidth=2.0, label='$f\'(x)=3x^2$')
plot(x, y3, '-.', color='crimson', linewidth=2.0, label='$f\'\'(x)=6x$')
legend(loc='lower right')
xlim(-2.5,2.5)
ylim(-8,8)
xticks([-2,0,2])
grid(True)

y1 = -x**3 
y2 = -3*x**2 
y3 = -6*x 
subplot(1,2,2)
plot(x, y1, color='crimson', linewidth=2.0, label='$f(x)=-x^3$')
plot(x, y2, '--', color='crimson', linewidth=2.0, label='$f\'(x)=-3x^2$')
plot(x, y3, '-.', color='crimson', linewidth=2.0, label='$f\'\'(x)=-6x$')
legend(loc='upper right')
xlim(-2.5,2.5)
ylim(-8,8)
xticks([-2,0,2])
grid(True)

show()

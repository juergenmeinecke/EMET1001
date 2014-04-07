from pylab import *

x = np.linspace(-2,2,30)
y1 = x**4 
y2 = -x**4 
y3 = x**3

plt.subplots_adjust(hspace=0.4)
subplot(1,3,1)
plot(x, y1, color='crimson', linewidth=2.0)
ylim(-8,8)
xticks([-2,0,2])
grid(True)

subplot(1,3,2)
plot(x, y2, color='crimson', linewidth=2.0)
ylim(-8,8)
xticks([-2,0,2])
grid(True)

subplot(1,3,3)
plot(x, y3, color='crimson', linewidth=2.0)
ylim(-8,8)
xticks([-2,0,2])
grid(True)
show()

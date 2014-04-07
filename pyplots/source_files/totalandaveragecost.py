from pylab import *

figure(figsize=(5,10), dpi=80)
subplots_adjust(hspace=0.001)

subplot(2,1,1)
def TC(x):
    f = 0.3*x**3 - 5*x**2 + 45*x + 100 
    return f

q = np.linspace(0,20,100)
plot(q, TC(q), color='crimson', linewidth=2.0, label='TC')
plot([10,10],[0,1600],'--',color='black')

plot([0,2],[0,TC(2)],'--',color='black')
plot([0,5],[0,TC(5)],'--',color='black')
plot([0,15],[0,TC(10)/10*15],'--',color='black')
legend(loc='upper left')
ylim(0,1600)
gca().xaxis.set_major_locator(NullLocator()) 

subplot(2,1,2)
ATC = 0.3*q**2 - 5*q**1 + 45 + 100/q 
plot(q, ATC, color='crimson', linewidth=2.0, label='ATC')
plot([10,10],[0,150],'--',color='black')
legend(loc='upper left')
ylim(0,150)


show()

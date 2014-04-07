from pylab import *

figure(figsize=(4,10), dpi=80)
subplots_adjust(hspace=0.001)

subplot(3,1,1)
def TC(x):
    f = 2*x**2 + 4*q + 600 
    return f

q = np.linspace(0,60,100)
plot(q, TC(q), color='crimson', linewidth=2.0,label='$TC(q)$')
plot(q, 124*q, '--', color='crimson', linewidth=2.0, label='$TR(q)$')
plot([30,30],[0,124*30],'--',color='black')
plot([5,5],[0,800],'--',color='black')
plot([54.5,54.5],[0,6900],'--',color='black')
qsub = np.linspace(20,40,100)
plot(qsub,124*qsub-1300,'--',color='black')
legend(loc='upper left')
ylim(0,8000)
gca().xaxis.set_major_locator(NullLocator()) 

subplot(3,1,2)
plot(q, -TC(q) + 124*q, color='crimson', linewidth=2.0, label='$\Pi(q)$')
plot([30,30],[0,1500],'--',color='black')
plot([5,5],[0,1500],'--',color='black')
plot([54.5,54.5],[0,1500],'--',color='black')
legend(loc='upper left')
ylim(0,1500)
yticks([0,500,1000])
gca().xaxis.set_major_locator(NullLocator()) 

subplot(3,1,3)
plot([0,60], [124,124], '--', color='crimson', linewidth=2.0, label='MR')
plot(q, 4*q + 4, color='crimson', linewidth=2.0, label='MC')
plot([30,30],[0,250],'--',color='black')
legend(loc='upper left')
ylim(0,250)
yticks([0,50,100,150,200])

show()

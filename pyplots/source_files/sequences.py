#!/usr/bin/env python
from pylab import *

n = np.linspace(1,15,15)
plt.subplots_adjust(hspace=0.4)

subplot(311)
l = plot(n, sqrt(n), 'bo', markerfacecolor='crimson')
grid(True)
xlim(0.0,15.0)
ylim(0.0,4.0)
title('Illustration:- The sequence $\sqrt{n}$')
xticks(np.linspace(0,15,16,endpoint=True))

subplot(312)
plot(n, (-1)**n, 'bo', markerfacecolor='crimson')
grid(True)
xlim(0.0,15.0)
ylim(-1.2,1.2)
title('Illustration:- The sequence $(-1)^n$')
xticks(np.linspace(0,15,16,endpoint=True))


subplot(313)
plot(n, 1/(n**2+1), 'bo', markerfacecolor='crimson')
grid(True)
xlim(0.0,15.0)
ylim(-0.2,1.0)
title('Illustration:- The sequence $1/(n^2+1)$')
xticks(np.linspace(0,15,16,endpoint=True))
xlabel('n')
show()

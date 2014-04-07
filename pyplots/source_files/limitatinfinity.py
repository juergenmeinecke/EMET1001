#!/usr/bin/env python
from pylab import *

def f(t):
    s1 = cos(2*pi*t)
    e1 = exp(-t)
    return multiply(s1,e1)

x = arange(0.0, 10.0, 0.02)
p = plot(x, f(x), color='crimson', linewidth=2.0)
xticks([0,10])

plot([0,10], [0.1,0.1], '--', color='black')
plot([0,10], [-0.1,-0.1], '--', color='black')
plot([2.1,2.1], [-0.8,0.1], '--', color='black')

grid(True)

ann0 = annotate('$L+\epsilon$',
         xy=(10.2,0.1), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann0.set_annotation_clip(False)

ann1 = annotate('$L$',
         xy=(10.2,-0.02), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann1.set_annotation_clip(False)

ann2 = annotate('$L-\epsilon$',
         xy=(10.2,-0.12), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann2.set_annotation_clip(False)

ann3 = annotate('$\delta$',
         xy=(2.0,-0.88), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann3.set_annotation_clip(False)

title('Illustration:- Limit at infinity')

show()


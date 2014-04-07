import pylab

pylab.plot([-2,0],[-4,-1], color='crimson', linewidth=2.0)
pylab.plot([0,2],[1,4], color='crimson',linewidth=2.0)
pylab.plot([0,0],[-4,4], '--', color='black')
pylab.plot([-2,0],[-1,-1], '--', color='black')
pylab.plot([-2,0],[1,1], '--', color='black')

pylab.xticks([0])
#pylab.gca().xaxis.set_major_locator(pylab.NullLocator()) # turn off x-axis ticks
pylab.gca().yaxis.set_major_locator(pylab.NullLocator()) # turn off y-axis ticks

ann0 = pylab.annotate('$L_+=1$',
         xy=(-2.45,0.9), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann0.set_annotation_clip(False)
ann1 = pylab.annotate('$L_-=-1$',
         xy=(-2.6,-1.1), xycoords='data',
         xytext=None, textcoords=None, fontsize=16)
ann1.set_annotation_clip(False)

pylab.title('Illustration:- Different LHS and RHS limits')
pylab.show()

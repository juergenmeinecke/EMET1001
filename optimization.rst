**************************
Multivariate Optimization
**************************

========================
Isolating Dimensions
========================

In the last few weeks, we have worked with functions a lot. We have defined them properly, starting out with the basics of set theory, distinguishing functions from relations, discussing important concepts such as surjectivity, injectivity and invertibility. After a brief detour in which we learned about sequences and series (all of which a special cases of functions!) we studied slopes of functions between two points as well as at a particular point, discussed extrema, curvature and inflection points.

All of these things we did using *univariate* functions. That is, the function had one argument (typically called :math:`x`) and one image dimension (typically called :math:`y`). We now generalize the concept of functions and permit the argument-dimension to be greater than one. Mathematically, we move from the univariate case

.. math::

        y = f(x)

to the multivariate case

.. math:: 
        
        y = f(x_1, x_2, \ldots, x_n)

The function's arguments are now called :math:`x_1,x_2` up to :math:`x_n` instead of just :math:`x`. In general, the function's arguments are thus :math:`n`-dimensional. Together with the image :math:`y` itself, we thus have to consider altogether :math:`n+1` dimensions. For example, the function :math:`y=f(x_1,x_2)` has a two-dimensional argument that is mapped into a third image-dimension. Therefore, we would graph this function in a three-dimensional coordinate system.

Let's consider the general equation for a two-dimensional plane that cuts through a three-dimensional space:

.. math::

        y = f(x_1,x_2) = a_0 - a_1 x_1 - a_2 x_2 \qquad \qquad a_0, a_1, a_2 \in \mathbb{R},

where :math:`a_0, a_1, a_2` are place holders for real numbers. How does the above function look like in three dimensions? Here's a picture of it:

.. admonition:: Figure: Two-dimensional plane through three-dimensional space

        .. raw:: html
        
                <embed src="./_static/3dplane.mov" width="640" height="500" CONTROLLER="false" LOOP="false" AUTOPLAY="true"></embed>

If you had not seen this picture, you may have found it difficult to imagine the graph of the function :math:`f(x_1,x_2)` in three dimensions. It is already difficult to think of graphs in two dimensions, never mind three, four, five, six, ..., :math:`n` dimensions! 
        
Having said that, we are used to picturing graphs in two dimensions. More generally, we would like a way to deal with multivariate functions (as an extension to univariate functions). Even if we were able to imagine the shape of a function in three dimensions, once we move to four dimensions we reach the limits of our imagination. 

The trick to deal with multivariate functions is to *artificially* reduce their dimensionality by forcing some variables to take on fixed values. These variables then become *parameters* of the function. That is what the following three iso-sections accomplish for the above example:

.. admonition:: Iso-:math:`x_2`-section

        :math:`y = f(x_1,\bar{x}_2) = c_0 + c_1 x_1 + c_2 \bar{x}_2`

        Here, we force the variable :math:`x_2` to take on the fixed value :math:`\bar{x}_2 \in \mathbb{R}`. In doing so, we effectively change its role from that of a *variable* to that of a *parameter*. A parameter is just a number and can simply be treated as such. As a consequence, the expression :math:`y = f(x_1,\bar{x}_2)` is regarded as a *univariate* function in :math:`x_1` only. 


.. admonition:: Iso-:math:`x_1`-section

        :math:`y = f(\bar{x}_1,x_2) = c_0 + c_1 \bar{x}_1 + c_2 x_2`

        Here, we force the variable :math:`x_1` to take on the fixed value :math:`\bar{x}_1 \in \mathbb{R}`. In doing so, we effectively change its role from that of a *variable* to that of a *parameter*. A parameter is just a number and can simply be treated as such. As a consequence, the expression :math:`y = f(\bar{x}_1,x_2)` is regarded as a *univariate* function in :math:`x_2` only. 


.. admonition:: Iso-:math:`y`-section

        :math:`\bar{y} = f(x_1, x_2) = c_0 + c_1 x_1 + c_2 x_2` resulting in

        :math:`x_1 = \frac{\bar{y} - c_0 - c_2 x_2}{c_1}` or equivalently
  
        :math:`x_2 = \frac{\bar{y} - c_0 - c_1 x_1}{c_2}`. 

        Here, we force the variable :math:`y` to take on the fixed value :math:`\bar{y} \in \mathbb{R}`. In doing so, we effectively change its role from that of a *variable* to that of a *parameter*. A parameter is just a number and can simply be treated as such. As a consequence, the expression :math:`\bar{y} = f(x_1,x_2)` can be regarded either as a *univariate* function in :math:`x_1` (with :math:`x_2 = f(x_1`)) or as a *univariate* function in :math:`x_2` (with :math:`x_1 = f(x_2`)).



.. admonition:: Example (Two-dimensional plane cutting through three-dimensional space)

        Let's specify the parameters :math:`c_0, c_1, c_2` and work out the iso-sections. Setting

        .. math:: c_0=200, \quad c_1=-3, \quad c_2=-4

        we obtain 
        
        .. math:: y=200-3x_1-4x_2. 

        The three-dimensional graph above is based on that specification. Now, letting
       
        .. math:: \bar{x}_1=20, \quad \bar{x}_2=5 \quad \bar{y}=80, 

        we get the following iso-sections: 

        * Iso-:math:`x_1`-section: :math:`y = f(20,x_2) = 140 - 4 x_2`
        
        * Iso-:math:`x_2`-section: :math:`y = f(x_1,5) = 180 - 3 x_1`
        
        * Iso-:math:`y`-section: :math:`80 = f(x_1,x_2) = 200 - 3 x_1 - 4 x_2` resulting in either :math:`x_1=40+\tfrac{4}{3} x_2` or :math:`x_2=30+\tfrac{3}{4} x_1`.


.. admonition:: Figure: Iso-section

        .. raw:: html
        
                <embed src="./_static/isosection.mov" width="640" height="500" CONTROLLER="false" LOOP="false" AUTOPLAY="true"></embed>



========================
Partial Derivatives
========================

For multivariate functions, we need to think about how to define derivatives properly. The general idea of a derivative is to measure the change in the function value as we change the :math:`x`-value infinitesimally. In the case of a function with two-dimensional domain, for example, we can change the :math:`x`-value in two different directions. Separating these properly is an important part of the following definition:

.. admonition:: Definition (First Order Partial Derivative)

        Let :math:`f:X_1 \times X_2 \to Y` be a function. There are two first order parital derivatives:

        * :math:`\frac{\partial f(x_1,x_2)}{\partial x_1} = \lim_{x_1 \to x_{10}} \frac{f(x_1,x_2)-f(x_{10},x_2)}{x_1-x_{10}}`
        
        * :math:`\frac{\partial f(x_1,x_2)}{\partial x_2} = \lim_{x_2 \to x_{20}} \frac{f(x_1,x_2)-f(x_1,x_{20})}{x_2-x_{20}}`


Intuitively, the partial derivative :math:`\partial f(x_1,x_2) / \partial x_1` measures the slope of the function in the direction of :math:`x_1`, keeping :math:`x_2` constant. Likewise, the partial derivative :math:`\partial f(x_1,x_2) / \partial x_2` measures the slope of the function in the direction of :math:`x_2`, keeping :math:`x_1` constant.         

.. admonition:: Example

        :math:`f(x_1,x_2) = x_1^3 + 3 x_1^2 x_2^2 + x_2^3`

        The partial derivatives are

        .. math::

                \begin{align*}
                        \frac{\partial f(x_1,x_2)}{\partial x_1} 
                                &= 3x_1^2 + 6x_1x_2^2 + 0 \\
                        \frac{\partial f(x_1,x_2)}{\partial x_2} 
                                &= 0 + 6 x_1^2 x_2 + 3x_2^2
                \end{align*}



Multivariate functions also have second derivatives.                

.. admonition:: Definition (Second Order Direct Partial Derivative)

        Let :math:`f:X_1 \times X_2 \to Y` be a function. There are two *direct* second order parital derivatives:

        * :math:`\frac{\partial}{\partial x_1} \Big(\frac{\partial f(x_1,x_2)}{\partial x_1} \Big)` denoted by :math:`\frac{\partial^2 f(x_1,x_2)}{\partial x_1 \partial x_1}` or :math:`f_{x_1 x_1}` 
        
        * :math:`\frac{\partial}{\partial x_2} \Big( \frac{\partial f(x_1,x_2)}{\partial x_2} \Big)` denoted by :math:`\frac{\partial^2 f(x_1,x_2)}{\partial x_2 \partial x_2}` or :math:`f_{x_2 x_2}`

Similarly to the univariate case, the second derivative is defined here as the first derivative of the first derivative. Because the first derivative is properly defined above, the definition of the direct second order partial derivative is closed and complete.        
       
.. admonition:: Example

        :math:`f(x_1, x_2) = x_1^{1/2} \cdot x_2^{1/2} - 10`

        The first order partial derivative and the direct second order partial derivatives are

        .. math::

                \begin{align*}
                        \frac{\partial f(x_1, x_2)}{\partial x_1} 
                                &= 1/2 \cdot x_1^{-1/2} \cdot x_2^{1/2} \\
                        \frac{\partial^2 f(x_1,x_2)}{\partial x_1 \partial x_1} & = -1/4 \cdot x_1^{-3/2} \cdot x_2^{1/2}
                \end{align*}


There are two additional second order partial derivatives.               

.. admonition:: Definition (Second Order Cross Partial Derivative)

        Let :math:`f:X_1 \times X_2 \to Y` be a function. There are two second order *cross* parital derivatives:

        * :math:`\frac{\partial}{\partial x_2} \Big(\frac{\partial f(x_1,x_2)}{\partial x_1} \Big)` denoted by :math:`\frac{\partial^2 f(x_1,x_2)}{\partial x_2 \partial x_1}` or :math:`f_{x_1 x_2}` 
        
        * :math:`\frac{\partial}{\partial x_1} \Big( \frac{\partial f(x_1,x_2)}{\partial x_2} \Big)` denoted by :math:`\frac{\partial^2 f(x_1,x_2)}{\partial x_1 \partial x_2}` or :math:`f_{x_2 x_1}`


.. admonition:: Example

        :math:`f(x_1,x_2) = x_1^3 \cdot x_2^4`

        The first order partial derivative and the second order cross partial derivatives are

        .. math::

                \begin{align*}
                        \frac{\partial f(x_1, x_2)}{\partial x_1} 
                                &= x_2^4 \cdot 3x_1^2 \\
                        \frac{\partial^2 f(x_1,x_2)}{\partial x_2 \partial x_1} & = 3x_1^2 \cdot 4 x_2^3
                \end{align*}

Again, similarly to the univariate case, the second derivative is defined here as the first derivative of the first derivative. 




========================
Economic Applications
========================

.. admonition:: Definition (Production Function)

        A production function gives the relationship between inputs of capital :math:`K` and labor :math:`L` and resulting output :math:`Q` of some product:

        .. math::
                
                Q = f(K,L)

.. admonition:: Definition (Neoclassical Assumptions)

        * :math:`Q,K,L` are infinitely divisible and :math:`f(K,L)` is a smooth and continuous function

        * :math:`f(0,L) = f(K,0) = 0` (implying :math:`f(0,0)=0`)

        * For :math:`L>0` and :math:`K>0` increasing either :math:`L` or :math:`K` will increase :math:`Q`

        * Law of diminishing marginal product applies (see below)

.. admonition:: Figure: Cobb-Douglas production function :math:`Q=f(K,L)`

                .. raw:: html
        
                        <embed src="./_static/productionfunction.mov" width="640" height="500" CONTROLLER="false" LOOP="false" AUTOPLAY="true"></embed>

                
Technically, we can now distinguish between the iso-K-section and the iso-L-section. Economists, somewhat arbitrarily, view the iso-K-section as the so-called *short-run production function*. The iso-K-section results from fixing the capital input to some predetermined level :math:`\bar{K}`, thus reducing the problem to a univariate production function

        :math:`Q = f(\bar{K},L)`

Why should this be the short-run production function? It may be reasonable to regard the input factor capital as immobile in the short-run (at least relative to labor). 

Digression: It may actually be confusing (or not helpful) to think of :math:`K` and :math:`L` as capital and labor. I find it more useful to think of them more abstractly as placeholders for any input factors in a production process. Capital and labor are somewhat outdated terms stemming from the early days of economic theory that do not relate very well to modern applications of economic theory. In that case, it does not actually matter what the input factor :math:`K` represents, but we distinguish it from the other input factor :math:`L` in that it is assumed to be fixed in the short-term.

.. admonition:: Figure: Iso-:math:`K`-section

        .. raw:: html
        
                <embed src="./_static/isoksection.mov" width="640" height="500" CONTROLLER="false" LOOP="false" AUTOPLAY="true"></embed>

bla

.. admonition:: Figure                

        .. image:: ./pyplots/isoksection.png


We can now define the so-called marginal product of labor as the slope of the iso-K-section:

.. admonition:: Definition (Marginal Product of Labor)

        :math:`\text{MPL} = \frac{\partial f(K,L)}{\partial L}`


Now, the third neoclassical assumption says that :math:`\text{MPL} \geq 0`, or in words, if the labor input increases then a firm cannot produce less output.

At the same time, the fourth neoclassical assumption says that successive increases of the labor input lead to smaller and smaller increases in output. This is the so-called diminishing marginal product of labor. Technically, it means that the iso-K-section is concave, reflected in the following result for the second order direct partial derivative:

        :math:`\frac{\partial^2 f(K,L)}{\partial L^2} = \frac{\partial \text{MPL}}{\partial L} \leq 0`

Furthermore, we define the so-called average product of labor:

.. admonition:: Definition (Average Product of Labor)
        
        :math:`\text{APL} = \frac{Q}{L}`

Likewise, we can define the marginal product of capital as the slope of the iso-L-section:

.. admonition:: Definition (Marginal Product of Capital)

        :math:`\text{MPK} = \frac{\partial f(K,L)}{\partial K}`
        
Again, the third neoclassical assumption says that :math:`\text{MPK} \geq 0`, or in words, if the capital input increases then a firm cannot produce less output.

At the same time, the fourth neoclassical assumption says that successive increases of the capital input lead to smaller and smaller increases in output. This is the so-called diminishing marginal product of capital. Technically, it means that the iso-L-section is concave, reflected in the following result for the second order direct partial derivative:

        :math:`\frac{\partial^2 f(K,L)}{\partial K^2} = \frac{\partial \text{MPK}}{\partial K} \leq 0`

Furthermore, we define the so-called average product of capital:

.. admonition:: Definition (Average Product of Capital)
        
        :math:`\text{APK} = \frac{Q}{K}`

How does the iso-L-section look like?

Next, we deal with the iso-Q-section, the so-called isoquant (because the quantity is held constant).

.. admonition:: Definition (Isoquant)

        The isoquant is the iso-Q-section of the production function; formally the output amount :math:`Q` is fixed at some level :math:`\bar{Q}` while both the capital and the labor input are allowed to vary: :math:`\bar{Q}=f(K,L)`.

The isoquant therefore results in an implicit function between the two inputs :math:`K` and :math:`L`. Graphically, the isoquant is given in the following picture.

.. admonition:: Figure                

        .. image:: ./pyplots/isoquant.png


On any given isoquant, the production quantity is kept fixed while the amounts of the two input factors vary. There are at least two interesting things to observe about the shape of the isoquants in the above picture: they are sloped negatively and they are convex. The negative slope concerns the first partial derivative while the convexity has to do with the second partial derivative.

Why should the isoquant be sloped negatively? Recall that for all points on the isoquant, the output amount is fixed to some exogenous level. Intuitively, the isoquant collects all combinations of :math:`K` and :math:`L` for which the production output is equal to some level. In the above picture, the top isoquant fixes the production output level at 20. Moving from point :math:`P_0` to :math:`P_1`, you increase the amount of the labor input by a certain amount. To keep producing that same production output amount, you have to decrease the amount of the capital input. If you did not decrease the amount of the capital input while at the same time increasing the amount of the labor input then you would end up producing a larger production output amount. But then you would not stay on that isoquant any longer, you would jump up further onto another isoquant on which the production output exceeds 20.

Simply put, the negative slope of the isoquant results from the neoclassical assumption that both input factors are *substitutes* in production. But what about the convexity of the production function? What is the source of this convexity? Technically, the source of the convexity of the isoquant is the assumption of a decreasing marginal rate of substitution between :math:`K` and :math:`L`. The marginal rate of substitution is defined now.

.. admonition:: Definition (Marginal Rate of Substitution)

        :math:`\text{MRS} = \big| \frac{\partial K}{\partial L} \big|`


How can we see the marginal rate of substitution in the above picture? Well, it is simply the absolute value of the slope of each isoquant. As you start in point :math:`P_0` and 'walk' along the top isoquant towards point :math:`P_1` the slope decreases (in absolute value), it becomes flatter. The change in the input factor :math:`K` is relatively large compared to when you walk from point :math:`P_2` to point :math:`P_3`. In both cases, you increase the amount of the input factor :math:`L` by the same value, yet in between points :math:`P_2` and :math:`P_3` you give up less of the input factor :math:`K` in order to stay on that same production level.

But what exactly do we mean when we say that the marginal rate of substitution is decreasing? Well, the higher your amount of the input factor :math:`L`, the less you can afford to give up in terms of the other input factor :math:`K`. Compare points :math:`P_0` and :math:`P_2`: at point :math:`P_2` you use more labor. Now, at both points, increase the amount of labor by the same amount. Doing so, you move from point :math:`P_0` to :math:`P_1` (decreasing capital by a lot) and from point :math:`P_2` to point :math:`P_3` (decreasing capital by a little). Although you increased the amount of labor by the same amounts, you had to decrease capital by different amounts. When you started out from a relatively low level of labor (point :math:`P_0`) you were able to reduce the amount of the capital input by a large value (low initial level of labor, large decrease in capital). When you started out from a relatively high level of labor (point :math:`P_2`) you were able to reduce the amount of the capital input only by a small value (large initial level of labor, small decrease in capital). This is what we mean by the decreasing marginal rate of substitution. 

In the whole discussion on isoquants above, we have put :math:`K` on the vertical axis and :math:`L` on the horizontal axis, which seems to suggest that capital is viewed as a function of labor. We could have, of course, done this whole discussion the other way around without effect. Putting capital on the vertical axis was just an arbitrary choice that does not affect any of the results presented here.



======================================
Extrema of Multivariate Functions
======================================


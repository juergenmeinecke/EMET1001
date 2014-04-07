***************************
Differential Calculus
***************************



=====================================
Difference quotient and derivatives
=====================================

.. admonition:: Definition (Difference quotient)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function. For :math:`x, x_0 \in X`, we call

        .. math::

		\frac{f(x) - f(x_0)}{x-x_0}, \qquad\qquad \text{with } x \neq x_0,

        the **difference quotient**. 


.. admonition:: Figure
        
        .. image:: ./pyplots/differencequotient.png

        *Illustration of the difference quotient. The difference quotient is the slope of the line segment AB. Alternatively, it is the average slope on the curve as one walks from A to B. If instead we are interested in the slope at a point, we need to study the difference quotient as* :math:`x_0` *and* :math:`x` *get closer and closer to each other. For example, the slope of the curve at point B is represented by the limit of the difference quotient as* :math:`x` *approaches* :math:`x_0`.
   

The next definition makes this formal.

.. admonition:: Definition (Differentiability, derivative)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function. For :math:`x_0 \in X`, if the limit

        .. math::

        	\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x-x_0} = L \in \mathbb{R}, \qquad \qquad \text{with } x \neq x_0,
	
	then we say that :math:`f` is **differentiable** at :math:`x_0` with **derivative** :math:`L` and write
	
        .. math::

                f'(x_0) = L.
	
        If the limit does not exist then we say that the function is **not differentiable**.
        
	



.. admonition:: Example 

	Let :math:`f: \mathbb{R} \to \mathbb{R}` with :math:`f(x) = x^2`. Then

        .. math::

        	\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x-x_0} &= \lim_{x \to x_0} \frac{x^2 - x_0^2}{x-x_0} = \lim_{x \to x_0} \frac{(x-x_0)(x+x_0)}{x-x_0} \\
	        &= \lim_{x \to x_0} (x+x_0) = 2 x_0.
        
	Note that cancelling the :math:`(x-x_0)` factors is legitimate because :math:`x \neq x_0` (otherwise the derivative would not be properly defined). 


Some basic derivatives that should be familiar (assumed knowledge) are given by the next two propositions:

.. admonition:: Proposition (Basic derivatives)

        .. math::

		\text{(Constant function)} 	&& f(x) &= c 	& \Rightarrow f'(x) & = 0 \\
		\text{(Power rule)}		&& f(x) &= x^n	& \Rightarrow f'(x) & = n \cdot x^{n-1} 


.. admonition:: Proof 

	Omitted.



.. admonition:: Proposition (Derivatives of exponential and logarithmic functions)

	Let :math:`f: \mathbb{R} \to \mathbb{R}_+` with :math:`f(x) = b^x` for some :math:`b \in \mathbb{R}_+ \setminus \{1\}`. Then :math:`f` is called an exponential function. The derivative is :math:`f'(x) = b^x \ln b`. For the special case :math:`b=e` we get :math:`f'(x) = e^x \ln e = e^x`.

	Let :math:`f: \mathbb{R}_+ \to \mathbb{R}` with :math:`f(x) = \log_b x` for some :math:`b \in \mathbb{R}_+ \setminus \{1\}`. Then :math:`f` is called a logarithmic function. The derivative is :math:`f'(x) = \frac{1}{\ln b} \cdot \frac{1}{x}`. For the special case :math:`b=e` we get :math:`f'(x) = \frac{1}{\ln e} \frac{1}{x} = \frac{1}{x}`.




.. admonition:: Proof 

	Omitted.




The following standard derivative laws can be useful.

.. admonition:: Theorem (Derivative laws)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` and :math:`g: X \to \mathbb{R}` both be functions that are differentiable at :math:`x_0`. Let :math:`c` be some real constant. Then

        (i)     Sum and difference rule
                :math:`(f \pm g)'(x_0) = f'(x_0) \pm g'(x_0)`
		
        (#)     Multiplicative constant rule
		:math:`(c \cdot f)'(x_0) = c \cdot f'(x_0)`

	(#)     Product rule
		:math:`(f \cdot g)'(x_0) = f'(x_0) \cdot g(x_0) + f(x_0) \cdot g'(x_0)`

        (#)     Quotient rule
		:math:`\bigg(\frac{f}{g} \bigg)' (x_0) = \frac{f'(x_0) \cdot g(x_0) - f(x_0) \cdot g'(x_0)}{g(x_0)^2},`
		for :math:`g(x_0) \neq 0`

	(#)     Chain rule
		:math:`g \big( f(x_0) \big)' = g'(y_0) \cdot f'(x_0),`
		where :math:`y_0=f(x_0)`, and :math:`g` is differentiable at :math:`y_0`



.. admonition:: Proof 

	Omitted.








=====================================
Determining local and global extrema
=====================================


Derivatives are often used for curve sketching of functions. Loosely speaking, if the derivatives equals zero then the function attains an extremum point (a maximum or a minimum). But we need to be careful what exactly we mean by that.

.. admonition:: Definition (Global extrema)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function and let :math:`x_0 \in X`. We say that :math:`f` attains a *global maximum* at :math:`x_0` if :math:`f(x_0) \geq f(x)` for all :math:`x \in X`. We say that :math:`f` attains a *global minimum* at :math:`x_0` if :math:`f(x_0) \leq f(x)` for all :math:`x \in X`.


.. admonition:: Example 

	The constant function :math:`f(x)=c` with :math:`c \in \mathbb{R}` has infinitely many global maxima and minima.


.. admonition:: Proposition EP (Extremum principle) 

	Let :math:`a<b` be real numbers and let :math:`f:[a,b] \to \mathbb{R}` be a function continuous on :math:`[a,b]`. Then :math:`f` attains its global maximum at some point :math:`x_{max} \in [a,b]` and it also attains its global minimum at some point :math:`x_{min} \in [a,b]`.
	


.. admonition:: Proof 

	Omitted.



.. admonition:: Example 

	Let :math:`f: [-5,-2] \to \mathbb{R}` be the function :math:`f(x)=|x|`. We have learnt previously that this function is continuous on :math:`\mathbb{R}`. Thus, Proposition EP tells us that the function must attain its maximum and minimum on the closed interval :math:`[-5,-2]`. The corresponding :math:`x`-values are, of course, :math:`x_{max}=-5` and :math:`x_{min}=-2`.



.. admonition:: Definition (Local extrema)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function and let :math:`x_0 \in X`. Then :math:`f(x_0)` is a *local maximum* of :math:`f` at :math:`x_0` if there exists :math:`\delta>0` such that :math:`f(x) \leq f(x_0)` for all :math:`x \in X \cap (x_0-\delta,x_0+\delta)`. Analogously, :math:`f(x_0)` is a *local minimum* of :math:`f` at :math:`x_0` if there exists :math:`\delta>0` such that :math:`f(x) \geq f(x_0)` for all :math:`x \in X \cap (x_0-\delta, x_0+\delta)`.




.. admonition:: Example 

	Let :math:`f: \mathbb{R} \to \mathbb{R}` be the function :math:`f(x) = x^2 - x^4`. What kind of extrema does this function have at zero? It cannot be a global minimum because :math:`f(2) = -12 < 0 = f(0)`. But it is local, because if we choose, for example, :math:`\delta=1` and study :math:`f` on the open interval :math:`(-1,1)` then we get :math:`x^4 \leq x^2` and therefore :math:`f(x) = x^2 - x^4 \geq 0 = f(0)`.



.. admonition:: Proposition NC (Necessary condition for local extrema)  

	Let :math:`a<b` be real numbers and let :math:`f:(a,b) \to \mathbb{R}` be a function. If :math:`x_0 \in (a,b)`, :math:`f` is differentiable at :math:`x_0`, and :math:`f` attains either a local maximum or a local minimum at :math:`x_0` then :math:`f'(x_0)=0`.


.. admonition:: Proof 

	Omitted.




.. admonition:: Example 

	Take :math:`f(x)=x^2-x^4` from the previous example. We learnt that this function has a local minimum at :math:`x=0`. Proposition NC requires that the derivative :math:`f'(0)` must be zero. This indeed is true, as we can readily see.


.. admonition:: Example 

	Let :math:`f: (-1,1) \to \mathbb{R}` be the function :math:`f(x) = x^2`. Then :math:`f` attains a local minimum at :math:`x_0=0` for which indeed we have :math:`f'(0)=0`.



.. admonition:: Example 

	It is crucial that the domain inside Proposition NC be an open set. If the function from the previous example instead had been defined as :math:`(-1,1] \to \mathbb{R}` with :math:`f(x) = x^2` then, by construction, it would have attained another local extremum, namely a local maximum  at :math:`x_0=1` for which the first derivative is not equal to zero, i.e. :math:`f'(1) \neq 0`.


:math:`\diamondsuit`

Combining Proposition EP with Proposition NC results in 

.. admonition:: Proposition (Rolle's theorem)

	Let :math:`a<b` be real numbers and let :math:`f: [a,b] \to \mathbb{R}` be a continuous function which is differentiable on :math:`(a,b)`. Suppose also that :math:`f(a) = f(b)`. Then there exists an :math:`x \in (a,b)` such that :math:`f'(x)=0`.


.. admonition:: Proof 

	Omitted.

       
.. admonition:: Figure
        
        .. image:: ./pyplots/rollestheorem.png

        *Illustration of Rolle`s Theorem.* 


Rolle's Theorem has an important corollary.

.. admonition:: Corollary (Mean Value Theorem)

	Let :math:`a<b` be real numbers, and let :math:`f: [a,b] \to \mathbb{R}` be a function which is continuous on :math:`[a,b]` and differentiable on :math:`(a,b)`. Then there exists a :math:`c \in (a,b)` such that
	
        .. math::

        	f'(c) = \frac{f(b) - f(a)}{b-a}.
	

.. admonition:: Figure
        
        .. image:: ./pyplots/meanvaluetheorem.png

        *Illustration of the Mean Value Theorem. Intuitively, the mean value theorem states that there exists some point* :math:`(c,f(c))` *on the graph of* :math:`f` *at which a tangent line is parallel to the line segment connecting the points* :math:`(a,f(a))` *and* :math:`(b,f(b))`. 



The main use of the mean value theorem, however, is to prove the following results.

.. admonition:: Proposition FDT (First derivative test for local extrema) 

	Let :math:`f: [a,b] \to \mathbb{R}` be a continuous and differentiable function. Let :math:`x_0 \in (a,b)`. Then

                (i)     If there is a neighborhood :math:`(x_0-\delta,x_0+\delta)` such that :math:`f'(x) \geq 0` for :math:`x \in (x_0-\delta, x_0)` and :math:`f'(x) \leq 0` for :math:`x \in (x_0, x_0+\delta)`, then :math:`f` attains a local maximum at :math:`x_0`.
		(#)      If there is a neighborhood :math:`(x_0-\delta,x_0+\delta)` such that :math:`f'(x) \leq 0` for :math:`x \in (x_0-\delta, x_0)` and :math:`f'(x) \geq 0` for :math:`x \in (x_0, x_0+\delta)`, then :math:`f` attains a local minimum at :math:`x_0`.



.. admonition:: Proof 

	We just prove (i) here, the proof for (ii) is similar. For :math:`x \in (x_0-\delta,x_0)` it follows, from the mean value theorem, that there exists a point :math:`c \in (x, x_0)` such that :math:`f(x_0)-f(x) = (x_0-x) \cdot f'(c)`. But :math:`f'(c) \geq 0` and :math:`(x_0-x) >0` so that :math:`f(x_0) \geq f(x)` for :math:`x \in (x_0-\delta, x_0)`. Similarly, for :math:`x \in (x_0,x_0+\delta)` it follows, from the mean value theorem, that there exists a point :math:`c \in (x_0,x)` such that :math:`f(x)-f(x_0) = (x-x_0) \cdot f'(c)`. But :math:`f'(c) \leq 0` and :math:`(x-x_0) >0` so that :math:`f(x_0) \geq f(x)` for :math:`x \in (x_0, x_0+\delta)`. In summary, :math:`f(x_0) \geq f(x)` for all :math:`x \in (x_0-\delta, x_0+\delta)` which is what is required for a local maximum.



The First derivative test for local extrema helps determine whether a point :math:`x_0` with :math:`f'(x_0)=0` is a local minimum or a local maximum. Checking the first derivative to the left and to the right of a :math:`x_0` is not always easy to do. There exists a more practical way, based on the second derivative, of determining the nature of extrema.



.. admonition:: Definition (Second derivative)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function with derivative :math:`f'(x_0)` at :math:`x_0 \in X`. Then we call the derivative of the function :math:`f'(x)` at the point :math:`x_0` the **second derivative of** :math:`f`, denoted by :math:`f''(x_0)`.

	A similar definition holds for higher order derivatives.




We now use the second derivative to provide a more practical sufficient condition for extrema. 

.. admonition:: Proposition SC (Second derivative test for local extrema)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function with second derivative :math:`f''(x_0)` at :math:`x_0 \in X`. Then, if :math:`f'(x_0)=0` and :math:`f''(x_0)<0` the function attains a local maximum. If, instead, :math:`f'(x_0)=0` and :math:`f''(x_0)>0` the function attains a local minimum. Last, if both :math:`f'(x_0) = f''(x_0) = 0` then the function attains either a local maximum, a local minimum, or it has an inflection point at :math:`x_0`.


.. admonition:: Figure
        
        .. image:: ./pyplots/secondderivativetest.png

        *Illustration of the second derivative test. The functions* :math:`f_1(x)=x^4`, :math:`f_2(x)=-x^4`, *and* :math:`f_3(x)=x^3` *are all examples of functions that have a zero first and second derivative*. 



Proposition SC is much easier to use than Proposition FDT. While the latter requires knowledge of the behavior of :math:`f'(x)` at points to the left and right of :math:`x_0`, the former only requires knowing the first two derivatives of the function :math:`f` but only at the point :math:`x_0` itself.



=============================================
Monotonicity, curvature and inflection points
=============================================

We now move on to techniques that can be helpful in determining the shape and look of functions. 

.. admonition:: Definition (Increasing, decreasing, monotone functions)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function. Pick an interval :math:`J \subset X`.

	The function :math:`f` is said to be *increasing* on :math:`J` if for all :math:`x_1,x_2 \in J` such that :math:`x_1 < x_2 \Rightarrow f(x_1) \leq f(x_2)`.

	The function :math:`f` is said to be *strictly increasing* on :math:`J` if for all :math:`x_1,x_2 \in J` such that :math:`x_1 < x_2 \Rightarrow f(x_1) < f(x_2)`.
	
        The function :math:`f` is said to be *decreasing* on :math:`J` if for all :math:`x_1,x_2 \in J` such that :math:`x_1 < x_2 \Rightarrow f(x_1) \geq f(x_2)`.
	
        The function :math:`f` is said to be *strictly decreasing* on :math:`J` if for all :math:`x_1,x_2 \in J` such that :math:`x_1 < x_2 \Rightarrow f(x_1) > f(x_2)`.

	If a function is either increasing or decreasing on :math:`X`, we say that it is *monotone* on :math:`X`. If it is either strictly increasing or either strictly decreasing on :math:`X`, we say that it is *strictly monotone* on :math:`X`.

It can be quite difficult to apply this definition for the purpose of checking whether a particular function is increasing or decreasing on a certain subset of the domain. The following proposition makes that job easier by linking the monotonicity of a function to the first derivative of the function.

.. admonition:: Proposition DM

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function that is differentiable on :math:`X`. Let :math:`J \subset X`. Then

		(i) :math:`f` is increasing on :math:`J` iff :math:`f'(x) \geq 0` for all :math:`x \in J`

		(#) :math:`f` is decreasing on :math:`J` iff :math:`f'(x) \leq 0` for all :math:`x \in J`.

		(#) :math:`f` is strictly increasing on :math:`J` if :math:`f'(x) > 0` for all :math:`x \in J`

		(#) :math:`f` is strictly decreasing on :math:`J` if :math:`f'(x) < 0` for all :math:`x \in J`


.. admonition:: Proof 

	Omitted.

This proposition is helpful because it allows you to use the derivative in order to learn about the monotonicity of a function. 

It is therefore safe to use the weak monotonicity property (increasing/decreasing) interchangeably with the property of weakly positive/negative derivatives. You need to be careful though when dealing with strictly increasing/decreasing functions, note that the *if and only if* statement holds only for cases (i) and (ii) but not for cases (iii) and (iv). The following example illustrates.


.. admonition:: Example 

	Let :math:`f(x) = x^3` (the previous figure shows the graph of this function). Then, clearly, :math:`f'(x)=3x^2`. Now, let :math:`J` from the proposition be the real line, i.e. :math:`J=\mathbb{R}`. It should be obvious that :math:`f'(x) \not> 0` on :math:`x \in J` (why?) but the function is in fact *strictly* increasing (you will prove this in next week's tute). 
	On the other hand, for weakly increasing functions Proposition DM works in both directions. Note that :math:`f` is also weakly increasing (strict increasing implies weak increasing). The proposition therefore states that its derivative must be weakly positive on :math:`\mathbb{R}`. This indeed holds, because :math:`f'(x) \geq 0` for :math:`x \in J`.



.. admonition:: Definition (Curvature of functions)

	Let :math:`a<b` be real numbers and let :math:`f:(a,b) \to \mathbb{R}` be a continuous and twice differentiable function. Then :math:`f` is said to be (weakly) convex (textbook: `concave up`) on :math:`(a,b)` if :math:`f''(x) \geq 0`. The function is said to be (weakly) concave (textbook: `concave down`) on :math:`(a,b)` if :math:`f''(x) \leq 0`. 


Note: this definition of curvature is a little non-standard. There exists a more general definition of convexity that does not invoke the second derivative and therefore is valid even for functions that are not differentiable. 

.. admonition:: Figure
        
        .. image:: ./pyplots/curvature.png



Combining this definition with Proposition DM results in the following Corollary.

.. admonition:: Corollary

        Let :math:`a<b` be real numbers and let :math:`f:(a,b) \to \mathbb{R}` be a continuous and twice differentiable function. Then :math:`f` is said to be (weakly) convex on :math:`(a,b)` iff :math:`f'(x)` is increasing on :math:`(a,b)`. The function is said to be (weakly) concave on :math:`(a,b)` iff :math:`f'(x)` is decreasing on :math:`(a,b)`. 





Now we are ready to define inflection points. Loosely speaking, an inflection point is a point where the curvature of a function changes from convex to concave or from concave to convex. A non-conventional way to define inflection point is via local extrema of first derivatives. The following two graphs illustrate that inflection points are points where the first derivative attains a local extremum. Depending on whether the extremum is a minimum or a maximum, the curvature changes from concave to convex (left figure) or the curvature changes from convex to concave (right figure). (Note that it does not matter whether the graph changes from concave to convex sloping upwards (as shown in the figure) or sloping downwards (not shown). Likewise for when the graph changes from convex to concave sloping downwards (shown) or sloping upwards (not shown).)

In the following definition of an inflection point, however, we do not distinguish what direction the curvature changes to.


.. admonition:: Figure
        
        .. image:: ./pyplots/inflectionpoints.png

        *Inflection points can be interpreted as local extrema of first derivatives. Here, for example, the function* :math:`f(x)=x^3` *has a first derivative that attains a local minimum at zero. The original function* :math:`f(x)` *has an inflection point there.*  



.. admonition:: Definition IP (Inflection point)

	Let :math:`a<b` be real numbers and let :math:`f:[a,b] \to \mathbb{R}` be a continuous and twice differentiable function. Then the point :math:`x_0 \in (a,b)` is an inflection point of :math:`f(x)` if :math:`f'(x)` attains a local extremum at :math:`x_0`.

**Note: END OF EXAMINABLE MATERIAL (only material up to this point is relevant for the mid-semester exam)**

:math:`\diamondsuit`

Now we can apply the same machinery from before to figure out whether a point :math:`x_0` is an inflection point. The only difference here is that we are looking for an extremum of :math:`f'` and not :math:`f`. The necessary condition follows straightforwardly.

.. admonition:: Proposition (Necessary condition for inflection point) 

	Let :math:`a<b` be real numbers and let :math:`f:(a,b) \to \mathbb{R}` be a function. If :math:`f` has an inflection point at :math:`x_0 \in (a,b)` and is twice differentiable at :math:`x_0` then :math:`f''(x_0)=0`. 



.. admonition:: Proof 

	This is the same necessary condition as before, just that now :math:`f'` (instead of :math:`f`) attains a local extremum at :math:`x_0` (which is equivalent to having an inflection point there).


Thus, determining the roots of :math:`f''(x)` gives us a list of candidates for inflection points. Not all of these roots will be inflection points. We need to study sufficient conditions. 

.. admonition:: Corollary IP (Second derivative test for inflection points)
	
	Let :math:`f: [a,b] \to \mathbb{R}` be a continuous and twice differentiable function. Let :math:`x_0 \in (a,b)`. Then
		
                (i) If there is a neighborhood :math:`(x_0-\delta,x_0+\delta)` such that :math:`f''(x) \geq 0` for :math:`x \in (x_0-\delta, x_0)` and :math:`f''(x) \leq 0` for :math:`x \in (x_0, x_0+\delta)`, then :math:`f'` attains a local maximum at :math:`x_0` and therefore :math:`f` has an inflection point (convex to concave) at :math:`x_0`.

		(#) If there is a neighborhood :math:`(x_0-\delta,x_0+\delta)` such that :math:`f''(x) \leq 0` for :math:`x \in (x_0-\delta, x_0)` and :math:`f''(x) \geq 0` for :math:`x \in (x_0, x_0+\delta)`, then :math:`f'` attains a local minimum at :math:`x_0` and therefore :math:`f` has an inflection point (concave to convex) at :math:`x_0`.


.. admonition:: Proof 

	Follows again by the mean value theorem.



Under the conditions given (twice differentiable and :math:`x_0` an interior point), both Definition IP and Corollary IP can be treated as being synonymous. Some textbooks reinterpret Corollary IP as the actual *definition* of an inflection point. 

Parallel to before, Corollary IP may not be practical because it could be difficult to check the derivative in a neighborhood around :math:`x_0`. Instead we propose the sufficient condition based on the higher-order derivative---here the third derivative.

.. admonition:: Proposition (Third derivative test for inflection point)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function with third derivative :math:`f'''(x_0)` at :math:`x_0 \in X`. Then, if :math:`f''(x_0)=0` and :math:`f'''(x_0) \neq 0` the function attains an inflection point. 
	
	Last, if both :math:`f''(x_0) = f'''(x_0) = 0` then the function may or may not have an inflection point at :math:`x_0`.




        
        
        
===========
Exercises
===========

*Note: Solutions for exercises will only be given during the tutorials. They will not be posted here.*

(1)     Let :math:`f: \mathbb{R} \to \mathbb{R}` with :math:`f(x) = |x|`. Is this function differentiable? Show your work!


(#)	True or False? Argue.
       
        Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function.

		(i) If :math:`f` is continuous at a point then it is also differentiable there.
		(ii) If :math:`f` is differentiable at a point then it is also continuous there.


(#)	In the lecture you learnt about a necessary condition for local extrema. Loosely speaking, if a function attains a local extremum, then its derivative there is equal to zero. How does this argument work (or not!) for the function :math:`f(x)=|x|` at :math:`x=0`?


(#)	Proof the power rule (i.e, if :math:`f(x) = x^n` then :math:`f'(x) = n \cdot x^{n-1}`).


(#)	Let :math:`f: \mathbb{Z} \to \mathbb{R}` be the function :math:`f(x)=x`. Determine all local and global extrema.




*Related exercises in the textbook you should study, include (but are not limited to):*

* Exercises 10-4 --- Problems 1-26, 45-60
* Exercises 10-5 --- Problems 1-18, 25-52, 69-80
* Exercises 11-2 --- Problems 1-22, 27-42
* Exercises 11-3 --- Problems 1-82
* Exercises 11-4 --- Problems 1-76, 79-90

*The tutors at the EMET1001 help desk are happy to help, if you have any questions.*











(6)     Consider the function :math:`f: \mathbb{R} \to \mathbb{R}` with :math:`f(x)=x^3`. 

                (i) Prove that :math:`f` is strictly increasing on :math:`\mathbb{R}`.

		(#) Prove that :math:`f` is weakly increasing on :math:`\mathbb{R}`.



(#)	The total cost of producing :math:`q` units of a good is
	
        .. math::
        	TC(q) = aq^2 + bq + c, \qquad q>0,
	
        where :math:`a`, :math:`b`, and :math:`c` are positive constants.

        (i) Find the local extrema of the average total cost function

            .. math::
	       ATC(q) = TC(q)/q.
	 
            Determine the nature of the local extrema (minimum/maximum) and also discuss curvature of the ATC curve.

	(#) Sketch the graph of :math:`ATC(q)` together with the graphs of the functions 

            .. math::
	       f(q) &= aq+b	\\
	       g(q) &= 2aq+b.	
	
            What is the interpretation of the function :math:`f`? The function :math:`g`?


(#)	A function :math:`f` is given by :math:`f(x) = (1+2/x) \cdot \sqrt{x+6}`.
		
                (i)     What is the domain of :math:`f`? 
		(#)     On which intervals is :math:`f(x)` positive?
		(#)     Find the local extrema of :math:`f`. Are they minima or maxima?




*Related exercises in the textbook you should study, include (but are not limited to):*

* Exercises 12-1 --- Problems 19-40, 47-54, 79-88
* Exercises 12-2 --- Problems 7-34 

*The tutors at the EMET1001 help desk are happy to help, if you have any questions.*





(9)	Evaluate the first three derivatives of the functions
	
                .. math::

                        f(x)=x^4, \qquad\qquad g(x)=-x^4, \qquad \qquad h(x)=x^5
	
        at zero. What do you conclude about possible inflection points there? Draw the function :math:`h` and its first three derivatives in one graph.	







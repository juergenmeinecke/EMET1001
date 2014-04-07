***************************
Limits of Functions
***************************


============================
Two-sided limits
============================

.. admonition:: Definition

        Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function. We say that :math:`f(x)` approaches the limit :math:`L` as :math:`x` approaches :math:`x_0` and write

        .. math::

        	\lim_{x \to x_0} f(x) = L
	
	if :math:`f` is defined on some neighborhood of :math:`x_0` and, for every :math:`\epsilon > 0`, there is a :math:`\delta > 0` such that :math:`|f(x)-L| < \epsilon` for all :math:`x` with :math:`0 < |x-x_0| < \delta`.
	
        We say that :math:`L` is the **limit of the function at** :math:`x_0`.




.. admonition:: Example

	Let :math:`f(x) = c` for some :math:`c \in \mathbb{R}` and for all :math:`x \in \mathbb{R}`. We want to show that :math:`\lim_{x \to x_0} f(x) = c`. For all :math:`\epsilon > 0` just let :math:`\delta = 1` (in fact any positive :math:`\delta` will do). Then whenever :math:`x` is such that :math:`0 < |x-x_0| < 1` we get that :math:`|f(x) - c | =  | c - c | = 0 < \epsilon`. This holds for arbitrary :math:`\epsilon` and thus it shows that the limit is indeed equal to :math:`c`.



.. admonition:: Example

	Let :math:`f(x) = x+1`. Then :math:`\lim_{x \to 1} f(x) = 2`. While it seems obvious, how do you prove this? We need :math:`|f(x) - 2| = |x-1| < \epsilon` in a neighborhood :math:`0 < |x-1| < \delta` for some :math:`\delta>0` of our choice. Well, just set :math:`\delta=\epsilon` and the result follows.


This example shows that sometimes, in order to find the limit of a function :math:`f(x)` at :math:`x_0` you can simply just evaluate the function at the limit, i.e. :math:`f(x_0)`. 

.. admonition:: Question
        
        Let :math:`f(x) = c \cdot x` which is just a linear function through the origin (for some real number :math:`c`). Then :math:`\lim_{x \to x_0} f(x) = c \cdot x_0`. How do you prove that?


        
The function does not need to be defined at :math:`x_0`. The limit looks at the function value in a neighborhood of :math:`x_0`, what happens at :math:`x_0` is irrelevant. Often times determining the limit of a function at :math:`x_0` is akin to just plugging in :math:`x_0` and getting the function value :math:`f(x_0)`. But this appraoch may not always work. The next example illustrates this.

.. admonition:: Example

	Let :math:`g: \mathbb{R}\setminus\{1\} \to \mathbb{R}` be defined as :math:`g(x)=\frac{x^2-1}{x-1}`. Then :math:`\lim_{x \to 1} g(x) = 2`. To see this note first that we cannot simply guess that :math:`g(1)` is the correct limit. The function is not defined at :math:`1`. Instead we have to make sure that :math:`|g(x) - 2| < \epsilon` for some :math:`x` in the neighborhood of :math:`x_0=1`. Writing out gives
	
        .. math::

                |g(x)-2| = \bigg|\frac{x^2-1}{x-1} - 2 \bigg| = \bigg| \frac{(x+1)(x-1)}{(x-1)} -2 \bigg| = | (x+1) - 2 | = |f(x) - 2|,
	
	where :math:`f(x) = x+1`. What this shows is that the functions :math:`g(x)=\tfrac{x^2-1}{x-1}` and :math:`f(x) = x+1` are identical for the purpose of determining the limit at :math:`x_0=1`. While this is not trivial for :math:`g(x)`, we have already shown in one of the previous examples that the limit of :math:`f(x)` is 2 at :math:`x_0=1`.

	It is important to understand that the functions :math:`f(x)` and :math:`g(x)` are not the same. The domain of :math:`f` is :math:`\mathbb{R}` while the domain of :math:`g` is :math:`\mathbb{R} \setminus \{1\}`. However, what this last example shows is that when we restrict the function :math:`f` to the set :math:`\mathbb{R} \setminus \{1\}` then we can treat :math:`f` as being identical to the function :math:`g` and exploit this to find the limit for :math:`g` at :math:`x_0`.


.. admonition:: Theorem (Limit laws for functions)

        If :math:`\lim_{x \to x_0} f(x) = L_1` and :math:`\lim_{x \to x_0} g(x) = L_2` for :math:`L_1, L_2 \in \mathbb{R}` then
		
        (i)     Sum and difference rule

         	:math:`\lim_{x \to x_0} \big( f(x) \pm g(x) \big) = L_1 \pm L_2`

	(#)     Multiplicative constant rule 

		:math:`\lim_{x \to x_0} \big( c \cdot f(x) \big) = c \cdot L_1` for some :math:`c \in \mathbb{R}`

	(#)     Product rule

		:math:`\lim_{x \to x_0} \big( f(x) \cdot g(x) \big) = L_1 \cdot L_2` 

        (#)     Quotient rule
                
		:math:`\lim_{x \to x_0} \bigg( \frac{f(x)}{g(x)} \bigg) = \frac{L_1}{L_2}`, if :math:`g(x)\neq0` and :math:`L_2 \neq 0`  

        (#)     Rule for polynomial functions
                
         	If :math:`f(x)` is a polynomial function, i.e. :math:`f(x) = c_n x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0` for some :math:`c_0,\ldots,c_n \in \mathbb{R}`, then :math:`\lim_{x \to x_0} f(x) = f(x_0)`

        (#)     Rule for rational functions 

                If :math:`f(x)` and :math:`g(x)` are both polynomial functions then the rational function constructed as :math:`r(x) = f(x)/g(x)` has the limit :math:`\lim_{x \to x_0} r(x) = r(x_0)`, provided that :math:`g(x_0) \neq 0` 


.. admonition:: Proof

	Omitted.


.. admonition:: Example

	Let :math:`f(x) = 2x^2 + x -3` and :math:`g(x) = x^3+4` and :math:`r(x) = f(x)/g(x)`. Then
	
        .. math::

	        \lim_{x \to 1} r(x) = \lim_{x \to 1} \frac{2x^2 + x -3}{x^3+4} = \frac{\lim_{x \to 1} (2x^2 + x - 3)}{\lim_{x \to 1} (x^3+4)} = \frac{2 \cdot 1^2 + 1 -3}{1^3 + 4} = 0
	
	But since :math:`r(x)` is a rational function we could have know from the beginning that the limit coincides with the function value :math:`r(1)=0`.



============================
One-sided limits
============================


For some functions, the above definition of a limit does not seem to apply. Consider the function

.. math::

        f(x) = 
        \begin{cases}
	        x+1 & \text{if } x>0 \\
	        x-1 & \text{if } x<0.
        \end{cases}


What is the limit of this function at zero? First, the function is not defined at zero. This need not be a problem as we discussed earlier. The problem here is that the function behaves in \`different ways\' to the left and to the right of zero. (Can you sketch this function?)

The following versions of limit may be more applicable in such cases.

.. admonition:: Definition (One-sided limit)

	We say that :math:`f(x)` approaches the left-hand limit :math:`L_-` as :math:`x` approaches :math:`x_0` from the left and write :math:`\lim_{x \to x_0-} f(x) = L_-` if :math:`f` is defined on some open interval :math:`(a,x_0)` and, for each :math:`\epsilon>0`, there is a :math:`\delta>0` such that :math:`|f(x)-L_-| < \epsilon` if :math:`x_0-\delta < x < x_0`.

	We say that :math:`f(x)` approaches the right-hand limit :math:`L_+` as :math:`x` approaches :math:`x_0` from the right and write :math:`\lim_{x \to x_0+} f(x) = L_+` if :math:`f` is defined on some open interval :math:`(x_0,b)` and, for each :math:`\epsilon>0`, there is a :math:`\delta>0` such that :math:`|f(x)-L_+| < \epsilon` if :math:`x_0 < x < x_0+\delta`.


.. admonition:: Figure

        .. image:: ./pyplots/onesidedlimits.png


.. admonition:: Proposition

	The limit laws for functions also apply to one-sided limits.


.. admonition:: Proof

	Omitted.




.. admonition:: Example

	Let :math:`f(x) = \frac{x}{|x|}` for :math:`x \in \mathbb{R} \setminus \{0\}`. Then :math:`\lim_{x \to 0+} f(x) = 1` and :math:`\lim_{x \to 0-} f(x) = -1`. 



But does this function have a limit at zero? The next theorem clarifies.

.. admonition:: Theorem

	A function :math:`f` has a limit at :math:`x_0` iff it has a left- and a right-hand limit at :math:`x_0` and they are equal. Thus
	
	.. math::

                \lim_{x \to x_0} f(x) = L \qquad \qquad \text{iff } \lim_{x \to x_0-} f(x) = \lim_{x \to x_0+} f(x) = L.
	


It follows that the function from the previous example does not have a limit at zero because their one-sided limits do not coincide (although they both exist).



============================
Limits at infinity
============================


How do functions behave when :math:`x` approaches a very, very large (small) number?

.. admonition:: Definition (Limits at infinity)

	We say that :math:`f(x)` approaches the limit :math:`L` as :math:`x` approaches :math:`\infty` and write :math:`\lim_{x \to \infty} f(x) = L` if :math:`f` is defined on an interval :math:`(a,\infty)` and, for each :math:`\epsilon>0`, there is a number :math:`\delta` such that :math:`|f(x) - L| < \epsilon` if :math:`x>\delta`.
	
	We say that :math:`f(x)` approaches the limit :math:`L` as :math:`x` approaches :math:`-\infty` and write :math:`\lim_{x \to -\infty} f(x) = L` if :math:`f` is defined on an interval :math:`(-\infty,b)` and, for each :math:`\epsilon>0`, there is a number :math:`\delta` such that :math:`|f(x) - L| < \epsilon` if :math:`x<\delta`.


.. admonition:: Figure

        .. image:: ./pyplots/limitatinfinity.png


.. admonition:: Example

	Let :math:`f(x) = 1-1/x^2`. Then :math:`\lim_{x \to \infty} f(x) = 1` because :math:`|f(x)-1| = 1/x^2 < \epsilon` if :math:`x > 1/\sqrt{\epsilon}=\delta`.




.. admonition:: Example

	Let :math:`f(x) = \frac{2 \cdot |x|}{1+x}`. Then :math:`\lim_{x \to \infty} f(x) =2` because :math:`|f(x)-2| = \big| \frac{2x}{1+x}-2 \big| = \frac{2}{1+x} < \frac{2}{x} < \epsilon` if :math:`x > 2/\epsilon = \delta`.


============================
Infinite limits
============================


When do limits not exist?


.. admonition:: Definition (Infinite limits)

	We say that :math:`f(x)` approaches :math:`\infty` as :math:`x` approaches :math:`x_0` from the left and write
	
        .. math::

        	\lim_{x \to x_0-} f(x) = \infty,
	
	if :math:`f` is defined on some open interval :math:`(a,x_0)` and, for each real number :math:`M \in \mathbb{R}_+`, there is a :math:`\delta>0` such that
	
        .. math::

	        f(x) > M \qquad\qquad \text{if } x_0-\delta<x<x_0.
	
        
	We say that :math:`f(x)` approaches :math:`-\infty` as :math:`x` approaches :math:`x_0` from the left and write

        .. math::

        	\lim_{x \to x_0-} f(x) = -\infty,
	
	if :math:`f` is defined on some open interval :math:`(a,x_0)` and, for each real number :math:`M \in \mathbb{R}_-`, there is a :math:`\delta>0` such that
	
        .. math::

	        f(x) < M \qquad\qquad \text{if } x_0-\delta<x<x_0.
	
	
        Likewise for right-sided limits:

	We say that :math:`f(x)` approaches :math:`\infty` as :math:`x` approaches :math:`x_0` from the right and write
	
        .. math::

        	\lim_{x \to x_0+} f(x) = \infty,
	
	if :math:`f` is defined on some open interval :math:`(x_0,b)` and, for each real number :math:`M \in \mathbb{R}_+`, there is a :math:`\delta>0` such that
	
        .. math::
         
	        f(x) > M \qquad\qquad \text{if } x_0<x<x_0+\delta.
	
	We say that :math:`f(x)` approaches :math:`-\infty` as :math:`x` approaches :math:`x_0` from the right and write
	
        .. math::

        	\lim_{x \to x_0+} f(x) = -\infty,
	
	if :math:`f` is defined on some open interval :math:`(x_0,b)` and, for each real number :math:`M \in \mathbb{R}_-`, there is a :math:`\delta>0` such that
	
        .. math::

        	f(x) < M \qquad\qquad \text{if } x_0<x<x_0+\delta.
	


.. admonition:: Example

	Let :math:`f(x)=1/x`. Then :math:`\lim_{x \to 0+} f(x) = \infty` and :math:`\lim_{x \to 0-} f(x)=-\infty`. Even though this may seem obvious, how do you prove this?

	First, for the right-hand limit choose any real number :math:`M \in \mathbb{R}_+` and set :math:`\delta=1/M`. Then :math:`0<x<\delta=1/M` for which :math:`1/x > 1/\delta` and thus indeed :math:`f(x)>M`. For instance, let :math:`M=1000`; then :math:`x` has to stay in a :math:`\tfrac{1}{1000}`-th neighborhood to the right of :math:`x_0=0` in order to make sure that :math:`f(x)` is larger than :math:`M=1000`.
        
        Second, for the left-hand limit choose any real number :math:`M \in \mathbb{R}_-` and set :math:`\delta=-1/M`. Then :math:`1/M = -\delta < x < 0` for which :math:`-1/\delta > 1/x` (careful here!) and thus indeed :math:`1/x=f(x)<M`.
	

.. admonition:: Figure

        .. image:: ./pyplots/oneoverx.png


============================
Continuity 
============================

We now learn about one fundamental concept in the theory of functions.

.. admonition:: Definition (Continuity)

	Let :math:`X \subset \mathbb{R}` and let :math:`f: X \to \mathbb{R}` be a function. Let :math:`x_0 \in X`. We say that :math:`f` is continuous at :math:`x_0` iff we have
	
        .. math::

	        \lim_{x \to x_0} f(x) = f(x_0).
	
	We say that :math:`f` is continuous on :math:`X` (or simply continuous) iff :math:`f` is continuous at :math:`x_0` for every :math:`x_0 \in X`. We say that :math:`f` is discontinuous at :math:`x_0` iff it is not continuous at :math:`x_0`.


Therefore, for a function to be continuous at a point :math:`x_0` in the domain we need three things: the limit as :math:`x` approaches :math:`x_0` needs to exist, the function value at :math:`x_0` needs to exist, and both the limit and the function value need to be identical.


.. admonition:: Example

	Let :math:`f: \mathbb{R} \to \mathbb{R}` with :math:`f(x)=c` for some real number :math:`c`. Then for any :math:`x_0 \in \mathbb{R}` we have :math:`\lim_{x \to x_0} f(x) = \lim_{x \to x_0} c = c = f(x_0)` and thus :math:`f` is continuous at every point :math:`x_0 \in \mathbb{R}`. This in fact makes :math:`f` continuous on the whole real line :math:`\mathbb{R}`. 



.. admonition:: Question

        Let :math:`f: \mathbb{R} \to \mathbb{R}` with 
	
        .. math:: 
        
                f(x) = 
        	\begin{cases}
	        	0 & \text{if } x \neq 0 \\
		        1 & \text{if } x = 0.
        	\end{cases}
	
	For which values of :math:`x` is this function continuous? 


:math:`\diamondsuit`

===========
Exercises
===========

*Note: Solutions for exercises will only be given during the tutorials. They will not be posted here.*

(1)	Let :math:`f: \mathbb{R} \setminus \{0\} \to \mathbb{R}` be the function :math:`f(x) = 1/x`. Prove that
	
        .. math::

                \lim_{x \to \infty} f(x) = 0.
	


(#)	Let :math:`f: \mathbb{R} \to \mathbb{R}` be the function :math:`f(x) = e^{-x}`. Prove that
	
        .. math::

                \lim_{x \to \infty} f(x) = 0.
	

(#)	Use the limit laws and what you learned about limits at infinity and infinite limits to determine 
	
        .. math::

                \lim_{x \to \infty} \frac{e^{-x}}{x}.



(#)	Use the limit laws and what you learned about limits at infinity and infinite limits to determine 

        .. math::

                \lim_{x \to \infty} \frac{2x^2 - x +1}{3x^2 + 2x -1}.


(#)	Let :math:`f: \mathbb{R} \to \mathbb{R}` with :math:`f(x) = |x|`. Is this function continuous? Show your work!




(#)	Let :math:`f:\mathbb{R} \setminus \{0\} \to \mathbb{R}` with :math:`f(x) = 1/x`. For which values of :math:`x` is this function continuous? Show your work!

*Related exercises in the textbook you should study, include (but are not limited to):*

* Exercises 10-1 --- Problems 21-38, 43-74
* Exercises 10-2 --- Problems 9-52 
* Exercises 10-3 --- Problems 23-34, 57-62

*The tutors at the EMET1001 help desk are happy to help, if you have any questions.*



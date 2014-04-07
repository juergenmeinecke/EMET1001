***************************
Sequences, Series, Limits
***************************


============================
Sequences
============================

.. admonition:: Definition (Sequence)

	A **sequence** (or **infinite sequence**) is a real-valued function :math:`f` defined on the set of positive integers, i.e., :math:`f: \mathbb{N}\rightarrow \mathbb{R}`. If :math:`f(n) = a_n`, for :math:`n \in \mathbb{N}`, it is convention to write the sequence as :math:`\{a_n\}_{n=1}^\infty` or shorter as :math:`\{ a_n \}` or alternatively as :math:`a_1, a_2, a_3, \dots`. (The elements :math:`a_1, a_2, a_3,\ldots` are also called the terms of the sequence.)  


Note that the terms :math:`a_1, a_2, a_3,\dots` of a sequence need not be distinct.

.. admonition:: Example

        .. math::

		\left\{ \sqrt{n} \right\} & = \{ 1, 1.4142, 1.7321,\ldots \} \\
		\{ (-1)^n \} & = \{-1, 1, -1, \dots \} \\
		\left\{ \frac{1}{n^2+1} \right\} &= \left\{ \frac{1}{2}, \frac{1}{5}, \frac{1}{10}, \dots \right\} 


.. admonition:: Figure                

        .. image:: ./pyplots/sequences.png

Sequences can be finite too.

.. admonition:: Definition (Finite sequence)

	Let :math:`J=\{1,2,\ldots,n\}` for :math:`n \in \mathbb{N}`. A **finite sequence** is a real-valued function :math:`f` defined on :math:`J`, i.e., :math:`f: J \rightarrow \mathbb{R}`.  


.. admonition:: Definition (Arithmetic sequence)

	An **arithmetic sequence** :math:`\{ a_n \}` is a sequence such that :math:`a_{n+1}-a_n = d` for all :math:`n \in \mathbb{N}` and some :math:`d \in \mathbb{R}`. The constant :math:`d` is called the common difference.



.. admonition:: Proposition

        n-th term of an arithmetic sequence

	:math:`a_n = a_1 + (n-1) \cdot d`.


.. admonition:: Proof

	Omitted.



.. admonition:: Definition (Geometric sequence)

	A **geometric sequence** :math:`\{ a_n \}` is a sequence such that :math:`\tfrac{a_{n+1}}{a_n} = i` for all :math:`n \in \mathbb{N}` and some :math:`i \in \mathbb{R}\setminus \{0\}`. The constant :math:`i` is called the common ratio.



.. admonition:: Proposition

        n-th term of a geometric sequence

	:math:`a_n = a_1 \cdot i^{n-1}`.


.. admonition:: Proof

	Omitted.


It should be clear how the definitions of arithmetic and geometric sequences should be modified to yield *finite* arithmetic and geometric sequences.



============================
Convergence of Sequences
============================


.. admonition:: Definition (Convergence, limit)

	A sequence :math:`\{ a_n \}` converges to the **limit** :math:`a` if for every real number :math:`\epsilon>0` there exists a :math:`N \in \mathbb{N}` such that :math:`| a_n-a | \leq \epsilon` for all :math:`n \geq N`.

	We say that the sequence :math:`\{ a_n \}` is **convergent** and write :math:`\displaystyle\lim_{n \to \infty} a_n = a`. If a sequence does not converge it is **divergent**.




.. admonition:: Example

	Let :math:`\{ a_n \}` be such that :math:`a_n=6` for every :math:`n`. This sequence converges to :math:`a=6`. It is relatively easy to see that for any real number :math:`\epsilon >0` there exists a natural number :math:`N` such that :math:`|a_n-6| \leq \epsilon` for all :math:`n \geq N`. To see this, just set :math:`N=1` for which :math:`|a_n-6|=0 \leq \epsilon` for all :math:`n \geq N`. 
       

        
.. admonition:: Example

        The sequence :math:`\{-3,7,8,5,6,\pi,3,3,3,\ldots \}` converges to 3. To see this, write out as follows:

        For :math:`a=3`

        .. math::

                \begin{align*}
                        |a_1-a| & = |-3-3| = 6\\
                        |a_2-a| & = |7-3| = 4\\
                        |a_3-a| & = |8-3| = 5\\
                        |a_4-a| & = |5-3| = 2\\
                        |a_5-a| & = |6-3| = 3\\
                        |a_6-a| & = |\pi-3| = \pi-3\\
                        |a_7-a| & = |3-3| = 0 \leq \epsilon \\
                        |a_8-a| & = |3-3| = 0 \leq \epsilon \\
                        |a_9-a| & = |3-3| = 0 \leq \epsilon \\
                        & \; \vdots 
                \end{align*}

        which holds for any :math:`\epsilon >0` when :math:`N=7` and :math:`n \geq N`.

.. admonition:: Lemma (Archimedian principle)

        Let :math:`r` be a real number. Then there exists a natural number :math:`n` greater than :math:`r`. Formally,

        .. math::

                \forall r \in \mathbb{R}: \exists n \in \mathbb{N}: n > r     


.. admonition:: Proof

	Suppose the lemma is false and :math:`n < r` for all natural numbers :math:`n`. Then the set of natural numbers :math:`\mathbb{N}` is bounded above by :math:`r` and, by the Completeness Axiom (not stated here), it has a least upper bound :math:`M \in \mathbb{R}`. Since :math:`M` is the least upper bound, :math:`M-1` cannot be an upper bound. Thus, there is a natural number :math:`x \in \mathbb{N}` such that :math:`M-1 < x`. Adding 1 gives :math:`M < x+1` but :math:`x+1` must also be a natural number which contradicts the fact that :math:`M` is an upper bound of :math:`\mathbb{N}`.  



.. admonition:: Example

	Let :math:`a_n = \left\{ \frac{2n+1}{n+1} \right\}`. This sequence converges to 2. How do you prove this?
        
        We need to show that there exists a natural number :math:`N` such that :math:`|a_n-2| \leq \epsilon` for all positive real numbers :math:`\epsilon` and :math:`n \geq N`. Here, we can simplify and obtain :math:`| a_n-2 | = \left| \frac{2n+1}{n+1} - \frac{2n+2}{n+1} \right|= \frac{1}{n+1} < \frac{1}{n}`. Now pick :math:`N \in \mathbb{N}` such that :math:`1/N < \epsilon`. For any :math:`n \geq N` it also holds that :math:`1/n < \epsilon` and thus :math:`| a_n-2 | < \epsilon`. Therefore the sequence :math:`\{ a_n \}` converges to 2.

	Note: How do we know that there always exists an :math:`N \in \mathbb{N}` such that :math:`1/N<\epsilon`? This follows from the Archimedean Principle. 




.. admonition:: Example

	Does the sequence :math:`\{ n/2 + 1/n \}` converge? Let's assume that it indeed does converge to the real number :math:`a`. In that case we should be able show that the difference :math:`\left| \frac{n^2+2}{2n} - a \right|` can be made arbitrarily small by choosing :math:`n` large enough. Does this work here? Rewrite

        .. math::
                
                \begin{align*}
                        \left| \frac{n^2+2}{2n} - a \right| 
                        & = \left| \frac{n^2+2}{2n} - \frac{2an}{2n} \right|
                        = \left| \frac{n^2+2 - 2an}{2n} \right| \\
                        & > \left| \frac{n^2 - 2an}{2n} \right| 
                        = \left| \frac{n - 2a}{2} \right|, 
                \end{align*}
        
       
        where the last expression will be equal to or greater than zero for :math:`n \geq N` if :math:`N = 2a` (assuming, without loss of generality, that :math:`2a` is a natural number). It thus follows that :math:`\left| \frac{n^2+2}{2n} - a \right|` will be strictly greater than zero and can therefore not be made arbitrarily small by choosing large values for :math:`n`. In fact, for large values of :math:`n` the difference :math:`\left| \frac{n^2+2}{2n} - a \right|` becomes quite large. 
        



.. admonition:: Proposition (Limit laws for sequences)

	Let :math:`\{ a_n \}` and :math:`\{ b_n \}` be convergent sequences, and let :math:`a` and :math:`b` be their limits, i.e., :math:`a = \lim_{n \to \infty} a_n` and :math:`b = \lim_{n \to \infty} b_n`. Then,

		(i) :math:`\lim_{n \to \infty} c = c`, for any real constant :math:`c`

		(#) :math:`\lim_{n \to \infty} (a_n \pm b_n) = a \pm b`

		(#) :math:`\lim_{n \to \infty} (c \cdot a_n ) = c \cdot a` for any real constant :math:`c`

		(#) :math:`\lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b`  

		(#) :math:`\lim_{n \to \infty} ( b_n^{-1} ) = b^{-1}`, assuming that :math:`b \neq 0` and :math:`b_n \neq 0` for all :math:`n`  

		(#) :math:`\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{a}{b}`, assuming that :math:`b \neq 0` and :math:`b_n \neq 0` for all :math:`n` 

		(#) :math:`\lim_{n \to \infty} a_n^p = a^p`, for a real constant :math:`p>0` and assuming that :math:`a_n>0` for all :math:`n`




.. admonition:: Proof

	Omitted.


:math:`\diamondsuit`

============================
Finite Series
============================


.. admonition:: Definition (Summation operator)

	Given a sequence :math:`\{ a_n \}`, we use the **summation operator**
	
        .. math:: 

               \sum_{n=p}^q a_n \qquad (p,q \in \mathbb{Z} \text{ with } p \leq q)
        
	to denote the sum :math:`a_p + a_{p+1} + \cdots + a_q`. 



.. admonition:: Definition (Finite series)

	Given the sequence :math:`\{a_n\}`, we define the **finite series** :math:`S_n` by :math:`S_n = \sum_{k=1}^n a_k`. 


The finite series :math:`S_n` takes the first :math:`n` terms of the sequence :math:`\{ a_n \}` and adds them together. Note that we can construct a sequence :math:`\{ S_n \}` out of the series :math:`S_n`. The value of the finite series :math:`S_n` depends on the choice of :math:`n`. 


It should be obvious how one would define the concepts of finite arithmetic and finite geometric series.


.. admonition:: Definition (Finite arithmetic series)

	A **finite arithmetic series** :math:`S_n` is defined by the first term :math:`a_1` of an arithmetic sequence, the common difference :math:`d`, and the number of elements :math:`n` in the sequence: :math:`S_n = \sum_{k=1}^n a_1 + (k-1) \cdot d`.


It is easy to verify that :math:`S_n = a_1 + \cdots + a_n`, where :math:`a_1,\ldots, a_n` are the terms of the underlying arithmetic sequence. Some textbooks let the sum index start at zero, :math:`S_n = \sum_{k=0}^{n-1} a_1 + k \cdot d`. This, of course, is equivalent notation.


.. admonition:: Proposition 

	The :math:`n` terms of a finite arithmetic series :math:`S_n` add up to
	
        .. math::
                S_n = n (2 a_1 + (n-1) d) /2.
                :label: arithmetic_series	


.. admonition:: Proof

        .. math::

	        S_n     & = a_1 + a_2 + \cdots + a_n \\
	                & = a_1 + (a_1+d) + (a_1+2d) + \cdots + (a_1+(n-2)d) + (a_1+(n-1)d),


	and then rewriting in reverse order

        .. math::

        	S_n     & = (a_1+(n-1)d) + (a_1+(n-2)d)+ \cdots + (a_1+2d) + (a_1+d) + a_1.

        Thus for :math:`2 S_n` we get

        .. math::

	        2 S_n   & = (2a_1 + (n-1)d) + (2a_1 + (n-1)d) + \cdots + (2a_1 + (n-1)d) + (2a_1 + (n-1)d) \\
                	& = n (2a_1 + (n-1)d),

        which yields the result.



.. admonition:: Corollary

	Alternatively, the :math:`n` terms of a finite arithmetic series :math:`S_n` add up to

        .. math::

                S_n = n \cdot \frac{a_1 + a_n}{2}.


.. admonition:: Proof

	Replace :math:`a_1 + (n-1)d` in equation :eq:`arithmetic_series` by :math:`a_n`. (Why is this justified?)


        
.. admonition:: Definition (Finite geometric series)

	A **finite geometric series** :math:`S_n` is defined by the first term :math:`a_1` of a geometric sequence, the common ratio :math:`i`, and the number of elements :math:`n` in the sequence: :math:`S_n = \sum_{k=1}^n a_1 \cdot i^{k-1}`.



.. admonition:: Proposition

	The :math:`n` terms of a finite geometric series :math:`S_n` add up to

        .. math::
        	S_n = \frac{a_1 (i^n-1)}{i-1}, \qquad \text{ for } i \neq 1.
                :label: geometric_series
	

.. admonition:: Proof

        .. math::	

		S_n 
		&= a_1 + a_2 + \cdots + a_n \\
		&= a_1 + a_1 i + a_1 i^2 + \cdots + a_1 i^{n-2} + a_1 i^{n-1}, 

        and then multiplying both sides by :math:`i`

        .. math::

		i S_n
		&= a_1 i + a_1 i^2 + a_1 i^3 + \cdots + a_1 i^{n-1} + a_1 i^{n}.

        Subtracting gives

        .. math::

		iS_n - S_n
		&= a_1 i^n - a_1,

        which yields the result.



.. admonition:: Corollary

	Alternatively, the :math:`n` terms of a finite geometric series :math:`S_n` add up to
	
        .. math::
        	S_n = \frac{i a_n - a_1}{i-1}, \qquad\;\;\; \text{ for } i \neq 1.
	


.. admonition:: Proof

	Since :math:`a_n=a_1 i^{n-1}`, or equivalently :math:`a_1 i^n = i a_n`, plugging into equation :eq:`geometric_series` delivers the result.


============================
Infinite Series
============================

So far we defined finite series. But how would we handle objects such as :math:`\sum_{k=1}^\infty a_k`? It seems reasonable to think of this as an infite series. But how would we determine its 'value'? For example, what is :math:`\sum_{k=1}^\infty 1 = 1 + 1 + 1 + \cdots` (a never-ending sum of ones) equal to? 

To address this problem, we need to define the concept of convergence for infinite series. Before we do that, let's properly define the term.

.. admonition:: Definition (Series)

	An **infinite series** (or just a series) is any expression of the form 
        
        .. math::
	        \sum_{n=1}^\infty a_n,
	
        where :math:`a_n` is a real number. We sometimes write this series as :math:`a_1+a_2+a_3+\cdots`.


Out of convention, we changed the index variable to :math:`n`. This is just a label, it does not matter whether we use :math:`k`, :math:`n`, or any other symbol. Also, for convenience, we sometimes label an infinite series :math:`\sum_{n=0}^\infty a_n` instead (this will become clear later in context). 



.. admonition:: Definition (Convergence of series)

	The infinite series :math:`\sum_{n=1}^\infty a_n` is said to **converge** to the real number :math:`S` if the sequence :math:`\{ S_n \}` of partial sums :math:`S_n= \sum_{k=1}^n a_k` converges to :math:`S`. We write 

        .. math::

        	\sum_{n=1}^\infty a_n = S.
	
        If the sequence of partial sums :math:`\{ S_n \}` diverges then we say that the infinite series **diverges** (or is divergent).



The definition of convergence of an infinite series is thus based on the definition of convergence of the underlying sequence. In that sense we are not defining a new concept of convergence. Convergence of a series is understood as convergence of a sequence.

This suggests that the convergence behavior of a sequence may influence whether or not the related series converges. There exists a handy result that links the two.



.. admonition:: Proposition (Zero test)

	Let :math:`\{a_n\}` be a sequence. If :math:`\lim_{n \to \infty} a_n` is non-zero, then the series :math:`\sum _{n=1}^\infty a_n` is divergent.


.. admonition:: Proof

	Omitted.




.. admonition:: Example

	The sequence :math:`\{1,1,1, \ldots \}` clearly does not converge to zero. By the zero test, we know that :math:`\sum_{n=1}^\infty 1 = 1+1+1+\cdots` is a divergent infinite series. Note though that the underlying sequence :math:`\{1,1,1, \ldots \}` itself is actually convergent (to 1, obviously). 


On the other hand, if a sequence :math:`\{ a_n \}` does converge to zero, then the series :math:`\sum_{n=1}^\infty a_n` may or may not converge. It depends. Take, for example, the sequence :math:`\{ 1/n \}`. The series :math:`\sum_{n=1}^\infty 1/n` diverges even though :math:`1/n` converges to zero (see exercises below).

Now we state and proof a result that is used in finance, accounting and financial econometrics all the time. 

.. admonition:: Proposition

	The series :math:`\sum_{n=1}^\infty i^{n-1}` converges to :math:`1/(1-i)` if :math:`-1<i<1`.




.. admonition:: Proof

	The finite sums :math:`S_n = \sum_{k=1}^n i^{k-1}` are straightforward geometric series. By Proposition \ref{prop: geometric series} we have :math:`S_n = (1-i^n)/(1-i)`. To get the limit of the series, we need to get the limit of the sequence :math:`\{ S_n \}`. This requires us to show that there exists a natural number :math:`N` such that 

        .. math::
                \left| \frac{ (1-i^n)}{1-i} - \frac{1}{1-i} \right| = \left| \frac{-i^n}{1-i} \right| < \epsilon 
	

        for any real number :math:`\epsilon>0` and :math:`n \geq N`. We will not prove this rigorously here but appeal to the intuition that indeed :math:`\left| -i^n \right|` is positive and can be made arbitrarily small by picking :math:`n` large enough. (Note that the denominator is positive and finite.)



:math:`\diamondsuit`







===========
Exercises
===========

*Note: Solutions for exercises will only be given during the tutorials. They will not be posted here.*

1) You deposit \$2,000 in a bank account which pays 6\% interest each year. You do not withdraw money and keep it in the bank for :math:`12` years. What is the amount of money :math:`A` saved over that time span? Provide a formula for :math:`A` in terms of the principal :math:`P`, the interest rate :math:`r` and the time span :math:`T`. (Apply the :math:`n`-th term formula for geometric sequences. How do :math:`A, P, r` and :math:`T` relate to the elements of the :math:`n`-th term formula?) 

	
	
#) Redo the previous exercise assuming that the bank pays a *nominal* annual interest rate of 6\% compounded half-yearly. What is the amount of money :math:`A` saved over that time span? Provide a formula for :math:`A` in terms of the principal :math:`P`, the interest rate :math:`r` and the time span :math:`T` as well as the number of compounding periods per year :math:`m`. (How do :math:`A, P, r, m` and :math:`T` relate to the elements of the :math:`n`-th term formula?)			

	
	
#) Redo the previous exercise with monthly and daily (assume that the year has 365 days) and continuous compounding. For all five cases of compounding, what is the *effective annual rate* (also called the annual percentage yield)? (See textbook for definition.)

			
#) Given your initial deposit of \$2,000 and the 6\% nominal interest rate, how long will it take you to save up \$5,000? (Calculate this for monthly as well as continuous compounding.) 

#) What is the limit of the sequence :math:`\left\{ \tfrac{3n+2}{n+1}\right\}`? Prove.
   (*Note: Depending on time constraints, part or all of this question will also be answered in next week's tutorial.*)

*You can find related exercises in the textbook under:* 

* Exercises 3-1 and 3-2.

*Make sure to use these to practice with! The tutors at the EMET1001 help desk are happy to help, if you have any questions.*



6)      On her 25th birthday, Maria has nothing better to do than worry about her financial situation when she retires. She wants to save up enough money for a comfortable retirement. On the website of the Association of Superannuation Funds of Australia (ASFA) Maria discovers that she needs \$3,350 a month for a comfortable retirement lifestyle in NSW (as a single female retiree). She would like to retire on her 65th birthday. 

        The current life expectancy at age 65 for females is about 22 years. This means, that a 65 year old woman is currently expected to live until age 87. Maria is conservative and factors in that technological progress in medical treatment will raise her life expectancy (once she reaches 65) to 30 years. She therefore wants to make sure that she can guarantee a secure monthly income stream of \$3,350 for 30 years starting at her 65th birthday. (Note: For simplicity, we ignore inflation.)

        Maria's bank promises a 5.5\% nominal annual interest rate compounded monthly forever. 

        	(i) On her 65th birthday, how much money needs to be in Maria's bank account to guarantee a comfortable retirement? (She does not plan to leave an inheritance.)

        	(#) How much money would Maria need to have now (at her 25th birthday) to guarantee that she can retire at age 65 with the amount of savings determined under part (i)? (This question asks for the *present value*.) 

        	(#) Maria currently has no savings but luckily she has a steady job. In order to come up with the necessary retirement savings, she decides to put aside a constant dollar amount (an *annuity*) at the beginning of every month until she retires. How much money should Maria set aside each month?
	

7)      Prove that the series :math:`\sum_{n=1}^\infty 1/n` diverges. Recall from the lecture that the underlying sequence :math:`\{1/n\}` does converge to zero. To answer this question, you need to study the convergence behavior of the sequence of *partial sums* :math:`\{S_n\}` where each partial sum is defined by :math:`S_n=\sum_{k=1}^n 1/k`.



*You can find related exercises in the textbook under:*

* Exercises 3-3 and 3-4. 

*Make sure to use these to practice with! The tutors at the EMET1001 help desk are happy to help, if you have any questions.*








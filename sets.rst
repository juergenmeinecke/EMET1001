***************************
Sets, Relations, Functions
***************************


============================
Set Theory
============================

We start by defining what sets are

.. admonition:: Definition (Set)

   A **set** is a collection of distinct objects.

   
.. admonition:: Example
   
   All students sitting in this room.

   All students standing in this room. (empty set?)
   
   The numbers :math:`8, 10, -4,349`.


Two ways of defining sets:

* By description
* By enumeration


.. admonition:: Example
    
   All students sleeping during lecture. (description)
   
   All non-negative integers. (description)
    
   :math:`S = \{ 3, 12, -5,555 \}`. (enumeration)


If two sets :math:`A` and :math:`B` contain exactly the same elements, that is, :math:`x \in A \text{ iff } x \in B`, then it is said that both sets are identical, writing :math:`A=B`. Otherwise we write :math:`A \neq B`. (Reminder: iff means \`if and only if\'.)


.. admonition:: Example

        .. math::
         
           \{x, y \} &= \{y, x \}\\
	   \{x, x \} &= \{ x \}\\
	   \{ \{x\} \} & \neq \{x\} \text{(why?)}


.. admonition:: Definition (Empty set)

	The **empty set**, denoted :math:`\emptyset` is the set that contains no element; if a set contains at least one element it is called nonempty.

.. admonition:: Definition (Subset)

	Let :math:`A` and :math:`B` be sets. We say that :math:`A` is a **subset** of :math:`B` if :math:`x \in A` implies :math:`x \in B`. We write :math:`A \subset B`. 

Intuitively, the set :math:`A` is a subset of :math:`B` whenever it is contained in :math:`B`.

.. admonition:: Definition (Natural numbers)

	The set of **natural numbers** is denoted by :math:`\mathbb{N}` and defined by :math:`\mathbb{N} = \{1,2,3,\dots\}`. This set is also called the set of positive integer numbers.

.. admonition:: Definition (Integer numbers)

	The set of **integer numbers** is denoted by :math:`\mathbb{Z}` and defined by :math:`\mathbb{Z} = \{\dots,-3,-2,-1,0,1,2,3,\dots\}`.

.. admonition:: Definition (Non-positive integer numbers)

	The set of **non-positive integer numbers** is denoted by :math:`\mathbb{Z}_{-}` and defined by :math:`\mathbb{Z}_{-} = \{\dots, -3, -2, -1, 0\}`.

.. admonition:: Definition (Negative integer numbers)

	The set of **negative integer numbers** is denoted by :math:`\mathbb{Z}_{--}` and defined by :math:`\mathbb{Z}_{--} = \{\dots, -3, -2, -1 \}`.

.. admonition:: Definition (Rational numbers)  

	The set of **rational numbers** is denoted by :math:`\mathbb{Q}` and defined by :math:`\mathbb{Q}=\left\{ \tfrac{p}{q} | p \in \mathbb{Z}, q \in \mathbb{Z} \setminus \{0\} \right\}`.


Is the set of rational numbers complete? Intuitively, for :math:`\mathbb{Q}` to be complete we need to be able to solve any equation within the set of rational numbers. 

.. admonition:: Example

	Imagine a square with side length 1. What is the length of its diagonal :math:`r`? We know from geometry that :math:`r^2 = 1^2 + 1^2`. The question now is whether :math:`r \stackrel{?}{\in} \mathbb{Q}`. Suppose that indeed :math:`r^2 =2` for some :math:`r \in \mathbb{Q}`. Thus, :math:`r` can be expressed as the ratio :math:`\tfrac{p}{q}` with :math:`q \neq 0`. Here :math:`p` and :math:`q` do not have a common factor. (Note: If they did have a common factor we could cancel it out and continue the analysis with :math:`p'` and :math:`q'` which now denote the equivalents of :math:`p` and :math:`q` after removing the common factor.) Then clearly, :math:`p^2 = 2 q^2` which implies that :math:`p^2` must be an even integer. This in turn is only possible if :math:`p` itself is an even integer. We can therefore write :math:`p` as :math:`p=2k` for some :math:`k \in \mathbb{Z}`. It follows that :math:`2q^2 = 4 k^2` so that :math:`q^2 = 2 k^2`. By a similar argument to before, :math:`q^2` must be even and then also :math:`q` must be an even integer. But then :math:`p` and :math:`q` share the common factor 2 which contradicts what we assumed earlier.  

In other words, :math:`r \notin Q`. The rational numbers contain 'holes'. In the above example, the number :math:`\sqrt{2}` is the solution for :math:`r` which is not part of the rational numbers. In fact, many square roots are not members of the rational numbers (but some are!). Other examples of 'holes' in the rational numbers are: :math:`\pi, e, \log_2 7`. There are in fact infinitely many such 'holes' in the rational numbers. Without digging too deep, we want to come up with a 'complete' set of numbers that fills up all the 'holes'. It turns out that the real numbers accomplish this. If we denote the set of irrational numbers by :math:`\mathbb{I}` we can afford a formal defintion of the real numbers:

.. admonition:: Definition (Real numbers) 

	The set of **real numbers** is denoted by :math:`\mathbb{R}` and defined by 
        
        .. math::
           \mathbb{R} = \mathbb{Q} \cup \mathbb{I}
           :label: realnumbers 

This definition has a slightly tautological flavor. We have not really defined precisely what the irrational numbers are. (And we will not have the time this semester!) But if we had that definition :eq:`realnumbers` then the preceding definition would succinctly define the real numbers. For now, all we need to understand is that the irrational numbers fill ALL the remaining gaps of the rational number system. It is therefore pleasant to work in the real number system.




.. admonition:: Definition (Intervals)
	
        We distinguish between the following special sets of real numbers, so-called **intervals**. Let :math:`a,b \in \mathbb{R}` and suppose that :math:`a \leq b`, then define:
        
		* **Closed interval**: :math:`[a,b] = \{x \in \mathbb{R} | a \leq x \leq b \}`

		* **Open interval**: :math:`(a,b) = \{x \in \mathbb{R} | a < x < b \}`

		* **Half-open interval**: :math:`[a,b) = \{x \in \mathbb{R} | a \leq x < b \}`
                  
		* **Half-open interval**: :math:`(a,b] = \{x \in \mathbb{R} | a < x \leq b \}`

		* :math:`(-\infty,a] = \{x \in \mathbb{R} | x \leq a \}`

		* :math:`(-\infty,a) = \{x \in \mathbb{R} | x < a \}`

		* :math:`[a,\infty) = \{x \in \mathbb{R} | x \geq a \}`

		* :math:`(a,\infty) = \{x \in \mathbb{R} | x > a \}`

Note, as the symbols :math:`\pm \infty` do not describe any real number (i.e., :math:`\pm \infty \notin \mathbb{R}`), there is no such thing as :math:`[-\infty,a]` or :math:`[-\infty,a)` or :math:`[a,\infty]` or :math:`(a,\infty]`.



Assumed knowledge: Notions of subset, union, intersection, and complement (see textbook). 




===============================
Relations and Functions
===============================

.. admonition:: Definition (Ordered pair)

	An **ordered pair** is an ordered list :math:`(a,b)` consisting of two objects :math:`a` and :math:`b`. The ordered pair is ordered in the following sense: For any two ordered pairs :math:`(a,b)` and :math:`(a',b')`, we have :math:`(a,b) = (a',b')` iff :math:`a=a'` and :math:`b=b'`.


.. admonition:: Example

	Understand the difference b/w :math:`\{1,3\} = \{3, 1\}` but :math:`(1,3) \neq (3,1)`.


.. admonition:: Definition (Cartesian product)

	The **Cartesian product** of two nonempty sets :math:`A` and :math:`B`, denoted by :math:`A \times B`, is defined as the set of all ordered pairs :math:`(a,b)` where :math:`a` comes from :math:`A` while :math:`b` comes from :math:`B`. Formally: :math:`A \times B = \{(a,b) | a \in A, b \in B \}`


.. admonition:: Definition (Relation)

	Let :math:`X` and :math:`Y` be two nonempty sets. A subset :math:`R` of :math:`X \times Y` is called a **relation** from :math:`X` to :math:`Y`. 


.. admonition:: Example 

	The set :math:`\{(x,y) | y \leq 2x \}` is a relation. (Is it also a function?)


Relations broadly link two sets :math:`X` and :math:`Y`. We now want to move on to the more narrow concept of function. Functions transform the elements of one set to those of another. More precisely, this is what we mean by function:



.. admonition:: Definition (Function, domain, codomain)

	A **function** :math:`f` that maps the set :math:`X` into the set :math:`Y`, denoted by :math:`f:X \rightarrow Y`, is a relation :math:`f \subset X \times Y` such that

		* for every :math:`x \in X` there exists a :math:`y \in Y` such that :math:`(x,y) \in f`;
		* for every :math:`y,z \in Y` with :math:`(x,y) \in f` and :math:`(x,z) \in f` we have :math:`y = z`.

	Here :math:`X` is called the **domain** of :math:`f` and :math:`Y` is called the **codomain**. 
        

Sometimes, instead of the word 'function' we use the word 'map'. 


.. admonition:: Example

	The set of all functions that map :math:`X` into :math:`Y` is denoted by :math:`Y^X`. For example, :math:`\{0,1\}^X` is the set of all functions on :math:`X` whose values are either :math:`0` or :math:`1`. Likewise, :math:`\mathbb{R}^{[0,1]}` is the set of all real-valued functions on :math:`[0,1]`. 


Does the above definition of a function look a bit strange? What do we want a function to do? It is supposed to map each member of :math:`X` to a member of :math:`Y`. Well, all that :math:`f` does is completely given by the set :math:`\{(x, f(x)) \in X \times Y | x \in X\}`. The more familiar notation :math:`f(x) = y` (which we will mostly use throughout the course) is then merely an alternative way of expressing :math:`(x,y) \in f`.


.. admonition:: Definition (Image, range, inverse image)

	Let :math:`f: X \to Y` be a function. Let :math:`E \subset X`. Then :math:`f(E)` is defined to be the set of all elements :math:`f(x)` such that :math:`x \in E`, formally: :math:`f(E) = \{ f(x) | x \in E \subset X \}`. We call :math:`f(E)` the **image** of :math:`E` under :math:`f`. The special case :math:`f(X)` is called the **range** of :math:`f`. (The range is the subset of the codomain that the function actually attains.)

	Now let :math:`E \subset Y`. Then :math:`f^{-1}(E)` is defined to be the set of all :math:`x \in X` such that :math:`f(x) \in E`, formally :math:`f^{-1}(E) = \{x \in X | f(x) \in E \subset Y \}`. We call :math:`f^{-1}(E)` the **inverse image** of :math:`E` under :math:`f`.

:math:`\diamondsuit`

Condition (i) in the definition of a function therefore says that every element in the domain :math:`X` of :math:`f` has an image under :math:`f` in the codomain :math:`Y`. Condition (ii) states that no element in the domain of :math:`f` can have more than one image under :math:`f`.


.. admonition:: Definition (Surjection)

	A function :math:`f: X \to Y` is a **surjection** if :math:`f(X) = Y`. In other words, a surjective function has a range that is equal to its codomain. We say that :math:`f` maps :math:`X` onto :math:`Y`. (The function may also be called **surjective** or **onto**.)


.. admonition:: Definition (Injection)

	A function :math:`f: X \to Y` is an **injection** if :math:`x \neq y` implies :math:`f(x) \neq f(y)` for all :math:`x,y \in X`, in other words, if :math:`f` maps distinct points in its domain to distinct points in its codomain. (The function may also be called injective or one-to-one.) Equivalently, the function is an injection if :math:`f(x) = f(y)` implies :math:`x=y` for all :math:`x,y \in X`.



        
.. admonition:: Definition (Bijection)

	A function :math:`f` is a **bijection** if it is both surjective and injective. (The function may also be called bijective.)



.. admonition:: Example

	If :math:`X=\{1,\dots, 10\}`, then :math:`f=\{(1,2), (2,3),\dots,(10,1)\}` is a bijection in :math:`X^X`. However, the function :math:`g \in X^X` given by :math:`g(x)=3` for all :math:`x \in X` is neither an injection nor a surjection. 


.. admonition:: Question

        Let :math:`f` from the preceding example be a map in :math:`\big( \{0\} \cup X \big)^X`. Is it an injection? A surjection?

.. admonition:: Question

        Let the *identity function* be an element of the space :math:`X^X` (functions in this space are also called *self-maps*), denote it by :math:`\text{id}_X` and define it by :math:`\text{id}_X = x` for all :math:`x \in X`. Is :math:`\text{id}_X` a bijection? 



.. admonition:: Definition (Inverse)

	For any function :math:`f \in Y^X` define the set :math:`f^{-1} = \{(y,x) \in Y \times X | (x,y) \in f \}`. If :math:`f^{-1}` itself is a function then we say that :math:`f` is **invertible** and :math:`f^{-1}` is the **inverse** of :math:`f`. 


.. admonition:: Example

	Let :math:`f: \mathbb{R} \rightarrow \mathbb{R}_{+}` given by :math:`f(t) = t^2`. Then :math:`(1,1) \in f^{-1}` but also :math:`(1,-1) \in f^{-1}`, that is, :math:`1` does not have a unique image under :math:`f^{-1}` and therefore is not a function.


.. admonition:: Example

	Take the same :math:`f` as in the preceding example but restrict the domain to positive real numbers. Thus, :math:`f: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}`. Then :math:`f^{-1}(t) = \sqrt{t}` for all :math:`t \in \mathbb{R}_+` is indeed a function.

.. admonition:: Proposition

        A function :math:`f: X \to Y` is invertible iff it is bijective.

.. admonition:: Question
        
        Does invertibility imply injectivity? Conversely, does injectivity imply invertibility? The first question is answered directly by the preceding proposition: invertibility implies bijectivity and thus injectivity. But does an injective function need to be invertible? Just reconsider the example from above, in which :math:`X=\{1,\ldots,10\}` and :math:`f \in \big( \{0\} \cup X \big)^X` with :math:`f=\{(1,2), (2,3),\dots,(10,1)\}`.  

===========
Exercises
===========

*Note: Solutions for exercises will only be given during the tutorials. They will not be posted here.*

1) Let :math:`f: (-\infty,2] \cup [3,\infty) \to \mathbb{R}` be given by :math:`f(x) = \sqrt{x^2 -5x +6}`.

	(i) What are the domain and codomain of :math:`f`?

	(#) Sketch the function. 
            (Hint: First think about how the graph of :math:`x^2-5x+6` looks like. Then think about how its square root looks like, especially for large values of :math:`|x|`.)

 	(#) Let :math:`E = [4,5]`. What is the image of :math:`E` under :math:`f`? 

	(#) Now let :math:`E=[\sqrt{12},\infty)`. What is the inverse image of :math:`E` under :math:`f`? 

	(#) What would be the inverse image if instead :math:`E=[\sqrt{-8},\sqrt{-7}]`? 

	(#) What is the range of the function :math:`f`? Is it equal to the codomain?

#) (Cardinality of sets) The notion of cardinality in set theory concerns the size of sets. Consider the following definition.

   .. admonition:: Definition

      We say that two sets :math:`X` and :math:`Y` have **equal cardinality** iff there exists a bijection :math:`f: X \to Y` from :math:`X` to :math:`Y`. 

      Let :math:`n` be a natural number. A set :math:`X` is said to have **cardinality n**, iff it has equal cardinality with the set :math:`\{1,2,\ldots,n\}`.	

   Prove the following:

        (i) The set :math:`\{ c,b,a \}` has cardinality 3.

        (#) The sets :math:`\{0,1,2\}` and :math:`\{d,e,f\}` have equal cardinality.

        (#) The set of natural numbers and the set of even natural numbers have equal cardinality. (This seems counterintuitive: the set of even natural numbers seems to be contained in the set of natural numbers, yet they have equal cardinality.)


#) (Countability and finiteness of sets). The notions of countability and finiteness should be more or less intuitive. We do not want to rigorously define these concepts here; instead, use your intuition to assign the following sets into the right position in the table below.

        (i) :math:`\{4, \psi, -342\}`

        (#) :math:`\mathbb{N}` 

        (#) :math:`\mathbb{Z}` 
        
        (#) :math:`[-34, 102]` 
        
        (#) :math:`\mathbb{R}` 

   +----------+-----------+-------------+
   |          | Countable | Uncountable |
   +----------+-----------+-------------+
   | Finite   | ?         | ?           |
   +----------+-----------+-------------+
   | Infinite | ?         | ?           |
   +----------+-----------+-------------+




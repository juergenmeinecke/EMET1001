**************************
Cost and Profit Functions
**************************

========================
Total and Average Cost
========================

Example of a total cost function:

.. math::

	TC(q) = aq^2 + bq +c,

with :math:`c>0` and :math:`q \geq 0`. This gives the total cost as a function of output :math:`q`. This is a generic *quadratic* cost function. Of course, cost functions do not need to be quadratic.

Decomposition of :math:`TC`:

.. math::

	TC(q) 
	&= \underbrace{TVC(q)}_{\text{total variable cost}} &&+ \underbrace{TFC(q)}_{\text{total fixed cost}} \\
	&= (aq^2+bq) &&+ c.

Average total cost

.. math::

	ATC(q) := TC(q)/q = \tfrac{aq^2+bq+c}{q} = aq+b+c/q.

.. admonition:: Example

	:math:`a=5`, :math:`b=5`, :math:`c=2,000`. Then :math:`TC(0)=2,000`, :math:`TC(1000)=5,007,000` and :math:`ATC(1000)=5,007`. The last result means that each of the :math:`1,000` units cost, *on average* \$ 5,007 to produce. Note: This does not mean that each unit cost \$ 5,007 to produce. Some units may cost more, some less. But on average each cost \$ 5,007. This is the important distinction between *marginal* cost and *average* cost, as will become clearer later.


.. admonition:: Figure

        .. image:: ./pyplots/totalandaveragecost.png
                 
        Relationship between :math:`TC(q)` and :math:`ATC(q)`-curves. The :math:`ATC(q)`-curve (bottom) can be derived from the slopes of the secant lines (top, dashed lines). These secant lines connect the origin to points on the :math:`TC(q)`-curve. Three such secant lines are shown here; there are, of course, infinitely many more, eventually tracing out the entire :math:`ATC(q)`-curve. 
        
Asymptotic behavior of ATC

.. math::

	ATC(q)
	:= & \frac{TC(q)}{q} = \frac{TVC(q) + TFC(q)}{q} \\
	=& \frac{TVC(q)}{q} + \frac{TFC(q)}{q} \\
	=& AVC(q) + AFC(q) \\
	=& aq + b + c/q.

What happens to :math:`AFC(q)` as :math:`q \to 0`? Well, :math:`\lim_{q \to 0+} AFC(q) = \lim_{q \to 0+} c/q = \infty`.

What happens to :math:`AFC(q)` as :math:`q \to \infty`? Well, :math:`\lim_{q \to \infty} AFC(q) = \lim_{q \to \infty} c/q = 0`.


.. admonition:: Figure

        .. image:: ./pyplots/averagefixedcost.png

        Typical shape of an average fixed cost curve. In words: Fixed cost are spread over large output :math:`q`, each output unit carries an infinitesimally small fixed cost. Asymptotically, the fixed cost become irrelavant. In practice, firms with large fixed cost tend to produce a very large amount of output to spread fixed cost by as much as possible (example: power companies, utilities, car producers).


===================
Marginal cost
===================

.. admonition:: Definition (Marginal cost)

	For any total cost function :math:`TC(q)`, the *marginal cost* are defined by

        .. math::

		MC(q) := TC'(q) = \frac{dTC(q)}{dq}.

By this definition, the marginal cost are merely the slope of the TC.

Independence between :math:`MC` and :math:`TFC`

Recall that

.. math:: 

	TC(q) 
	&= TVC(q) + TFC(q) \\
	MC(q)
	&:= \frac{dTC(q)}{dq} \\
	&= \frac{dTVC(q)}{dq} + \frac{dTFC(q)}{dq},

but the last term is equal to zero because :math:`TFC` is just a constant function. Thus,

.. math::

	MC(q) = \frac{TC(q)}{dq} = \frac{dTVC(q)}{dq}

and it follows that marginal cost are equal to the slope of the :math:`TC` (which we knew already) and also are equal to the slope of the :math:`TVC`.

============================================================
Relationship between :math:`MC` and :math:`ATC`
============================================================

Recall that :math:`ATC(q) := TC(q)/q`. We want to study the relationship between various cost functions at the minimum of the :math:`ATC`. Let's start by deriving that minimum. To find the minimum, we look at the first order necessary condition.

.. math::

	\frac{dATC(q)}{dq} = \frac{TC'(q) \cdot q - TC(q) \cdot 1}{q^2}.

The necessary condition for :math:`ATC` to attain a local minimum is :math:`dATC(q)/dq = 0`. Therefore we need

.. math::

	0 = \frac{TC'(q) \cdot q - TC(q) \cdot 1}{q^2},

which is equivalent to having :math:`0 = TC'(q) \cdot q - TC(q)`. Rearranging yields the necessary condition 

.. math::

	\frac{TC(q)}{q} 
	&= TC'(q) 
	\Leftrightarrow ATC(q) = MC(q).	

So far, all we can say is that at local extrema of :math:`ATC` we have that :math:`ATC=MC`. We set out to study the behavior of various cost functions at the local minimum of the ATC. We therefore still need to make sure that we restrict our attetion to minima only. To do so, we study the second order condition next.

Recall

.. math::

	\frac{ATC(q)}{dq} = \frac{TC'(q) \cdot q - TC(q)}{q^2},

then

.. math::

	\frac{d^2 ATC}{dq^2} 
	&= \frac{\big(TC''(q) \cdot q + TC'(q) - TC'(q) \big) \cdot q^2 - \overbrace{ \big( TC'(q) \cdot q - TC(q) \big) }^{=0 \text{ b/c of necessary condition}} \cdot 2q}{q^4} \\
	&= \frac{\big( TC''(q) \cdot q \big) \cdot q^2}{q^4} = \frac{TC''(q)}{q} = \frac{dMC(q)}{dq} \cdot \frac{1}{q}.

For a local minimum of :math:`ATC` we therefore need that

.. math::

	\frac{d^2 ATC(q)}{dq^2} = \frac{dMC(q)}{dq} \cdot \frac{1}{q} > 0.

Because we always assume that :math:`q>0` this condition holds whenever :math:`dMC(q)/dq >0`. In words, at the minimum of the :math:`ATC`, the :math:`MC` curve cuts the :math:`ATC` curve from below. When :math:`MC` are below the :math:`ATC` then the :math:`ATC` are falling. (One could interpret this as the :math:`MC` pulling down the :math:`ATC` to the minimum. After that, the :math:`MC` are pushing the :math:`ATC` up away from the minimum.)

.. admonition:: Figure
        
        .. image:: ./pyplots/totalmarginalandaveragecost.png

        The :math:`MC(q)`-curve cuts the :math:`ATC(q)`-curve from below at the minimum of the :math:`ATC(q)`-curve.


:math:`\diamondsuit`

=========================
Exercises
=========================

(1)     A firm has total cost function :math:`TC(q) = 0.5q + 2` for :math:`q \in [0,10]`. 

        (i)     Sketch the graph of the total cost function.
        (#)     Find the marginal and average total cost functions. Sketch their graphs.
        (#)     Explain in words why average total cost is greater than marginal cost at all levels of output.
        (#)     If the TC function is linear, on what assumption can :math:`MC=ATC`?



(#)	A firm has total cost function :math:`TC(q) = q^2 - 3q + 500`. The firm sells in a perfectly competitive market at ruling market price :math:`p=67`.

        (i)     Find the most profitable level of output and the profits at that output.
        (#)     Does the firm produce at minimum average total cost? Explain.
        (#)     Sketch the graphs of total cost and total revenue with the same axes, and do the same with marginal cost and marginal revenue.
        (#)     Sketch the graph of the profit function.
        (#)     Assume the market price rises first to 68, then 69, then 70. What's the firm's response to these price increases? Can you deduce from this the firm's supply function (i.e., the relationship between market price and the quantity the firm chooses to supply)? Illustrate with a sketch the graph of the supply function.
        (#)     Use the supply function calculated in part (v) to find the price that would induce the firm to produce at minimum average total cost.
        (#)     Suppose the fixed costs rise from 500 to 1000 (market price is back to 67). What effect will this have on the firm's chosen level of output? Profits?




==========================
Profit Maximization
==========================

Firms do not minimize cost, they maximize profits. Profit is defined as the difference between total revenues and total cost.

.. math::

        \Pi(q) = TR(q) - TC(q)

.. admonition:: Example

        A firm sells mobile phones for \$124 a piece. The firm cannot set it`s own market price; instead it accepts the price that is dictated by the market (i.e., this firm is a price-taker). Its total cost of producing :math:`q` units are given by the function :math:`2q^2 + 4q + 600`. How much should the firm produce to maximize profits?

        Intuitively, the total revenue function is just a linear function starting in the origin with slope equal to the market price. Therefore the profit function is

        .. math::
        
                \Pi(q) 
                &= 124q - 2q^2 - 4q - 600\\
                &= -2q^2 + 120q - 600 

        To maximize profit, we only need to study the first order condition 

        .. math:: 

                \frac{d\Pi(q)}{dq} = -4q + 120 = 0

        .. admonition:: Figure

                .. image:: ./pyplots/profitmaximization.png

        We infer that this firm *may* maximize its profit by producing 30 units. Of course, as we have learnt earlier in this course, setting the first derivative equal to zero is not sufficient for finding a local maximum. We could just as well have detected a profit minimum. To rule this out, we need to check the second derivative. We can easily convince ourselves that the second derivative evaluates to :math:`-4` at :math:`q=30` and hence we find that indeed the firm is maximizing its profits by producing 30 units.                

Now we would like to derive a more general result that relates revenue and cost to the profit maximizing behavior of the firm. Instead of using a particular price and a particular total cost function, we keep things generic. Recall, the general profit function of the firm was

.. math::

        \Pi(q) = TR(q) - TC(q)

The necessary condition for profit maximization is

.. math::

        \frac{d\Pi(q)}{dq} = 0

Breaking up the left-hand side, the necessary condition is equivalent to

.. math::

        \frac{dTR(q)}{dq} - \frac{dTC(q)}{dq} = 0
        
Therefore, a necessary condition for a profit maximum is simply

.. math::
        
        \frac{dTR(q)}{dq} = \frac{dTC(q)}{dq} 

or 

.. math:: 

        MR(q) = MC(q)

This last little equation is quite important in microeconomics. It says that in order to maximize profits, price-taking firms equalize marginal revenue and marginal cost. And since the marginal revenue for price-taking firms is dictated by the market (it is just the market price), all firms need to do is find the output amount :math:`q` at which their marginal cost are equal to the market price.

Again, we know from earlier in the course that equating marginal revenue and marginal cost may just as well result in a profit *minimum* rather than a maximum. To be sure that we have detected a local maximum we always also need to check the second order condition. That's why we need to be careful and understand that the condition :math:`MR(q)=MC(q)` is merely a necessary condition and not a sufficient one for profit maximization.

        
        

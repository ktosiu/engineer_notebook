Statistics
==========

Expected Value
--------------

The predicted value of a variable, calculated as the sum of all possible values (:math:`x_i`) each multiplied by the probability (:math:`p_i`) of its occurrence.

.. math::  
    E(x) = x_1p_1 + x_2p_2 + ... + x_np_n 
    
    E(x) = \mu 
    
The expected value is the mean of a random variable (greek letter :math:`\mu`).

Example
~~~~~~~

You pay $2 to roll a six sided dice. If you roll a 6, you get $10. The
expected value will tell you how much money you should make in the long
run.

.. math::     E(x) = -2\frac{5}{6}+(10-2)\frac{1}{6} = -0.33333334 

So, 5 of the 6 faces is a loosing roll, so you loose $2. You have to pay
$2 to play, so your next win is only $8 if you roll a 6. Therefore you
expect to loose 33 cents in the long run if you play this game … house
always wins!

Variance
--------

Variance describes how far a set of numbers are spread out from each
other from the mean. It is the average of the *squared* differences from
the mean. It is also the covariance of :math:`x` with it self.

.. math::     var(x) = E[(x-\mu)^2] = (x_1-\mu)^2p_1 + ... + (x_n-\mu)^2p_n = cov(x,x) = E[(x-\mu)(x-\mu)] 

Variance is also one of the moments of a distribution.

Example
~~~~~~~

A perfect die has an expected value and variance of:

.. math::     E(x) = (1+2+3+4+5+6)\frac{1}{6} = 3.5 

.. math::     var(x) = [(1-3.5)^2 + (2-3.5)^2 + ... (6-3.5)^2]\frac{1}{6} = 2.9167 

*Note:* The 1/6 above is the probability assuming a fair 6 sided dice.

Covariance
----------

The measure of how two random variables change together.

.. math::     cov(x,y) = E[(x-\mu)(y-\mu)] 

For random variables which show similar behavior the sign of the cov is
positive. If the random variables act differently, then the sign is
negative. The magnitude is hard to interpret unless the cov is
normalized, called the correlation coefficient.

Standard Deviation
------------------

The standard dev is the square root of the variance.

.. math::     std = \sqrt(E[(x-\mu)^2]) 

Example
~~~~~~~

The standard dev of the above dice example is:

::

    std(x) = 1.7078  

Example: Octave
~~~~~~~~~~~~~~~

::

    x = [ 1 2 3 4 5 6 ];
    var(x,1) = 2.9167
    std(x,1) = 1.7078

*Note:* The option 1 is passed because the variance and std are taken of
the complete set of 6 (N=1). The complete set is also called the
*Population*. The default is that this is a sample of a much larger
distribution, so this is just 6 samples. When this is just a sample set,
the devisor is now N-1 (i.e., N=5 for this example) and the results are
different.

Example: Python
~~~~~~~~~~~~~~~

::

    from numpy import *
    x = array([1,2,3,4,5,6])
    std(x) = 1.7078
    var(x) = 2.9167

References
~~~~~~~~~~

1. http://www.mathsisfun.com/data/index.html
Sequences and Series
=====================

Sequence
---------

A **sequence** is an ordered list of numbers (e.g., :math:`a_n`); the numbers are called 
"elements" or "terms". Every convergent sequence is bounded, thus an unbounded sequence
is divergent.

================ =========================================================================================================================== =========
Sequence Test    Converge                                                                                                                     Notes
================ =========================================================================================================================== =========
Squeeze Theorem  :math:`\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} c_n = L` then :math:`\lim\limits_{n \to \infty} b_n = L` :math:`a_n \le b_n \le c_n`
?                :math:`\lim\limits_{n \to \infty} a_n = L`
================ =========================================================================================================================== =========

Series
------

A **series** is the sum of the terms of a sequence. Finite sequences and series have defined first and last terms, whereas infinite sequences and series continue indefinitely.


==================== ================================================ =========================================================================================================== ========================================================================================================= =================================================================================
 Series Test         Formula                                           Converge                                                                                                   Diverge                                                                                                    Notes                                                                                                                                                                                                     
==================== ================================================ =========================================================================================================== ========================================================================================================= =================================================================================  
 Divergence          :math:`\sum\limits_{n=1}^\infty a_n`               N/A                                                                                                       :math:`\lim\limits_{n\to\infty} a_n \ne 0`                                                                 Doesn't show convergence                                 
 Geometric           :math:`\sum\limits_{n=1}^\infty ar^n`             :math:`|r| < 1`                                                                                            :math:`|r| \ge 1`                                                                                          sum :math:`= \frac{a}{1-r}`                            
 P-Series            :math:`\sum\limits_{n=1}^\infty \frac{1}{n^p}`    :math:`p > 1`                                                                                              :math:`p \le 1`                                                                                    
 Alternating         :math:`\sum\limits_{n=1}^\infty (-1)^{n-1} a_n`   :math:`0 < a_{n+1} \le a_n` and :math:`\lim\limits_{n \to \infty} a_n = 0`                                  N/A                                                                                              
 Integral            :math:`\sum\limits_{n=1}^\infty a_n`              :math:`\int\limits_1^\infty f(x) dx` converges                                                             :math:`\int\limits_1^\infty f(x) dx` diverges                                                              :math:`f(x)` must be positive, decreasing, and continous                                                
 Root                :math:`\sum\limits_{n=1}^\infty a_n`              :math:`\lim\limits_{n\to\infty}\sqrt[n]{|a_n|} = L < 1`                                                    :math:`\lim\limits_{n\to\infty}\sqrt[n]{|a_n|} = L > 1`                                                    inconclusive if :math:`L = 1`                                                       
 Ratio               :math:`\sum\limits_{n=1}^\infty a_n`              :math:`\lim\limits_{n\to\infty} \left| \frac{a_{n+1}}{a_n}\right| = L < 1`                                 :math:`\lim\limits_{n\to\infty} \left| \frac{a_{n+1}}{a_n}\right| = L > 1`                                 inconclusive if :math:`L = 1`                                                                          
 Direct Comparison   :math:`\sum\limits_{n=1}^\infty a_n`              :math:`0 \le a_n \le b_n` and :math:`\sum\limits_{n=1}^{\infty} b_n` converges                             :math:`0 \le b_n \le a_n` and :math:`\sum\limits_{n=1}^{\infty} b_n` diverges                              :math:`a_n,b_n > 0`                                                                                 
 Limit Comparison    :math:`\sum\limits_{n=1}^\infty a_n`              :math:`\lim\limits_{n\to\infty} \frac{a_n}{b_n} = L` and :math:`\sum\limits_{n=1}^{\infty} b_n` converges  :math:`\lim\limits_{n\to\infty} \frac{a_n}{b_n} = L` and :math:`\sum\limits_{n=1}^{\infty} b_n` diverges   :math:`a_n,b_n > 0` and L is a positive constant                                                 
==================== ================================================ =========================================================================================================== ========================================================================================================= =================================================================================



[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Answer:

The mean weights for first babies and those born after are 7.2 lbs and 7.35 lbs, respectively. The Cophen's d is -0.089, suggesting that this difference is small. This is smaller than the difference in pregnancy length, though in a different direction. This suggests that first babies are slightly smaller than those born subsequently.

Code:

import thinkstats2
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

    
mean1 = firsts.totalwgt_lb.mean()
mean2 = others.totalwgt_lb.mean()

var1 = firsts.totalwgt_lb.var()
var2 = others.totalwgt_lb.var()

diff = mean1 - mean2

n1 = len(firsts)
n2 = len(others)

pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

d = diff / math.sqrt(pooled_var)
print d

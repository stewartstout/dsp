[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import thinkstats2
import nsfg
import math
import thinkplot

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

cdf_firsts = thinkstats2.Cdf(firsts.totalwgt_lb, label='weight')
cdf_others = thinkstats2.Cdf(others.totalwgt_lb, label='weight')
thinkplot.PrePlot(2)
thinkplot.Cdfs([cdf_firsts,cdf_others])
thinkplot.Show(xlabel='weight (pounds)', ylabel='CDF')

my_birthweight = 10

print(cdf_firsts.PercentileRank(my_birthweight))

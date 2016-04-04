[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

mport scipy
import brfss

dist = scipy.stats.norm(loc=178, scale=7.7)
print(dist.mean())
print(dist.std())
min = dist.cdf(177.8)
max = dist.cdf(185.4)

eligible = 0.0
eligible = max - min

print(eligible)

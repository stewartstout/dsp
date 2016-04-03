[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)

print('Unbiased mean: ' + str(pmf.Mean()))

new_pmf = pmf.Copy()
for x, p in pmf.Items():
    new_pmf.Mult(x, x)
        
new_pmf.Normalize()


print('Unbiased mean: ' + str(new_pmf.Mean()))

width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(pmf, align='right', width=width, label='Unbiased')
thinkplot.Hist(new_pmf, align='left', width=width, label='Biased')
thinkplot.Show(xlabel='Number of children under 18 years of age', ylabel='Frequency')

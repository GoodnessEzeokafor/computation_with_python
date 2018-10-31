'''
PyLab is a Python library that provides many of the facilities of MATLAB
    MATLAB is a high-level technical computing language and iteractive environment for 
    algorithm development, data visualization, data analysis, and numeric computations
'''
import pylab

# pylab.figure(1) # create figure 1
# pylab.plot([1,2,3,4], [1,7,3,5]) # draw on figure 1
# pylab.figure(2)
# pylab.plot([1,4,2,3], [5,6,7,8])
# pylab.savefig('Figure-Addie')
# pylab.figure(1)
# pylab.plot([5,6,10,3])
# pylab.savefig('Figure-jane')
# pylab.show()


principal = 10000 # initial investement
interestRate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate



pylab.plot(values, linewidth = 30)
pylab.title("5% Growth, Compound Anually", fontsize = 'xx-large')
pylab.xlabel("Years of Compunding", fontsize = 'x-small')
pylab.ylabel("Value of Principal ($)")
pylab.show()

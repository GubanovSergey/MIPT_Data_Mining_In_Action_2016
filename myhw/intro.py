#Python 1
for number in range(1, 101):
    printed = False
    if number % 3 == 0:
        print("Fizz", end="")
        printed = True
    if number % 5 == 0:
        print("Buzz", end="")
        printed = True
    if not printed:
        print(number)
    else:
        print()

#Python 2
fib = [0]*101
fib[1] = 1
for seq in range(2, 101):
    fib[seq] = fib [seq-2] + fib[seq-1]
print('Answer =', fib[100])

#Python 3
from random import shuffle

def quick_sort(A):
    if len(A) <= 1:
        return A
    left = [];
    middle = [A[0]];
    right = []
    for ind in range(1, len(A)):
        if A[ind] < A[0]:
            left.append(A[ind])
        elif A[ind] > A[0]:
            right.append(A[ind])
        else:
            middle.append(A[ind])

    left, right = quick_sort(left), quick_sort(right)
    return left + middle + right


A = [i for i in range(10)]
shuffle(A)
print(*A)
print(*quick_sort(A))

#NumPy

import numpy

%timeit numpy.linspace(0, 100000, 1000)

%%timeit
A = []
for num in range(1000):
    A.append(num * 100000/1000)
    
%timeit [num * 100000/1000 for num in range(1000)]

#MathPlotLib1
%matplotlib inline
from matplotlib import pylab as plot
import math

x1 = numpy.arange(-1, 5, 0.05)
y1 = [math.exp(elem) for elem in x1]
x2 = numpy.arange(-math.pi/2., 3./2*math.pi, 0.05)
y2 = [math.sin(elem) * 100/elem for elem in x2]
x3 = numpy.arange(-1.5, 5, 0.05)
y3 = x3 ** 3

plot.plot(x1, y1, label = 'exponent')
plot.plot(x2, y2, label = 'sinx * 100/x')
plot.plot(x3, y3, label = 'x ^3')
plot.legend()
plot.show()

#MathPlotLib2
%matplotlib inline
from matplotlib import pylab as plot
import math

x1 = numpy.arange(-1, 5, 0.05)
y1 = [math.exp(elem) for elem in x1]
x2 = numpy.arange(-math.pi/2., 3./2*math.pi, 0.05)
y2 = [math.sin(elem) * 100/elem for elem in x2]
x3 = numpy.arange(-1.5, 5, 0.05)
y3 = x3 ** 3

plot.subplot(121)
plot.plot(x1, y1, x2, y2, x3, y3)

plot.subplot(122)
x21 = numpy.arange(-2, 5, 0.075)
y21 = [abs(elem) ** 0.5 for elem in x21]
x22 = numpy.arange(-math.pi/2., 3./2*math.pi, math.pi/12)
y22 = [math.sin(elem/2.) for elem in x22]
plot.plot(x21, y21, x22,y22)
plot.show()

plt.savefig("graph.png")
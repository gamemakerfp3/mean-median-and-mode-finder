print("The numbers mean, median, and mode are")
import numpy
numbers = [#put your numbers here]
f = numpy.mean(numbers)
print("mean = ")   
print(f)
x = numpy.median(numbers)
print("median = ")   
print(x)
from scipy import stats
y = stats.mode(numbers)
print("mode = ")
print(y)
import numpy

import numpy as np
import matplotlib.pyplot as plt
x = []
sum = []
for i in range (0,10):
    sum.append(0)
    x.append(np.random.rand(32))
print(x)
sum = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
print (sum)
num_bins = 4
n, bins, patches = plt.hist(sum, num_bins)
plt.xlabel('sum')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
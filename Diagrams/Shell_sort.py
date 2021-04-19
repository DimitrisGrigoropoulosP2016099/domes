import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([ 0.00022450000000007186 , 0.0005269000000001078 , 0.000916300000000092 , 0.0014167000000000485 , 0.0017577000000001952 , 0.002209399999999917 , 0.0029959000000001623 , 0.0030302999999998192 , 0.003593700000000144 , 0.004214200000000279 ])
ypoints = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ,700 ,800 ,900 ,1000])

plt.plot(xpoints, ypoints)
plt.title("Shell Sort")
plt.ylabel("megethos array")
plt.xlabel("xronos")
plt.show()

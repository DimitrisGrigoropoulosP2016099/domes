import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.001664600000000016, 0.005800100000000086 , 0.010012600000000038 , 0.014853399999999795 , 0.020136799999999955 , 0.025025000000000297 , 0.02991860000000024 ,0.0349765999999998 ,0.03894719999999996 ,0.04571419999999993 ])
ypoints = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ,700 ,800 ,900 ,1000])

plt.plot(xpoints, ypoints)
plt.title("Bubble Sort")
plt.ylabel("megethos array")
plt.xlabel("xronos")
plt.show()

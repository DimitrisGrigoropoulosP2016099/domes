import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([ 0 ,0.00011359999999993597, 0.00022699999999975518,0.00038800000000005497 , 0.0005747999999998754 ,0.0007276000000002725,  0.0009361000000001063 ,0.0010401999999998246,  0.0011719000000001145,0.001259200000000238])
ypoints = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ,700 ,800 ,900 ,1000])

plt.plot(xpoints, ypoints)
plt.title("Quick Sort")
plt.ylabel("megethos array")
plt.xlabel("xronos")
plt.show()

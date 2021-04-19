import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.0006540999999999908,  0.0029007999999999257 , 0.006147099999999739 ,0.01141269999999972, 0.01908120000000002 ,0.026047199999999826, 0.03856919999999997,0.04487419999999975, 0.0572547000000001, 0.0782307999999996 ])
ypoints = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ,700 ,800 ,900 ,1000])

plt.plot(xpoints, ypoints)
plt.title("Insertion Sort")
plt.ylabel("megethos array")
plt.xlabel("xronos")
plt.show()

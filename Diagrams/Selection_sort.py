import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([ 0.0008715000000001361 , 0.003627599999999731,0.00828350000000011, 0.014193999999999818,0.02261409999999975, 0.03262690000000035 ,0.04539930000000014,0.05918689999999982,0.07535630000000015 ,0.08869759999999971 ])
ypoints = np.array([ 100 , 200 , 300 , 400 , 500 , 600 ,700 ,800 ,900 ,1000])

plt.plot(xpoints, ypoints)
plt.title("Selection Sort")
plt.ylabel("megethos array")
plt.xlabel("xronos")
plt.show()

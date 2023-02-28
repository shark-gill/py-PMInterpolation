# 3D Point Visualization
#%%
from mpl_toolkits.mplot3d.axes3d import *
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter3D(x,y,z,c=z,cmap=plt.cm.jet)  
plt.show()

# 출처
# https://gis.stackexchange.com/questions/66367/display-a-georeferenced-dem-surface-in-3d-matplotlib

#
# %%

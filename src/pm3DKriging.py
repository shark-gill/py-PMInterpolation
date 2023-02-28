#%%
## 00_Package Import 
from pykrige.ok3d import OrdinaryKriging3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gstools as gs

absPath = "/home/lhshrk/py-PMInter/"
relPath = "data/pm_rawdata.csv"

df = pd.read_csv(absPath + relPath)

df.head()

print("PM10 value scope:", df['pm10'].shape)
print("PM2.5 value scope:", df['pm2.5'].shape)


print("Nmin:", df['N'].min(), "Nmax:", df['N'].max(),
      "Emin:", df['E'].min(), "Emax:", df['E'].max(),
      "Zmin:", df['z'].min(), "Zmax:", df['z'].max())

print("PM10 variance:", round(df['pm10'].var(), 2) )
print("PM2.5 variance:", round(df['pm2.5'].var(), 2) )

## 
#%%
## 01_Value ndarray Conversion
x = np.array(df['N'])
y = np.array(df['E'])
z = np.array(df['z'])
pm10 = np.array(df['pm10'])
pm25 = np.array(df['pm2.5'])



#%%
#

#%%
## 02_Variogram
pm10ok3d = OrdinaryKriging3D(x, y, z, pm10, variogram_model='spherical',
                             nlags=10, enable_plotting=True, verbose=True)
pm25ok3d = OrdinaryKriging3D(x, y, z, pm25, variogram_model='spherical',
                             nlags=10, enable_plotting=True, verbose=True)

# drift_terms=["specified"], specified_drift=df[df['N'], df['E'], df['z']],

#%%
## 03_Grid set
gridx = np.linspace(1932475, 1934146, num=30, endpoint=False)
gridy = np.linspace(948407, 949596, num=30, endpoint=False)
gridz = np.linspace(0, 150, num=15, endpoint=False)

zg, yg, xg = np.meshgrid(gridz, gridy, gridx, indexing='ij')

#%%
## 04_2D Grid Visualization

fig = plt.figure(figsize=(10, 6))
plot1 = fig.add_subplot(111)
a = plt.scatter(xg, yg)
plt.xlabel("N Coord [m]")
plt.ylabel("E Coord [m]")
plt.title("Grid 2D")
plt.grid(True)

#%%
## 06_3D Kriging Model
k3d1, ss3d = pm10ok3d.execute('grid', gridx, gridy, gridz)
k3d2, ss3d = pm25ok3d.execute('grid', gridx, gridy, gridz)


#%%
## 05_3D Grid Visualization
fig3d = plt.figure(figsize=(10, 10))
plot3d = fig3d.add_subplot(111, projection='3d')
plot3d.scatter(xg, yg, zg, c=k3d2)
plot3d.set_xlabel("N Coord [m]")
plot3d.set_ylabel("E Coord [m]")
plot3d.set_zlabel("Z Coord [m]")
plt.show()

#%%

print(len(k3d2))

#%%
# fig4d = plt.figure()
# plot4d = fig3d.add_subplot(111, projection='3d')
# plot4d.imshow(k3d1[:, :, :], origin="lower")
# plt.show()


#%%
# UTM-K
# 단위 m
# %%

#%%
# https://www.youtube.com/watch?v=pFCqt0M14bs
# https://mathematica.stackexchange.com/questions/268402/build-a-3d-heat-map-plot-from-4d-data
# https://stackoverflow.com/questions/48052969/python-2-3d-scatter-plot-with-surface-plot-from-that-data
# https://banesullivan.com/pyvista/examples/voxelize.html
# https://docs.pyvista.org/examples/00-load/create-uniform-grid.html
# DEM ;; https://gis.stackexchange.com/questions/66367/display-a-georeferenced-dem-surface-in-3d-matplotlib
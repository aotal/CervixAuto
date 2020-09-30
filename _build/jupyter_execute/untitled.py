# La mare del tano

import trimesh
import numpy as np
import matplotlib.pyplot as plt
#from shapely.geometry import Polygon
from matplotlib.path import Path

ImagenEntrada=trimesh.load('OV.stl')
ImagenEntrada.show()

```{note}
Here is a note
```

A=trimesh.Scene(ImagenEntrada)

A.show()

A.add_geometry()

# get a single cross section of the mesh
slice = ImagenEntrada.section(plane_origin=np.array([5,-10,0]), plane_normal=[1,0,0])

# the section will be in the original mesh frame
slice.show()

# get a single cross section of the mesh
slice = ImagenEntrada.section(plane_origin=np.array([5,-10,0]), plane_normal=[1,0,0])

slice_2D, to_3D = slice.to_planar()

slice_2D.show()

Ext=slice_2D.polygons_closed[0]
Int=slice_2D.polygons_closed[1:]

poly_path_ext=Path((np.array(Ext.exterior.coords.xy)/0.3125).T.astype(np.int32)+256)
poly_path_int=[Path((np.array(X.exterior.coords.xy)/0.3125).T.astype(np.int32)+256) for X in Int]

def CreateMask(path,height,width):
    x, y = np.mgrid[:height, :width]
    coors=np.hstack((x.reshape(-1, 1), y.reshape(-1,1)))
    return np.flip(path.contains_points(coors).reshape(height, width).T,axis=0)

mask1=CreateMask(poly_path_ext,512,512)
mask2=np.array([CreateMask(X,512,512) for X in poly_path_int]).sum(axis=0)

plt.imshow(mask1 & np.logical_not(mask2),cmap='gray')


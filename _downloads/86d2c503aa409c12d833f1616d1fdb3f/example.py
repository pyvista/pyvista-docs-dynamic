"""
Example
-------

This a simple example.


"""
import pyvista as pv
from pyvista import examples

pl = pv.Plotter()
pl.add_mesh(pv.Wavelet().contour())
pl.show()

###############################################################################
mesh = examples.load_random_hills()
cntrs, edges = mesh.contour_banded(7)

pl = pv.Plotter()
pl.add_mesh(cntrs, scalars='Scalars')
pl.add_mesh(edges, line_width=5)
pl.show()

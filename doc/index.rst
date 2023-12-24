Dynamic PyVista Examples
========================

This is a demostration of PyVista's dynamic Sphinx-Gallery scraper implemented
in https://github.com/pyvista/pyvista/pull/4569/

The dynamic in-browser renderings are made possible by PyVista's ``pyvista-plot``
directive:

.. code-block:: rst

    .. pyvista-plot::

        import pyvista as pv
        mesh = pv.Wavelet()
        mesh.plot()

.. pyvista-plot::

    import pyvista as pv
    mesh = pv.Wavelet()
    mesh.plot()


.. include:: examples/index.rst

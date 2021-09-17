# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""Test function :func:`iris.util.find_discontiguities"""

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests  # isort:skip

import numpy as np

from iris.tests.stock import (
    make_bounds_discontiguous_at_point,
    sample_2d_latlons,
    simple_3d,
)
from iris.util import find_discontiguities


def full2d_global():
    return sample_2d_latlons(transformed=True)


@tests.skip_data
class Test(tests.IrisTest):
    def setUp(self):
        # Set up a 2d lat-lon cube with 2d coordinates that have been
        # transformed so they are not in a regular lat-lon grid.
        # Then generate a discontiguity at a single lat-lon point.
        self.testcube_discontig = full2d_global()
        make_bounds_discontiguous_at_point(self.testcube_discontig, 3, 3)
        # Repeat that for a discontiguity in the grid 'Y' direction.
        self.testcube_discontig_along_y = full2d_global()
        make_bounds_discontiguous_at_point(
            self.testcube_discontig_along_y, 2, 4, in_y=True
        )

    def test_find_discontiguities(self):
        # Check that the mask we generate when making the discontiguity
        # matches that generated by find_discontiguities
        cube = self.testcube_discontig
        expected = cube.data.mask
        returned = find_discontiguities(cube)
        self.assertTrue(np.all(expected == returned))

    def test_find_discontiguities_in_y(self):
        # Check that the mask we generate when making the discontiguity
        # matches that generated by find_discontiguities
        cube = self.testcube_discontig_along_y
        expected = cube.data.mask
        returned = find_discontiguities(cube)
        self.assertTrue(np.all(expected == returned))

    def test_find_discontiguities_1d_coord(self):
        # Check that an error is raised when we try and use
        # find_discontiguities on 1D coordinates:
        cube = simple_3d()
        with self.assertRaises(NotImplementedError):
            find_discontiguities(cube)

    def test_find_discontiguities_with_atol(self):
        cube = self.testcube_discontig
        # Choose a very large absolute tolerance which will result in fine
        # discontiguities being disregarded
        atol = 100
        # Construct an array the size of the points array filled with 'False'
        # to represent a mask showing no discontiguities
        expected = np.zeros(cube.shape, dtype=bool)
        returned = find_discontiguities(cube, abs_tol=atol)
        self.assertTrue(np.all(expected == returned))

    def test_find_discontiguities_with_rtol(self):
        cube = self.testcube_discontig
        # Choose a very large relative tolerance which will result in fine
        # discontiguities being disregarded
        rtol = 1000
        # Construct an array the size of the points array filled with 'False'
        # to represent a mask showing no discontiguities
        expected = np.zeros(cube.shape, dtype=bool)
        returned = find_discontiguities(cube, rel_tol=rtol)
        self.assertTrue(np.all(expected == returned))


if __name__ == "__main__":
    tests.main()

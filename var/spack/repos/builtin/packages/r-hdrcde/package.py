# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class RHdrcde(RPackage):
    """Computation of highest density regions in one and two
    dimensions, kernel estimation of univariate density functions
    conditional on one covariate,and multimodal regression."""

    cran = 'hdrcde'

    version('3.4', sha256='4341c6a021da46dcae3b1ef6d580e84dcf625c2b2139f537d0c26ec90899149b')

    depends_on('r@2.15:', type=('build', 'run'))
    depends_on('r-locfit', type=('build', 'run'))
    depends_on('r-ash', type=('build', 'run'))
    depends_on('r-ks', type=('build', 'run'))
    depends_on('r-kernsmooth', type=('build', 'run'))
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-rcolorbrewer', type=('build', 'run'))

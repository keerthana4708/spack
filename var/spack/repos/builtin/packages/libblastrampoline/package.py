# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libblastrampoline(MakefilePackage):
    """Using PLT trampolines to provide a BLAS and LAPACK demuxing library."""

    homepage = "https://github.com/JuliaLinearAlgebra/libblastrampoline"
    git      = "https://github.com/JuliaLinearAlgebra/libblastrampoline.git"
    url      = "https://github.com/JuliaLinearAlgebra/libblastrampoline/archive/refs/tags/v3.1.0.tar.gz"

    maintainers = ['haampie']

    version('3.1.0', sha256='f6136cc2b5d090ceca67cffa55b4c8af4bcee874333d49297c867abdb0749b5f')
    version('3.0.4', sha256='3c8a54a3bd8a2737b7f74ebeb56df8e2a48083c9094dbbff80b225c228e31793')
    version('3.0.3', sha256='a9c553ee6f20fa2f92098edcb3fc4a331c653250e559f72b9317b4ee84500cd7')
    version('3.0.2', sha256='caefd708cf0cf53b01cea74a09ab763bf4dfa4aec4468892720f3921521c1f74')
    version('3.0.1', sha256='b5b8ac0d3aba1bcb9dc26d7d6bb36b352d45e7d7e2594c6122e72b9e5d75a772')
    version('3.0.0', sha256='4d0856d30e7ba0cb0de08b08b60fd34879ce98714341124acf87e587d1bbbcde')
    version('2.2.0', sha256='1fb8752891578b45e187019c67fccbaafb108756aadc69bdd876033846ad30d3')

    build_directory = 'src'

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make('prefix={0}'.format(prefix), 'install')

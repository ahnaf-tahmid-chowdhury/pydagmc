#!/usr/bin/env python
import os
import sys
from skbuild import setup

# Check for Windows
IS_NT = os.name == "nt"

# Check for Mac
IS_MAC = sys.platform == "darwin"

# Cmake args
cmake_args = [
    "-DCMAKE_BUILD_TYPE:STRING=Release",
]

# Specify GCC as the compiler for Windows
if IS_NT:
    cmake_args.append("-Visual Studio 17 2022") # MinGW Makefiles Unix Makefiles
    cmake_args.append("-DBUILD_EXE:BOOL=ON")
    cmake_args.append("-DBUILD_STATIC_EXE:BOOL=ON")
    cmake_args.append("-DBUILD_STATIC_LIBS:BOOL=ON")
    cmake_args.append("-DBUILD_UWUW:BOOL=ON")
    cmake_args.append("-DBUILD_MAKE_WATERTIGHT:BOOL=ON")
    cmake_args.append("-DBUILD_OVERLAP_CHECK:BOOL=OFF")
    cmake_args.append("-DBUILD_TESTS:BOOL=OFF")
    
# Specify gfortran-12 as the Fortran compiler for Mac
if IS_MAC:
    cmake_args.append("-DBUILD_SHARED_LIBS:BOOL=ON")
    cmake_args.append("-DCMAKE_CXX_FLAGS:STRING='-Werror=reorder'")

# Check for MOAB_ROOT
if "MOAB_ROOT" in os.environ:
    cmake_args.append("-DMOAB_DIR:FILEPATH=" + os.environ["MOAB_ROOT"])

# Collect extension
extension = ["*.dll", "*.so", "*.dylib", "*.pyd", "*.pyo"]

# Setup configuration
setup(
    packages=[
        "dagmc",
    ],
    package_data={
        "lib": extension,
    },
    cmake_args=cmake_args,
    cmake_source_dir='vendor/DAGMC',
    cmake_install_dir=".",
)

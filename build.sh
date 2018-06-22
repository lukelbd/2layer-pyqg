#!/usr/bin/env bash

#------------------------------------------------------------------------------#
# Build with setup command (overkill)
# Tried to get around this, because it creates stupid useless 'build' directory, but
# some stuff I don't understand
# Use python setup.py build_ext --help to see options
python setup.py build_ext --build-lib=pyqg/lib --build-temp=pyqg/tmp --inplace
exit

#------------------------------------------------------------------------------#
# Custom setup
# Test if openMPI present
echo "Checking for openMPI."
sleep 1
cat >test.c <<EOF
#include <omp.h>
#include <stdio.h>
int main() {
#pragma omp parallel
printf("Hello from thread %d, nthreads %d\n", omp_get_thread_num(), omp_get_num_threads());
}
EOF
gcc -fopenmp test.c
mpi_avail=$? # check for zero exit code
rm test.c

# Compile cython code
echo "Compiling cython."
sleep 1
python <<EOF
from setuptools import Extension
from Cython.Build import cythonize
import warnings
extra_compile_args = []
extra_link_args = []
if not $mpi_avail:
    extra_compile_args.append('-fopenmp')
    extra_link_args.append('-fopenmp')
else:
    warnings.warn('Could not link with openmp. Model will be slow.')
ext_module = cythonize(Extension(
    "pyqg_mod.kernel",
    ["pyqg_mod/kernel.pyx"],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args))
EOF
# This creates a file named a.out
mv a.out pyqg_mod/kernel.o

# Compile C code
echo "Compiling c file."
sleep 1
gcc -pthread -shared -L/project2/rossby/group07/.conda/lib \
  -Wl,-rpath=/project2/rossby/group07/.conda/lib,--no-as-needed pyqg_mod/kernel.o \
  -L/project2/rossby/group07/.conda/lib \
  -lpython2.7 -o pyqg_mod/kernel.so \
  -fopenmp

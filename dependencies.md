## Python packages

Note that some of these may exist in the Alpine official repo, for python 2 and/or 3, depending which branch you're looking at.  Build in this order:

| Package    | Dependencies |
|------------|--------------|
| cycler     | -            |
| nose       | -            |
| cython     | -            |
| numpy      | nose, cython |
| matplotlib | numpy, cycler|
| pandas     | numpy        |
| scipy      | numpy        |

## Octave packages

| Package             | Dependencies     |
|---------------------|------------------|
| arpack              | -                |
| texlive             | -                |
| gl2ps               | texlive          |
| glpk                | -                |
| gnu-units           | -                |
| hdf5                | -                |
| libtbb              | -                |
| nlopt               | -                |
| qhull               | -                |
| qrupdate            | -                |
| qscintilla          | -                |
| suitesparse         | libtbb           |
| octave-nbgallery    | everything above |
| octave-nbgallery-*  | octave-nbgallery |

## Everything else

| Package                | Dependencies     |
|------------------------|------------------|
| gdal                   | -                |
| geos                   | -                |
| libpst                 | -                |
| libspatialindex        | -                |
| proj4                  | -                |
| ssdeep                 | -                |
| hadoop                 | -                |
| pig                    | hadoop           |
| gallery-pig-kernel     | pig, hadoop      |
| gallery-go-kernel      | -                |
| gallery-nodejs-kernel  | -                |
| gallery-python3-kernel | -                |
| gallery-R-kernel       | -                |
| gallery-ruby-kernel    | -                |
| gallery-toree-kernel   | -                |
| cling                  | good luck!       |
| gallery-cpp-kernel     | cling            |

## Python packages

Note that some of these may exist in the Alpine official repo, for python 2 and/or 3, depending which branch you're looking at.  Build in this order:

| Package       | Dependencies            | Alpine 3.8 status                        |
|---------------|-------------------------|------------------------------------------|
| cycler        | -                       | 0.10.0 copied frome edge                 |
| cython        | -                       | 0.28.2 official for py2; nbg for py3     |
| kiwisolver    | -                       | 1.0.1 copied from edge                   |
| backports lru | -                       | 1.5 copied from edge                     |
| matplotlib    | cycler, backports, kiwi | 2.2.3 copied from edge                   |
| pandas        | numpy, cython           | 0.23.4 built by nbgallery                |
| ~~scipy~~     | numpy, cython           | 1.0.1 now in official repo               |

## Octave packages

Note: in the Alpine 3.7 official repo, `lapack-dev` and `openblas-dev` conflict -- they contain some of the same header files and cannot be installed at the same time.  The `qrupdate` package will build if `lapack-dev` is moved to `makedepends` but that may cause a problem at runtime.  The `nan` toolkit also requires `lapack-dev` (specifically `-lblas`), but also depends on `openblas-dev` via `octave-nbgallery-dev`, so I've removed that from the toolkits metapackage for now.

| Package                              | Dependencies      | Alpine 3.7 status          |
|--------------------------------------|-------------------|----------------------------|
| ~~arpack~~                           | -                 | 3.5.0 now in official repo |
| texlive                              | -                 | 20170524 (from edge)       |
| gl2ps                                | texlive           | 1.4.0 (by nbgallery)       |
| glpk                                 | -                 | 4.64 (by nbgallery)        |
| gnu-units                            | -                 | 2.16 (by nbgallery)        |
| hdf5                                 | -                 | 1.8.20 (from edge)         |
| libtbb                               | -                 | 4.4.4 (from edge)          |
| nlopt                                | -                 | 2.4.2 (by nbgallery)       |
| qhull                                | -                 | 7.2.0 (by nbgallery)       |
| qrupdate                             | -                 | 1.1.2 (by nbgallery)       |
| qscintilla                           | -                 | 2.10.2 (by nbgallery)      |
| ~~suitesparse~~                      | libtbb            | 4.5.6 now in official repo |
| octave-nbgallery                     | everything above  | 4.2.1 (by nbgallery)       |
| octave-nbgallery-communications      | octave-nbg        | 1.2.1                      |
| octave-nbgallery-data-smoothing      | octave-nbg        | 1.3.0                      |
| octave-nbgallery-fuzzy-logic-toolkit | octave-nbg        | 0.4.5                      |
| octave-nbgallery-general             | octave-nbg        | 2.0.0                      |
| octave-nbgallery-gsl                 | octave-nbg        | 2.1.0                      |
| octave-nbgallery-image               | octave-nbg        | 2.6.2                      |
| octave-nbgallery-linear-algebra      | octave-nbg        | 2.2.2                      |
| octave-nbgallery-ltfat               | octave-nbg        | 2.2.0                      |
| octave-nbgallery-miscellaneous       | octave-nbg, units | 1.2.1                      |
| octave-nbgallery-mvn                 | octave-nbg        | 1.1.0                      |
| ~~octave-nbgallery-nan~~             | octave-nbg        | broken, see note above     |
| octave-nbgallery-signal              | octave-nbg        | 1.3.2                      |
| octave-nbgallery-splines             | octave-nbg        | 1.3.2                      |
| octave-nbgallery-statistics          | octave-nbg        | 1.3.0                      |
| octave-nbgallery-strings             | octave-nbg        | 1.2.0                      |
| octave-nbgallery-struct              | octave-nbg        | 1.0.14                     |
| octave-nbgallery-tsa                 | octave-nbg        | 4.4.5                      |
| octave-nbgallery-toolkits            | everything above  | 4.2.1                      |


## Everything else

| Package                    | Dependencies     | Alpine 3.7 status       |
|----------------------------|------------------|-------------------------|
| gdal                       | -                | 2.2.3 (from edge)       |
| geos                       | -                | 3.6.2 (from edge)       |
| libpst                     | -                | 0.6.71 (by nbgallery)   |
| libspatialindex            | -                | 1.8.5 (by nbgallery)    |
| proj4                      | -                | 4.9.3 (from edge)       |
| ssdeep                     | -                | 2.14.1 (by nbgallery)   |
| hadoop                     | -                | 2.6.5 (by nbgallery)    |
| pig                        | hadoop           | 0.16.0 (by nbgallery)   |
| gallery-pig-kernel         | pig, hadoop      | built                   |
| gallery-go-kernel          | -                | built                   |
| gallery-nodejs-kernel      | -                | built                   |
| ~~gallery-python3-kernel~~ | -                | now baked into image    |
| gallery-R-kernel           | -                | built                   |
| gallery-ruby-kernel        | -                | built                   |
| gallery-toree-kernel       | -                | built                   |
| cling                      | good luck!       | not attempted yet       |
| gallery-cpp-kernel         | cling            | not attempted yet       |

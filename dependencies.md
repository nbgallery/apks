## Python packages

Note that some of these may exist in the Alpine official repo, for python 2 and/or 3, depending which branch you're looking at.  Build in this order:

| Package    | Dependencies  | Alpine 3.7 status                        |
|------------|---------------|------------------------------------------|
| cycler     | -             | 0.10.0 built by nbgallery                |
| ~~nose~~   | -             | 1.3.7 now in official repo               |
| cython     | -             | 0.27.2 official for py2; nbg for py3     |
| ~~numpy~~  | nose, cython  | 1.13.3 now in official repo              |
| matplotlib | numpy, cycler | 2.1.1 built by nbgallery                 |
| pandas     | numpy, cython | 0.22.0 built by nbgallery                |
| scipy      | numpy, cython | 1.0.0 built by nbgallery                 |

## Octave packages

| Package                              | Dependencies      | Alpine 3.7 status |
|--------------------------------------|-------------------|-------------------|
| arpack                               | -                 |                   |
| texlive                              | -                 |                   |
| gl2ps                                | texlive           |                   |
| glpk                                 | -                 |                   |
| gnu-units                            | -                 |                   |
| hdf5                                 | -                 |                   |
| libtbb                               | -                 |                   |
| nlopt                                | -                 |                   |
| qhull                                | -                 |                   |
| qrupdate                             | -                 |                   |
| qscintilla                           | -                 |                   |
| suitesparse                          | libtbb            |                   |
| octave-nbgallery                     | everything above  |                   |
| octave-nbgallery-communications      | octave-nbg        |                   |
| octave-nbgallery-data-smoothing      | octave-nbg        |                   |
| octave-nbgallery-fuzzy-logic-toolkit | octave-nbg        |                   |
| octave-nbgallery-general             | octave-nbg        |                   |
| octave-nbgallery-gsl                 | octave-nbg        |                   |
| octave-nbgallery-image               | octave-nbg        |                   |
| octave-nbgallery-linear-algebra      | octave-nbg        |                   |
| octave-nbgallery-ltfat               | octave-nbg        |                   |
| octave-nbgallery-miscellaneous       | octave-nbg, units |                   |
| octave-nbgallery-mvn                 | octave-nbg        |                   |
| octave-nbgallery-nan                 | octave-nbg        |                   |
| octave-nbgallery-signal              | octave-nbg        |                   |
| octave-nbgallery-splines             | octave-nbg        |                   |
| octave-nbgallery-statistics          | octave-nbg        |                   |
| octave-nbgallery-strings             | octave-nbg        |                   |
| octave-nbgallery-struct              | octave-nbg        |                   |
| octave-nbgallery-toolkits            | octave-nbg        |                   |
| octave-nbgallery-tsa                 | octave-nbg        |                   |


## Everything else

| Package                | Dependencies     | Alpine 3.7 status |
|------------------------|------------------|-------------------|
| gdal                   | -                |                   |
| geos                   | -                |                   |
| libpst                 | -                |                   |
| libspatialindex        | -                |                   |
| proj4                  | -                |                   |
| ssdeep                 | -                |                   |
| hadoop                 | -                |                   |
| pig                    | hadoop           |                   |
| gallery-pig-kernel     | pig, hadoop      |                   |
| gallery-go-kernel      | -                |                   |
| gallery-nodejs-kernel  | -                | built             |
| gallery-python3-kernel | -                |                   |
| gallery-R-kernel       | -                |                   |
| gallery-ruby-kernel    | -                | built             |
| gallery-toree-kernel   | -                |                   |
| cling                  | good luck!       |                   |
| gallery-cpp-kernel     | cling            |                   |

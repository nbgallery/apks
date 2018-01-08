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
| octave-nbgallery                     | everything above  |                            |
| octave-nbgallery-communications      | octave-nbg        |                            |
| octave-nbgallery-data-smoothing      | octave-nbg        |                            |
| octave-nbgallery-fuzzy-logic-toolkit | octave-nbg        |                            |
| octave-nbgallery-general             | octave-nbg        |                            |
| octave-nbgallery-gsl                 | octave-nbg        |                            |
| octave-nbgallery-image               | octave-nbg        |                            |
| octave-nbgallery-linear-algebra      | octave-nbg        |                            |
| octave-nbgallery-ltfat               | octave-nbg        |                            |
| octave-nbgallery-miscellaneous       | octave-nbg, units |                            |
| octave-nbgallery-mvn                 | octave-nbg        |                            |
| octave-nbgallery-nan                 | octave-nbg        |                            |
| octave-nbgallery-signal              | octave-nbg        |                            |
| octave-nbgallery-splines             | octave-nbg        |                            |
| octave-nbgallery-statistics          | octave-nbg        |                            |
| octave-nbgallery-strings             | octave-nbg        |                            |
| octave-nbgallery-struct              | octave-nbg        |                            |
| octave-nbgallery-tsa                 | octave-nbg        |                            |
| octave-nbgallery-toolkits            | everything above  |                            |


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
| gallery-go-kernel          | -                |                         |
| gallery-nodejs-kernel      | -                | built                   |
| ~~gallery-python3-kernel~~ | -                | now baked into image    |
| gallery-R-kernel           | -                | built                   |
| gallery-ruby-kernel        | -                | built                   |
| gallery-toree-kernel       | -                | built                   |
| cling                      | good luck!       |                         |
| gallery-cpp-kernel         | cling            |                         |

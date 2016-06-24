# Building jg-ipython3

Some users might get an error like this one when trying to build:

> error in ipython setup command: Invalid environment marker: sys_platform == "darwin" and platform_python_implementation == "CPython"

This is a bug in pip/setuptools bundled in the python3 apk. To work around it, install the jg-ipython3 dependecies on your apk build box, then upgrade pip/setuptools with the following command:

```bash
$ pip install --upgrade setuptools pip
```

Then build using `abuild`, instead of `abuild -r`.

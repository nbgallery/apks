# nb.gallery APKs 

These APKs are used by the nb.gallery Docker client to dynamically install kernels. 

## apkbuilder docker image

[This image](https://hub.docker.com/r/nbgallery/apkbuilder/) can be used to build the apks in this project.  By default it will use a signing key from this directory and will mount source and package directories located here.  The image is similar to [alpine-jazz-hands](https://github.com/madedotcom/alpine-jazz-hands) but customized for the nbgallery project.

1. If needed, run `sudo ./build-image` to build the `nbgallery/apkbuilder` image.  Or just [pull it](https://hub.docker.com/r/nbgallery/apkbuilder/).
2. Copy the signing key to this directory.  The `build` script will pick it up automatically, or use the -k option.
3. Run `sudo ./build <subdir>` to build the apk from the specified subdir.  If you're running from this directory, the source and package directories should get set automatically.

## Serving APKs from within the [jupyter-alpine](https://github.com/nbgallery/jupyter-docker) image

If you don't have a web server to host the apks, you can mount them into the jupyter-alpine docker image.  If the apks live locally at `packages/apks/x86_64/*.apk`, then run the image something like this:

```
docker run -ti -p 80:80 -v `pwd`/packages:/root/.jupyter/static nbgallery/jupyter-alpine bash
```

The directory `/root/.jupyter/static` is already configured as an extra static file path for the Jupyter web server.

Once you're inside the container, add the line `http://localhost/Jupyter/static/apks` to `/etc/apk/repositories`.  Then run `jupyter notebook`, and the dynamic kernel installation should now work.

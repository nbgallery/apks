# nb.gallery APKs 

These APKs are used by the [nbgallery Jupyter Docker client](https://github.com/nbgallery/jupyter-docker) to dynamically install kernels. 

## apkbuilder docker image

[This image](https://hub.docker.com/r/nbgallery/apkbuilder/) can be used to build the apks in this project.  By default it will use a signing key from this directory and will mount source and package directories located here.  The image is similar to [alpine-jazz-hands](https://github.com/madedotcom/alpine-jazz-hands) but customized for the nbgallery project.

1. git clone https://github.com/nbgallery/apks
2. cd apks
3. If needed, run `sudo ./build-image <branch>` to build the `nbgallery/apkbuilder:<branch>` image.  Currently supported branches are `edge` and `3.5`.  Or just [pull the image](https://hub.docker.com/r/nbgallery/apkbuilder/) you need.
4. Copy the signing key to the current directory -- both public and private keys are required.  The `build` script will pick them up automatically, or use the -k option to specify the private key (public key is assumed to be `<private-key-filename>.pub`.
5. Run `sudo ./build <branch> <subdir>` to build the apk from the specified subdir.  If you're running from the `apks` top-level directory, the source and package directories should get set automatically.  If branch is `edge`, apks and index will be written to the `packages` subdirectory; otherwise they will be written to `packages-<branch>`.

## Serving APKs from within the [jupyter-alpine](https://github.com/nbgallery/jupyter-docker) image

If you don't have a web server to host the apks, you can mount them into the jupyter-alpine docker image.  If the apks live locally at `packages/apks/x86_64/*.apk`, then run the image something like this:

```
docker run -it -p 443:443 -v `pwd`/packages:/root/.jupyter/static nbgallery/jupyter-alpine bash
```

The directory `/root/.jupyter/static` is already configured as an extra static file path for the Jupyter web server.

Once you're inside the container, add the line `http://localhost/Jupyter/static/apks` to `/etc/apk/repositories`.  Then run `jupyter-notebook-secure`, and the dynamic kernel installation should now work.

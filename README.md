# nb.gallery APKs 

These APKs are used by the [nbgallery Jupyter Docker client](https://github.com/nbgallery/jupyter-docker) to dynamically install kernels. 

## Background reading and helpful links

 * [Alpine Linux package management](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)
 * [Building Alpine packages](http://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package)
 * [Alpine Linux package search](https://pkgs.alpinelinux.org/packages)
 
## apkbuilder docker image

[This image](https://hub.docker.com/r/nbgallery/apkbuilder/) can be used to build the apks in this project.  By default it will use a signing key from this directory and will mount source and package directories located here.  The image is similar to [alpine-jazz-hands](https://github.com/madedotcom/alpine-jazz-hands) but customized for the nbgallery project.

1. git clone https://github.com/nbgallery/apks
2. cd apks
3. If needed, run `sudo ./build-image <branch>` to build the `nbgallery/apkbuilder:<branch>` image.  Or just [pull the image](https://hub.docker.com/r/nbgallery/apkbuilder/) you need.
4. Copy the signing key to the current directory -- both public and private keys are required.  The `build` script will pick them up automatically, or use the -k option to specify the private key (public key is assumed to be `<private-key-filename>.pub`.
    * If you don't have a signing key, you can run the apkbuilder image in debug: `sudo ./build <branch> debug`.  Then run `abuild-keygen` to generate a key.  Inside the container, `/home/nbgallery/apks` is mounted from the current directory, so copy the resulting key files into there to get them out of the container.
5. Run `sudo ./build <branch> <subdir>` to build the apk from the specified subdir.  If you're running from the `apks` top-level directory, the source and package directories should get set automatically.  By default, packages will will be written to the `packages-<branch>` subdirectory.
6. Check the build output as well as the size of the resulting apk file.  Failures are not always obvious.

### Workflow for new Alpine releases

All packages must be rebuilt for new Alpine releases.  Here is our general workflow for that:

1. For each package, in [dependency order](dependencies.md):
   1. Check [Alpine package search](https://pkgs.alpinelinux.org/packages) to see if it's now an official package.  If yes, delete the package from our repo.  If no, continue with the rest of these steps.
   2. Check the package's home page to see if there's a new version.  Update the APKBUILD file appropriately.  If there is not a new version, we usually bump the build number in the APKBUILD file.
   3. Build the APK using the apkbuilder build script: `sudo ./build <branch> <subdir>`
      * This step automatically updates the APKINDEX - it's usually easier to have one person build the "master" copy of the repo instead of trying to have everyone keep in sync.
    
## Serving APKs from within the [jupyter-alpine](https://github.com/nbgallery/jupyter-docker) image

If you don't have a web server to host the apks, you can mount them into the jupyter-alpine docker image.  If the apks live locally at `packages/apks/x86_64/*.apk`, then run the image something like this:

```
docker run -it -p 443:443 -v `pwd`/packages:/root/.jupyter/static nbgallery/jupyter-alpine bash
```

The directory `/root/.jupyter/static` is already configured as an extra static file path for the Jupyter web server.

Once you're inside the container, add the line `https://localhost/Jupyter/static/apks` to `/etc/apk/repositories`.  Then run `jupyter-notebook-secure`, and the dynamic kernel installation should now work.

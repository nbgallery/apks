# nb.gallery APKs 

These APKs are used by the [nbgallery Jupyter Docker client](https://github.com/nbgallery/jupyter-docker) to dynamically install kernels. 

## Background reading and helpful links

 * [Alpine Linux package management](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)
 * [Building Alpine packages](http://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package)
 * [APKBUILD reference](https://wiki.alpinelinux.org/wiki/APKBUILD_Reference)
 * [APKBUILD examples](https://wiki.alpinelinux.org/wiki/APKBUILD_examples)
 * [Alpine Linux package search](https://pkgs.alpinelinux.org/packages)
 
## apkbuilder docker image

[This image](https://hub.docker.com/r/nbgallery/apkbuilder/) can be used to build the apks in this project.  By default it will use a signing key from this directory and will mount source and package directories located here.  The image is similar to [alpine-jazz-hands](https://github.com/madedotcom/alpine-jazz-hands) but customized for the nbgallery project.

1. git clone https://github.com/nbgallery/apks
2. cd apks
3. If needed, run `sudo ./build-image <branch>` to build the `nbgallery/apkbuilder:<branch>` image.  Or just [pull the image](https://hub.docker.com/r/nbgallery/apkbuilder/) you need.
4. Copy the signing key to the current directory -- both public and private keys are required.  The `build` script will pick them up automatically, or use the -k option to specify the private key (public key is assumed to be `<private-key-filename>.pub`.
   * If you don't have a signing key already, you can run the apkbuilder image in debug: `sudo ./build <branch> debug`.  Then run `abuild-keygen` to generate a key and specify an output file like `/home/nbgallery/apks/somekey.rsa`.  Inside the container, `/home/nbgallery/apks` is mounted from the current directory, so the key files will be there after the container exits.
5. Run `sudo ./build <branch> <subdir>` to build the apk from the specified subdir.  If you're running from the `apks` top-level directory, the source and package directories should get set automatically.  By default, packages will will be written to the `packages-<branch>` subdirectory.
6. Check the build output as well as the size of the resulting apk file.  Failures are not always obvious.  When the apk build is successful, the build output will end with messages about updating and signing the index -- but if the `APKBUILD` script doesn't detect failure properly, you might end up with an empty apk.
   * You'll also see `fatal: No names found, cannot describe anything.`, but don't worry, it's not actually fatal

### Workflow for new Alpine releases

All packages must be rebuilt for new Alpine releases.  Here is our general workflow for that:

1. For each package, in [dependency order](dependencies.md):
   1. Check [Alpine package search](https://pkgs.alpinelinux.org/packages) to see if it's now an official package.  If yes, delete the package from our repo.  If no, continue with the rest of these steps.
   2. Check the package's home page to see if there's a new version.  Update the APKBUILD file appropriately.  If there is not a new version, we usually bump the build number in the APKBUILD file.
   3. Build the APK using the apkbuilder build script: `sudo ./build <branch> <subdir>`
      * This step automatically updates the APKINDEX - it may be easier to have one person build the "master" copy of the repo instead of trying to have everyone keep in sync.
    
## For testing: Serving APKs from within the [jupyter-alpine](https://github.com/nbgallery/jupyter-docker) image

If you don't have a web server to host the apks, you can mount them into the jupyter-alpine docker image.  If the apks live locally at, say, `packages-3.7/apks/x86_64/*.apk`, then run the image something like this:

```
docker run --rm -it -p 443:443 -p 80:80 -v `pwd`/packages-3.7:/root/.jupyter/static nbgallery/jupyter-alpine bash
```

That will mount the local package directory into the container at `/root/.jupyter/static`, which is already configured as an extra static file path for the Jupyter web server.  It will then run the `nbgallery/jupyter-alpine` image, but drop you into a bash shell instead of starting Jupyter.

Note: If you're not using our official nbgallery apk key (i.e. you generated your own with `abuild-keygen` as described above), you'll also need the `.pub` version inside the container -- either stick it in that same packages directory or add another `-v` option to mount the directory where it lives.  Once you're inside the container, copy it to `/etc/apk/keys` to make it a trusted signing key.

To configure Jupyter as an apk repository, you have two options:

1. Insecure mode
   1. Edit the file `/etc/apk/repositories`.  Uncomment the plain http localhost entry at the bottom.
   2. Run Jupyter in insecure http mode.  From what I can tell, in recent versions of Jupyter, this also requires disabling password/token authentication:
      * If you're running a 7.x.x or later version of the `nbgallery/jupyter-alpine` image, try our wrapper script `jupyter-notebook-insecure-for-testing-only`
      * If not, you'll want something like `jupyter notebook --allow-root --JupyterApp.token='' --JupyterApp.password=''`
2. Secure mode.  From what I can tell, in Alpine 3.7 (and later, presumably), this will not work because `apk` will do a certificate verification, which fails due to the self-signed cert generated by `jupyter-notebook-secure`.
   1. Edit the file `/etc/apk/repositories`.  Uncomment the secure https localhost entry at the bottom.
   2. Run Jupyter in secure https mode.  Try our wrapper script `jupyter-notebook-secure`, which is normally the default entrypoint for the image.

Once you have Jupyter running, it will now also act as an apk repository server.  That will enable our dynamic kernel installation to work while you're testing.  You can also verify this is working by opening a Jupyter terminal and running `apk update` or other `apk` commands.

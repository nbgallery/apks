# nb.gallery APKs 

These APKs are used by the nb.gallery Docker client to dynamically install kernels. 

## apkbuilder docker image

[This image](https://hub.docker.com/r/nbgallery/apkbuilder/) can be used to build the apks in this project.  By default it will use a signing key from this directory and will mount source and package directories located here.  The image is similar to [alpine-jazz-hands](https://github.com/madedotcom/alpine-jazz-hands) but customized for the nbgallery project.

1. If needed, run `sudo ./build-image` to build the `nbgallery/apkbuilder` image.  Or just [pull it](https://hub.docker.com/r/nbgallery/apkbuilder/).
2. Copy the signing key to this directory.  The `build` script will pick it up automatically, or use the -k option.
3. Run `sudo ./build <subdir>` to build the apk from the specified subdir.  If you're running from this directory, the source and package directories should get set automatically.

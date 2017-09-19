FROM nbgallery/apkbuilder:3.6
MAINTAINER team@nb.gallery

# Build-time dependencies
USER root
RUN apk --update add cmake python && rm -rf /var/cache/apk/*

# Check out llvm
USER nbgallery
WORKDIR /home/nbgallery
RUN \
  git clone http://root.cern.ch/git/llvm.git src && \
  cd src && \
  git checkout cling-patches

# Check out clang
WORKDIR /home/nbgallery/src/tools
RUN \
  git clone http://root.cern.ch/git/clang.git && \
  cd clang && \
  git checkout cling-patches

# Check out cling
WORKDIR /home/nbgallery/src/tools
RUN git clone https://github.com/root-project/cling

# Apply patches
COPY patches /home/nbgallery/patches
WORKDIR /home/nbgallery/src/tools/cling
RUN patch -p1 < /home/nbgallery/patches/ValuePrinter.patch
RUN patch -p1 < /home/nbgallery/patches/Interpreter.patch

# Configure
COPY scripts/* /usr/local/bin/
WORKDIR /home/nbgallery/
RUN mkdir /home/nbgallery/build /home/nbgallery/install /home/nbgallery/apk
WORKDIR /home/nbgallery/build
RUN configure

# Build & install
RUN compile
RUN install

# Build APK
COPY APKBUILD /home/nbgallery/apk
WORKDIR /home/nbgallery/apk
ENTRYPOINT ["/usr/local/bin/build-apk"]

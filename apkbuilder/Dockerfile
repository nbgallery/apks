FROM alpine:edge
MAINTAINER team@nb.gallery

ENV SHELL=/bin/bash
ADD repositories /etc/apk/
ADD min-package build-apk /usr/local/bin/
RUN \
  apk update && \
  apk upgrade --available && \
  apk add alpine-sdk coreutils bash && \
  min-package https://archive.org/download/zeromq_4.0.4/zeromq-4.0.4.tar.gz && \
  ln -s libzmq.so.3 /usr/local/lib/libzmq.so.4 && \
  rm -rf /var/cache/apk/* && \
  adduser -G abuild -g "nbgallery" -s /bin/bash -D nbgallery && \
  echo "nbgallery ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER nbgallery
ADD abuild.conf /home/nbgallery/.abuild/
RUN echo "alias ll='ls -l'" >> /home/nbgallery/.bashrc
WORKDIR /home/nbgallery
ENTRYPOINT ["/usr/local/bin/build-apk"]

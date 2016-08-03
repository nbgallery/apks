# Building jg-IRkernel

IRKernel needs to be linked against lizmq. We use libzmq 4.0.4 since all kernels seem to be compatible with that version. To install libzmq on your apk build box, do the following: 

```bash 
$ curl -LO https://archive.org/download/zeromq_4.0.4/zeromq-4.0.4.tar.gz
$ tar -xzf zeromq-4.0.4.tar.gz
$ cd zeromq-4.0.4
$ ./configure && make && sudo make install
```

IRKernel expects libzmq 4 to have a libzmq.so.4 (seems reasonable), but the library install libzmq.so.3. For the build to succeed, you will need to symlink the library:

```bash
$ sudo ln -s /usr/local/lib/libzmq.so.3 /usr/local/lib/libzmq.so.4
```

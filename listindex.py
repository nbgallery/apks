#!/usr/bin/env python

import os
import sys
import tarfile

if len(sys.argv) < 2:
  print("Usage: {} /path/to/APKINDEX.tar.gz".format(os.path.basename(sys.argv[0])))
  sys.exit(1)

tar = tarfile.open(sys.argv[1])
index = tar.extractfile('APKINDEX')

packages = []
current = ''
for line in index:
  line = line.strip()
  if line:
    if line.startswith(b'P:'):
      current = line[2:]
    if line.startswith(b'V:'):
      version = line[2:]
      packages.append((current, version))
  else:
    current = ''

packages.sort()
for (package, version) in packages:
  print(package.decode('utf-8'), version.decode('utf-8'))

#!/usr/bin/env python

import sys
import os

if len(sys.argv) > 1:
    apps = sys.argv[1:]
else:
    apps = ["api", "builder", "product", "image", "page"]  # deliver user

for i in apps:
    os.system("python manage.py loaddata {0}".format(i))

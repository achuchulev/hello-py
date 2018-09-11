#!/usr/bin/env python
import subprocess
from subprocess import check_output

out = subprocess.check_output("./hello.py")

print out

if out.find("Hello!") != -1:
    print('Good!')
else:
    print('Bad!')
    subprocess.call("exit 1", shell=True)

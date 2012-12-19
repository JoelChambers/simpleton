#!/usr/bin/env python

import time, os, sys
import urllib, ftplib, smtplib, yaml
from termcolor import colored, cprint

if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
    fh = open(os.path.join(os.getenv('HOME'), '.simpleton.yaml'))

services = yaml.load(fh)
tests, passed, started = (0, 0, time.time())

for k, v in services.items():
    for u in v:
        tests += 1
        msg = '* testing %s: %s' % (k, u)
        out = colored(msg, 'green')
        try:
            if k == 'HTTP':
                urllib.urlopen(u)
            if k == 'FTP':
                ftplib.FTP(u)
            if k == 'SMTP':
                smtplib.SMTP(u)
            passed += 1
        except Exception, e:
            out = colored(msg, 'red')

        print out

print '%d of %d tests passed in %d seconds' % (passed, tests, int(time.time() - started))

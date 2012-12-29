#!/usr/bin/env python

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import time
import os
import sys
import urllib
import ftplib
import smtplib
import urlparse
import subprocess
import tempfile
from termcolor import colored, cprint

if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
    fh = open(os.path.join(os.getenv('HOME'), '.simpleton'))

tests, passed, started = (0, 0, time.time())

for l in fh.readlines():
    url = l.strip()
    parsed = urlparse.urlparse(url)
    tests += 1
    msg = '* testing %s' % (url)
    out = colored(msg, 'green')

    try:
        if parsed.scheme == 'http':
            urllib.urlopen(url)
        if parsed.scheme == 'ftp':
            ftplib.FTP(parsed.netloc)
        if parsed.scheme == 'smtp':
            smtplib.SMTP(parsed.netloc)
        if parsed.scheme == 'afp':
            tmp_path = tempfile.mkdtemp()
            subprocess.check_call(['/sbin/mount_afp', '-o', 'nobrowse', url, tmp_path])
            subprocess.check_call(['/sbin/umount', tmp_path])
            os.rmdir(tmp_path)
        passed += 1
    except Exception, e:
        out = colored(msg, 'red')

    print out

print '%d of %d tests passed in %d seconds' % (passed, tests, int(time.time() - started))

simpleton
=========

A simple tool to check that your services are up. About as braindead as it gets, but better than nothing. ;-)


Installation
============
1. Install prerequisites:
    
    sudo pip install pyyaml termcolor

2. Create your ~/.simpleton.yaml file:

    HTTP:
        - http://intra.example.com

    SMTP:
        - mail.example.com

    FTP:
        - files.example.com

Todo
====
- Add more protocol support, even simple socket connections would be good
- Deeper checks (SMTP sending, FTP logins, HTML parsing, etc)

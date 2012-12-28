simpleton
=========

A simple tool to check that your services are up. About as braindead as it gets, but hopefully better than nothing. ;-)


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

        AFP:
            - username:password@files.example.com/share

Todo
====
- Add more protocol support, even simple socket connections would be good
- Deeper checks (SMTP sending, FTP logins, HTML parsing, etc)


License
=======
                    DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                            Version 2, December 2004

         Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

         Everyone is permitted to copy and distribute verbatim or modified
         copies of this license document, and changing it is allowed as long
         as the name is changed.

                    DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
           TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

          0. You just DO WHAT THE FUCK YOU WANT TO.

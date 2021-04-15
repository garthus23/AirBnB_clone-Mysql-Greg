#!/usr/bin/python3
# Distribute an archive
''' module fabric to make commands '''
from fabric.api import *


env.hosts = ['34.75.62.192', '35.196.192.33', ]


def do_clean(number=0):
    ''' clean some archive'''
    if int(number) < 2 and int(number) >= 0:
        local("cd versions && ls -t | tail -n +2 | xargs rm -f")
        run("cd /data/web_static/releases && ls -t | tail -n +2 | \
            xargs rm -rf")
    else:
        nlocal = local("cd versions && ls -t | wc -l", capture=True)
        todelete = int(nlocal) - int(number)
        if todelete > 0:
            local("cd versions && ls -t | tail -n %d | \
                  xargs rm -f" % (todelete))
        nremote = run("cd /data/web_static/releases && ls -t | \
                      grep web_static | wc -l")
        todelete = int(nremote) - int(number)
        if todelete > 0:
            run("cd /data/web_static/releases && ls -t | grep web_static | \
                tail -n %d | xargs rm -rf" % (todelete))

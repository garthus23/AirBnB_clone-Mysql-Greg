#!/usr/bin/python3
# generates a .tgz archive
''' module to execute cmd '''
from fabric.api import *

env.hosts = ['localhost', ]


def do_pack():
    ''' function to generate .tgz '''
    try:
        local("ls | grep -c versions", capture=False)
    except:
        local('mkdir versions', capture=False)
    try:
        local("tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz \
              web_static")
        result = local("ls -t versions | head -n 1")
        return result
    except:
        return None

#!/usr/bin/python3
# Distribute an archive
''' module fabric to make commands '''
from fabric.api import *


env.hosts = ['34.75.62.192', '35.196.192.33', ]


def do_deploy(archive_path):
    ''' deploy web content '''
    try:
        put(archive_path, '/tmp')
        # file name no extension
        fine = run("ls -t /tmp | head -n 1 | sed 's/\..*//'")
        run("mkdir -p /data/web_static/releases/%s" % (fine))
        # file name with extension
        fie = run("ls /tmp | grep .tgz")
        run("tar -xzf /tmp/%s -C /data/web_static/releases/%s" % (fie, fine))
        run("rm -f /tmp/%s" % (fie))
        run("mv /data/web_static/releases/%s//web_static/* \
            /data/web_static/releases/%s" % (fine, fine))
        run("rm -rf /data/web_static/releases/%s/web_static" % (fine))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/%s/ \
            /data/web_static/current" % (fine))
        return True
    except:
        return False

#!/usr/bin/python3
# do pack and do deploy
''' module to execute cmd '''
from fabric.api import *

env.hosts = ['34.75.62.192', '35.196.192.33', ]


def deploy():
    ''' deploy content '''
    def do_pack():
        ''' create archive '''
        try:
            local("ls | grep -c versions", capture=False)
        except:
            local('mkdir versions', capture=False)
        try:
            local("tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz \
                  web_static")
            archive_name = local("ls -t versions | grep web_static | \
                                 head -n 1", capture=True)
            do_deploy("versions/%s" % (archive_name))
        except:
            return None

    def do_deploy(archive_path):
        ''' upload archive, uncompress '''
        try:
            put(archive_path, '/tmp')
            # file name no extension
            fine = run("ls -t /tmp | head -n 1 | sed 's/\..*//'")
            run("mkdir -p /data/web_static/releases/%s" % (fine))
            # file name with extension
            fie = run("ls /tmp | grep .tgz")
            run("tar -xzf /tmp/%s -C \
                /data/web_static/releases/%s" % (fie, fine))
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

    do_pack()

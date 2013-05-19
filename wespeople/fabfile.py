from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['root@wespeople.com']

def deploy():
    code_dir = '/srv/www/wespeople.com/wespeople/WesPeople.com/wespeople'
    with cd(code_dir):
        run("git pull")
        run("supervisorctl -c /etc/supervisord.conf restart gunicorn")

#!/usr/bin/python3
"""packs and distributes an archive to two web servers"""
from fabric.api import *
from datetime import datetime
import os.path
from os.path import getsize

env.hosts = ['35.196.105.181', '3.93.188.97']


@task
def deploy():
    """uses do_pack and do_deploy"""
    path = do_pack()
    if path:
        return do_deploy(path)
    else:
        return False


@runs_once
def do_pack():
    local("mkdir -p versions")
    path_l = "versions/web_static_{:s}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    create_file = local("tar -cvzf {:s} web_static".format(path_l))
    if create_file.succeeded:
        print("web_static packed: {:s} -> {}Bytes".format(
            path_l, getsize(path_l)))
        return(path_l)
    else:
        return None


def do_deploy(archive_path):
    """transfer files to web server"""
    if os.path.isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        path_l = "/tmp/" + pre_path
        path_r = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(path_r))
        sudo("tar -xzf {:s} -C {:s}".format(path_l, path_r))
        sudo("rm {:s}".format(path_l))
        path_m = path_r + "/web_static/*"
        path_d = path_r + "/web_static/"
        sudo("mv {:s} {:s}".format(path_m, path_r))
        sudo("rm -rf {:s}".format(path_d))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(path_r))
        print("New version deployed!")
        return True
    else:
        return False

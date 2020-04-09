#!/usr/bin/python3
"""fab generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
from fabric.decorators import runs_once
from datetime import datetime
from os.path import getsize


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

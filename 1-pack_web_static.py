#!/usr/bin/env python3
"""fab generates a .tgz archive from the contents of the web_static"""
from fabric.api import local, runs_once
from datetime import datetime
import os


@runs_once
def do_pack():
    local("mkdir -p versions")
    path = "versions/web_static_{:s}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    print("Packing web_static to {:s}".format(path))
    create_file = local("tar -cvzf {:s} web_static".format(path))
    if create_file.succeeded:
        print("web_static packed: {:s} -> {}Bytes".format(
            path, os.path.getsize(path)))
        return(path)
    else:
        return None

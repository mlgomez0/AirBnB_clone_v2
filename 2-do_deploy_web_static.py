#!/usr/bin/env python3
"""distributes an archive to a web servers, using the function do_deploy"""
from fabric.api import *
import os

env.hosts = ['35.196.105.181', '3.93.188.97']


def do_deploy(archive_path):
    """transfer files to web server"""

    if os.path.isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        op1 = put(archive_path, "/tmp/")
        path_l = "/tmp/" + pre_path
        path_r = "/data/web_static/releases/" + pre_path.split(".")[0]
        op2 = sudo("mkdir -p {:s}".format(path_r))
        op3 = sudo("tar -xzf {:s} -C {:s}".format(path_l, path_r))
        op4 = sudo("rm {:s}".format(path_l))
        path_m = path_r + "/web_static/*"
        path_d = path_r + "/web_static/"
        op5 = sudo("mv {:s} {:s}".format(path_m, path_r))
        op6 = sudo("rm -rf {:s}".format(path_d))
        op7 = sudo("rm -rf /data/web_static/current")
        op8 = sudo("ln -s {:s} /data/web_static/current".format(path_r))
        ops = [op1, op2, op3, op4, op5, op6, op7, op8]
        return all([op.succeeded for op in ops])
    else:
        return False

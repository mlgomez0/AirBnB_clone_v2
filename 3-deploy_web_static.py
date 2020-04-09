#!/usr/bin/python3
"""packs and distributes an archive to two web servers"""
from fabric.api import *
import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """uses do_pack and do_deploy"""

    path = do_pack()
    return do_deploy(path)

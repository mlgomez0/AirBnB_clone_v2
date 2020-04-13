#!/usr/bin/python3
"""clean files in /data/web_static/releases in two servers"""
from fabric.api import *
import os

env.hosts = ['35.196.105.181', '3.93.188.97']


def do_clean(number=0):
    """clean files"""
    if int(number) == 0 or int(number) == 1:
        number = 1
    number = int(number) + 1
    with lcd("versions"):
        local("ls -1t | tail -n +{} | xargs rm -rf".format(number))
    with cd("/data/web_static/releases/"):
        sudo("ls -1t -I test | tail -n +{:d} | xargs rm -rf".format(number))

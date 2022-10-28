#!/usr/bin/python3
"""A fabric python script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""

from os import listdir
from fabric.api import *

env.hosts = ["3.233.234.234", "107.21.40.158"]


def do_clean(number=0):
    """This method deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

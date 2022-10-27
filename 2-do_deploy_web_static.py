#!/usr/bin/python3
"""A fabric python script that distributes an archive to the two web servers
"""
from os.path import exists
from fabric.api import run, put, env

env.hosts = ["3.233.234.234", "107.21.40.158"]


def do_deploy(archive_path):
    """This method distributes an archive to the two web servers
    """
    if not exists(archive_path):
        return False

    fileNameWithExt = archive_path.split("/")[1]
    fileName = archive_path.split("/")[1].split(".")[0]

    if put(archive_path, "/tmp/{}".format(
           fileNameWithExt)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".format(
           fileName)).succeeded is False:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(
           fileName)).succeeded is False:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
           fileNameWithExt, fileName)).succeeded is False:
        return False

    if run("rm /tmp/{}".format(fileNameWithExt)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(fileName, fileName)
           ).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(fileName)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(fileName)).succeeded is False:
        return False

    return True

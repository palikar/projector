import os
import shutil
import binaryornot.check as binary_check


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        sources = os.path.join(src, item)
        destd = os.path.join(dst, item)

        if os.path.isdir(sources):
            shutil.copytree(sources, destd, symlinks, ignore)
        else:
            shutil.copy2(sources, destd)


def copyfile(src, dst, symlinks=False, ignore=None):
    shutil.copy2(src, dst)


def is_binary(file):
    return binary_check.is_binary(file)

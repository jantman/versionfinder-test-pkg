import os
from versionfinder import find_version

def check_ver():
    return find_version('versionfinder_test_pkg')

def check_ver_file():
    fpath = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'version.py'
    ))
    return find_version('versionfinder_test_pkg', package_file=fpath)


class TopLevelClass(object):

    def find(self):
        fpath = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'version.py'
        ))
        return find_version('versionfinder_test_pkg', package_file=fpath)

    def find_with_file(self):
        return find_version('versionfinder_test_pkg')

import os
from versionfinder import find_version

def check_ver():
    return find_version('versionfinder_test_pkg', log=True)

def check_ver_file():
    fpath = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'version.py'
    ))
    return find_version('versionfinder_test_pkg', package_file=fpath, log=True)


class TopLevelClass(object):

    def find(self):
        fpath = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'version.py'
        ))
        return find_version('versionfinder_test_pkg',
                            package_file=fpath, log=True)

    def find_with_file(self):
        return find_version('versionfinder_test_pkg', log=True)

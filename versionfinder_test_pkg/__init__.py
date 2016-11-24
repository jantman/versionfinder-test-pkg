"""
The latest version of this package is available at:
<http://github.com/jantman/versionfinder-test-pkg>

##################################################################################
Copyright 2016 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of versionfinder-test-pkg, also known as versionfinder-test-pkg.

    versionfinder-test-pkg is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    versionfinder-test-pkg is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with versionfinder-test-pkg.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
##################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/versionfinder-test-pkg> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
##################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
##################################################################################
"""

import traceback
import json
import os
import logging
from versionfinder import find_version

from versionfinder_test_pkg.top_level_file import (
    check_ver, check_ver_file, TopLevelClass
)
from versionfinder_test_pkg.somedir.otherdir.nestedfile import (
    nested_check_ver, nested_check_ver_file, NestedClass
)

fmt = "[%(levelname)s %(filename)s:%(lineno)s - " \
      "%(name)s.%(funcName)s() ] %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)
logger = logging.getLogger()


def entrypoint():
    results = {}

    k = 'entrypoint'
    try:
        res = find_version('versionfinder_test_pkg')
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'entrypoint_other_file'
    try:
        fpath = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'version.py'
        ))
        res = find_version('versionfinder_test_pkg', package_file=fpath)
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'top_level_file_check'
    try:
        res = check_ver()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'top_level_file_check_file'
    try:
        res = check_ver_file()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'top_level_class_check'
    try:
        res = TopLevelClass().find()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'top_level_class_check_file'
    try:
        res = TopLevelClass().find_with_file()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'nested_file_check'
    try:
        res = nested_check_ver()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'nested_check_file'
    try:
        res = nested_check_ver_file()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'nested_class_check'
    try:
        res = NestedClass().find()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    k = 'nested_class_check_file'
    try:
        res = NestedClass().find_with_file()
        results[k] = {'failed': False, 'result': res}
    except Exception as ex:
        results[k] = {
            'failed': True,
            'exc_type': str(type(ex)),
            'exc_str': str(ex),
            'traceback': traceback.format_exc()
        }

    print(json.dumps(results))

if __name__ == "__main__":
    entrypoint()
#!/usr/bin/python
#
# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.core import setup

setup(name='capirca',
      maintainer='Google',
      maintainer_email='capirca-dev@googlegroups.com',
      version='1.108',
      url='http://code.google.com/p/capirca',
      license='Apache License, Version 2.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Security'],
      py_modules=['aclgen', 'lib.cisco', 'lib.ciscoasa', 'lib.iptables',
                  'lib.juniper', 'lib.nacaddr', 'lib.policy', 'lib.naming',
                  'lib.aclcheck', 'lib.aclgenerator', 'lib.port',
                  'lib.silverpeak', 'lib.speedway', 'third_party.ipaddr',
                  'third_party.ply.lex', 'third_party.ply.yacc'])
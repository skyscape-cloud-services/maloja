#!/usr/bin/env python
#   -*- encoding: UTF-8 -*-

# Copyright Skyscape Cloud Services
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from __future__ import unicode_literals

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import os.path
import shutil
import tempfile
import unittest

import pkg_resources
import ruamel.yaml

import maloja.plugin.vapplicator

from maloja.workflow.utils import plugin_interface
from maloja.workflow.utils import record


class DiscoveryTester(unittest.TestCase):

    def test_publishing(self):
        self.assertIn(
            maloja.plugin.vapplicator.plugin,
            dict(maloja.workflow.utils.plugin_interface()).values())

class NeedsTempDirectory:

    def setUp(self):
        self.drcty = tempfile.TemporaryDirectory()

    def tearDown(self):
        if os.path.isdir(self.drcty.name):
            self.drcty.cleanup()
        self.assertFalse(os.path.isdir(self.drcty.name))
        self.drcty = None

class RecordTests(NeedsTempDirectory, unittest.TestCase):

    def test_content_goes_to_named_file(self):
        fN = "node.yaml"
        fP = os.path.join(self.drcty.name, fN)
        self.assertFalse(os.path.isfile(fP))
        with record(fN, parent=self.drcty.name) as output:
            output.write(ruamel.yaml.dump("Test string"))

        self.assertTrue(os.path.isfile(fP))
        with open(fP, 'r') as check:
            self.assertEqual("Test string\n...", check.read().strip())

    def test_content_goes_to_file_object(self):
        fObj = StringIO()
        with record(fObj, parent=self.drcty.name) as output:
            output.write(ruamel.yaml.dump("Test string"))

        self.assertEqual("Test string\n...", fObj.getvalue().strip())

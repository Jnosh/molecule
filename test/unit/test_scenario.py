#  Copyright (c) 2015-2016 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import os

import pytest

from molecule import config
from molecule import scenario


@pytest.fixture
def scenario_instance(config_instance):
    return scenario.Scenario(config_instance)


def test_name_property(scenario_instance):
    assert 'default' == scenario_instance.name


def test_setup_property(scenario_instance):
    x = os.path.join(scenario_instance.directory, 'create.yml')

    assert x == scenario_instance.setup


def test_converge_property(scenario_instance):
    x = os.path.join(scenario_instance.directory, 'playbook.yml')

    assert x == scenario_instance.converge


def test_teardown_property(scenario_instance):
    x = os.path.join(scenario_instance.directory, 'destroy.yml')

    assert x == scenario_instance.teardown


@pytest.mark.parametrize(
    'config_instance', [{
        'molecule_file': config.molecule_file('/foo/bar/molecule/default/')
    }],
    indirect=['config_instance'])
def test_directory_property(config_instance):
    assert '/foo/bar/molecule/default' == config_instance.scenario.directory

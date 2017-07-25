# Copyright 2017 Cloudbase Solutions SRL
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oswin_tempest_plugin.tests._mixins import optional_feature
from oswin_tempest_plugin.tests import test_base


class QosTestCase(test_base.TestBase,
                  optional_feature._OptionalFeatureMixin):
    """QoS test suite.

    This test suite will spawn instances with QoS specs.

    Hyper-V uses normalized IOPS (8 KB increments), and the minimum IOPS that
    can be set is 1.
    """

    _FEATURE_FLAVOR = {
        'extra_specs': {'quota:disk_total_bytes_sec': '200'}}

# Copyright (c) 2015 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from oslo_config import cfg


_ADMIN_MODE_OPT = cfg.BoolOpt('admin_mode', default=False,
                              help='Activate privileged endpoints.')


_GENERAL_OPTIONS = (
    _ADMIN_MODE_OPT,
    cfg.BoolOpt('pooling', default=False,
                help=('Enable pooling across multiple storage backends. '
                      'If pooling is enabled, the storage driver '
                      'configuration is used to determine where the '
                      'catalogue/control plane data is kept.'),
                deprecated_opts=[cfg.DeprecatedOpt('sharding')]),
    cfg.BoolOpt('unreliable', default=None,
                help='Disable all reliability constrains.'),
)

_DRIVER_OPTIONS = (
    cfg.StrOpt('transport', default='wsgi',
               help='Transport driver to use.'),
    cfg.StrOpt('message_store', default='mongodb',
               deprecated_opts=[cfg.DeprecatedOpt('storage')],
               help='Storage driver to use as the messaging store.'),
    cfg.StrOpt('management_store', default='mongodb',
               help='Storage driver to use as the management store.'),
)

_DRIVER_GROUP = 'drivers'


def _config_options():
    return [(None, _GENERAL_OPTIONS),
            (_DRIVER_GROUP, _DRIVER_OPTIONS)]
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class LogRotate(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """LogRotate service
    """

    plugin_name = 'logrotate'
    profiles = ('system',)

    var_puppet_gen = "/var/lib/config-data/puppet-generated/crond"

    def setup(self):
        self.add_cmd_output("logrotate --debug /etc/logrotate.conf",
                            suggest_filename="logrotate_debug")
        self.add_copy_spec([
            "/etc/logrotate*",
            "/var/lib/logrotate.status",
            self.var_puppet_gen + "/etc/logrotate-crond.conf",
            self.var_puppet_gen + "/var/spool/cron/root"
        ])

# vim: set et ts=4 sw=4 :

# envvars.py
#
# Copyright 2020 brombinmirko <send@mirko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Handy

@Gtk.Template(resource_path='/com/usebottles/bottles/dialog-environment-variables.ui')
class EnvVarsDialog(Handy.Window):
    __gtype_name__ = 'EnvVarsDialog'

    # region Widgets
    entry_variables = Gtk.Template.Child()
    btn_cancel = Gtk.Template.Child()
    btn_save = Gtk.Template.Child()
    # endregion

    def __init__(self, window, config, **kwargs):
        super().__init__(**kwargs)
        self.set_transient_for(window)

        # common variables and references
        self.window = window
        self.manager = window.manager
        self.config = config
        variables = config["Parameters"]["environment_variables"]

        # set the default values
        self.entry_variables.set_text(variables)

        # connect signals
        self.btn_cancel.connect('pressed', self.__close_window)
        self.btn_save.connect('pressed', self.__save_variables)

    def __close_window(self, widget):
        self.destroy()

    def __save_variables(self, widget):
        '''
        This function take the new variables from the entry
        and save them to the bottle configuration. It will also
        close the window.
        '''
        variables = self.entry_variables.get_text()
        self.manager.update_config(
            config=self.config,
            key="environment_variables",
            value=variables,
            scope="Parameters"
        )
        self.__close_window(widget)
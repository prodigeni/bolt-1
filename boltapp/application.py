# Bolt Application
# Copyright (c) 2014 Hestia. All Rights Reserved.

from gi.repository import Gtk, Gio, GLib
from bolt.window import Window

class Bolt(Gtk.Application):
	def __init__(self):
		Gtk.Application.__init__(self, application_id="com.byhestia.Bolt", flags=Gio.ApplicationFlags.FLAGS_NONE)

		GLib.set_application_name("Bolt")
		GLib.set_prgname("bolt")

		self._window = None

	def _buildMenu(self):
		builder = Gtk.Builder()

		builder.add_from_resource('/com/byhestia/Bolt/bolt-menu.ui')

		menu = builder.get_object('app-menu')
		self.set_app_menu(menu)

		action = Gio.SimpleAction.new('about', None)
		action.connect('activate', self._about)
		self.add_action(action)

		action = Gio.SimpleAction.new('quit', None)
		action.connect('activate', self._quit)
		self.add_action(action)

	def _about(self, action=None, param=None):
		builder = Gtk.Builder()
		builder.add_from_resource('/com/byhestia/Bolt/about-dialog.ui')
		about = builder.get('about_dialog')
		about.set_transient_for(self._window)
		about.connect('response', self._response)
		about.show()

	def _response(self, dialog, response):
		dialog.destroy()

	def do_startup(self):
		Gtk.Application.do_startup(self)

		self._buildMenu()

	def _quit(self, action=None, param=None):
		self._window.destroy()

	def do_activate(self):
		self._window = Window(self)
		Gtk.main()
# Bolt Main Window
# Copyright (c) Hestia 2014. All Rights Reserved.

from gi.repository import Gtk, Gio

class Window(Gtk.ApplicationWindow):
	def __init__(self, app):
		Gtk.Window.__init__(self, application=app)

		box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.add(box)

		list_tasks = Gtk.ListView()
		tasks.set_size_request(250, -1)
		box.pack_start(list_tasks)

		self.set_titlebar(self._setupTitle())

		self.set_size_request(800, 500)
		self.set_title("Bolt")
		self.connect("delete-event", Gtk.main_quit)
		self.show_all()

	def _setupTitle(self):
		hb = Gtk.HeaderBar()
		hb.props.show_close_button = True
		hb.props.title = "Bolt"

		button = Gtk.Button()
		icon = Gio.ThemedIcon(name="list-add-symbolic")
		image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
		button.add(image)
		button.set_tooltip_text("Add Task")
		#button.connect('clicked', self._addTask)
		hb.pack_start(button)

		box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		Gtk.StyleContext.add_class(box.get_style_context(), "linked")

		# All, Today, Week and Someday views!
		button = Gtk.Button("All Tasks")
		box.add(button)

		button = Gtk.Button("Today")
		box.add(button)

		button = Gtk.Button("Week")
		box.add(button)

		button = Gtk.Button("Someday")
		box.add(button)

		hb.set_custom_title(box)

		return hb


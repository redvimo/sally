import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk


class Window(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
        self.window = Window()

    def start(self):
        self.window.show()
        Gtk.main()

    def stop(self):
        Gtk.main_quit()

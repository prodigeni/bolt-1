resource_file = $(shell $(GLIB_COMPILE_RESOURCES) --sourcedir=$(srcdir) --sourcedir=$(builddir) --generate-dependencies $(srcdir)/bolt.gresource.xml)

bolt.gresource: bolt.gresource.xml $(resource_files)
	$(AM_V_GEN) $(GLIB_COMPILE_RESOURCES) --target=$@ --sourcedir=$(srcdir) $<

resourcedir = $(pkgdatadir)
resource_DATA = bolt.gresource

#appsdir = $(datadir)/applications
#apps_DATA = bolt.desktop

# Icons
ic_16dir = $(datadir)/icons/hicolor/16x16/apps
ic_22dir = $(datadir)/icons/hicolor/22x22/apps
ic_32dir = $(datadir)/icons/hicolor/32x32/apps
ic_48dir = $(datadir)/icons/hicolor/48x48/apps
ic_256dir = $(datadir)/icons/hicolor/256x256/apps
ic_scalabledir = $(datadir)/icons/hicolor/scalable/apps

ic_16_DATA = icons/16/bolt.png
ic_22_DATA = icons/22/bolt.png
ic_32_DATA = icons/32/bolt.png
ic_48_DATA = icons/48/bolt.png
ic_256_DATA = icons/256/bolt.png
ic_scalable_DATA = icons/bolt.svg

ic_files = \
	$(ic_16_DATA) \
	$(ic_22_DATA) \
	$(ic_32_DATA) \
	$(ic_48_DATA) \
	$(ic_256_DATA) \
	$(ic_scalable_DATA)

gtk_update_icon_cache = gtk-update-icon-cache -f -t $(datadir)/icons/hicolor

install-data-hook: update-icon-cache
uninstall-hook: update-icon-cache
update-icon-cache:
	@-if test -z "$(DESTDIR)"; then \
		echo "Updating Gtk icon cache."; \
		$(gtk_update_icon_cache); \
	else \
		echo "*** Icon cache not updated.  After (un)install, run this:"; \
		echo "***   $(gtk_update_icon_cache)"; \
	fi

EXTRA_DIST = \
	$(icon_files) \
	$(resource_files) \
	bolt.gresource.xml \
	$(NULL)

CLEANFILES = \
	bolt.gresource \
	$(apps_DATA) \
	$(NULL)
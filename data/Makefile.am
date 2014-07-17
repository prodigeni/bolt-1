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

ic_16_DATA = icons/bolt-16.png
ic_22_DATA = icons/bolt-22.png
ic_32_DATA = icons/bolt-32.png
ic_48_DATA = icons/bolt-48.png
ic_256_DATA = icons/bolt-256.png

ic_files = \
	$(ic_16_DATA) \
	$(ic_22_DATA) \
	$(ic_32_DATA) \
	$(ic_48_DATA) \
	$(ic_256_DATA) \
	icons/hicolor/bolt.svg

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
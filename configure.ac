AC_PREREQ(2.6.3)
AC_INIT([bolt], [0.1], [http://github.com/byhestia/bolt/issues/], [bolt], [http://byhestia.com])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR([Makefile.am])
AC_CONFIG_HEADERS(config.h)

AM_INIT_AUTOMAKE([1.11 tar-ustar dist-xz no-dist-gzip -Wno-portability subdir-objects])
AM_MAINTAINER_MODE([enable])
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

AM_PATH_PYTHON([3])

AC_PROG_CC
AM_PROG_CC_C_O
LT_INIT([disable-static])

PKG_PROG_PKG_CONFIG([0.22])

GOBJECT_INTROSPECTION_REQUIRE([1.35.9])
PKG_CHECK_MODULES([GTK], [gtk+-3.0 >= 3.8])
PKG_CHECK_EXISTS([gtk+-3.0 >= 3.9.0], [GTK_OR_GD=Gtk], [GTK_OR_GD=Gd])
AC_SUBST(GTK_OR_GD)

GLIB_COMPILE_RESOURCES=`$PKG_CONFIG --variable glib_compile_resources gio-2.0`
AC_SUBST(GLIB_COMPILE_RESOURCES)

AC_CONFIG_FILES([
  Makefile
  data/Makefile
  data/about-dialog.ui
  boltapp/Makefile
])
AC_OUTPUT


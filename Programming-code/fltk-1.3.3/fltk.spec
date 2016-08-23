#
# "$Id: fltk.spec.in 8864 2011-07-19 04:49:30Z greg.ercolano $"
#
# RPM spec file for FLTK.
#
# Copyright 1998-2011 by Bill Spitzak and others.
#
# This library is free software. Distribution and use rights are outlined in
# the file "COPYING" which should have been included with this file.  If this
# file is missing or damaged, see the license at:
#
#      http://www.fltk.org/COPYING.php
#
# Please report all bugs and problems on the following page:
#
#      http://www.fltk.org/str.php
#

%define version @FL_MAJOR_VERSION@.@FL_MINOR_VERSION@.@FL_PATCH_VERSION@
%define release 1
%define prefix /usr

Summary: Fast Light Tool Kit (FLTK)
Name: fltk
Version: %{version}
Release: %{release}
License: LGPL
Group: System Environment/Libraries
Source: http://fltk.org/pub/fltk/1.3.3/fltk-1.3.3-source.tar.gz
URL: http://www.fltk.org/
Packager: FLTK Developer <fltk@fltk.org>
# use BuildRoot so as not to disturb the version already installed
BuildRoot: /var/tmp/fltk-%{PACKAGE_VERSION}

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a
cross-platform C++ GUI toolkit for UNIX(r)/Linux(r) (X11),
Microsoft(r) Windows(r), and MacOS(r) X.  FLTK provides modern
GUI functionality without the bloat and supports 3D graphics via
OpenGL(r) and its built-in GLUT emulation.

%package devel
Summary: FLTK Development Environment
Group: Development/Libraries

%description devel
Install fltk-devel if you need to develop FLTK applications. 
You'll need to install the fltk package if you plan to run
dynamically linked applications.

%package games
Summary: FLTK Games
Group: Games

%description games
Install fltk-games to play Block Attack!, Checkers, or Sudoku on your computer.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --mandir=%{_mandir} --enable-largefile --enable-shared --enable-threads --enable-xft --enable-xdbe --enable-xinerama

# If we got this far, all prerequisite libraries must be here.
make

%install
# these lines just make sure the directory structure in the
# RPM_BUILD_ROOT exists
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make -e DESTDIR=$RPM_BUILD_ROOT install install-desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{prefix}/lib
%{prefix}/lib/libfltk*.so.*

%files devel
%defattr(-,root,root)

%dir %{prefix}/bin
%{prefix}/bin/fltk-config
%{prefix}/bin/fluid

%dir %{prefix}/include/FL
%{prefix}/include/FL/*
%{prefix}/include/Fl

%dir %{prefix}/lib
%{prefix}/lib/libfltk*.so
%{prefix}/lib/libfltk*.a

%dir %{_mandir}
%{_mandir}/cat1/*
%{_mandir}/cat3/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%dir %{prefix}/share/doc/fltk
%{prefix}/share/doc/fltk/*

%dir %{prefix}/share/applications
%{prefix}/share/applications/*

%dir %{prefix}/share/icons
%{prefix}/share/icons/hicolor/*/apps/fluid.png

%dir %{prefix}/share/mimelnk
%{prefix}/share/mimelnk/*

%files games
%dir %{prefix}/bin
%{prefix}/bin/blocks
%{prefix}/bin/checkers
%{prefix}/bin/sudoku

%dir %{_mandir}
%{_mandir}/cat6/*
%{_mandir}/man6/*

%dir %{prefix}/share/applications
%{prefix}/share/applications/*

%dir %{prefix}/share/icons
%{prefix}/share/icons/hicolor/*/apps/blocks.png
%{prefix}/share/icons/hicolor/*/apps/checkers.png
%{prefix}/share/icons/hicolor/*/apps/sudoku.png

#
# End of "$Id: fltk.spec.in 8864 2011-07-19 04:49:30Z greg.ercolano $".
#
